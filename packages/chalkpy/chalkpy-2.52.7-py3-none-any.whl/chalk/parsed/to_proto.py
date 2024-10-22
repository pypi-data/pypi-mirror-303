from __future__ import annotations

import collections
import collections.abc
import inspect
import json
from datetime import timedelta
from typing import Any, Callable, ClassVar, Collection, Mapping, Optional, Sequence, Union, cast

import pyarrow as pa
from google.protobuf import duration_pb2

from chalk import DataFrame
from chalk._gen.chalk.arrow.v1 import arrow_pb2 as arrow_pb
from chalk._gen.chalk.expression.v1 import expression_pb2 as expr_pb
from chalk._gen.chalk.graph.v1 import graph_pb2 as pb
from chalk._gen.chalk.graph.v1 import sources_pb2 as sources_pb
from chalk._gen.chalk.graph.v1.graph_pb2 import CronFilterWithFeatureArgs
from chalk._validation.feature_validation import FeatureValidation
from chalk.features import (
    CacheStrategy,
    Feature,
    FeatureConverter,
    Features,
    FeatureWrapper,
    Filter,
    TimeDelta,
    TPrimitive,
    Underscore,
    ensure_feature,
    unwrap_feature,
)
from chalk.features._encoding.converter import PrimitiveFeatureConverter
from chalk.features._encoding.rich import TRich
from chalk.features.pseudofeatures import PSEUDONAMESPACE
from chalk.features.resolver import (
    Cron,
    OfflineResolver,
    OnlineResolver,
    ParseInfo,
    Resolver,
    ResolverArgErrorHandler,
    SinkResolver,
    StateDescriptor,
    StreamResolver,
)
from chalk.features.underscore import (
    DoubleUnderscore,
    UnderscoreAttr,
    UnderscoreBinaryOp,
    UnderscoreBytesToString,
    UnderscoreCall,
    UnderscoreCoalesce,
    UnderscoreCosineSimilarity,
    UnderscoreFunction,
    UnderscoreGetJSONValue,
    UnderscoreGunzip,
    UnderscoreIfThenElse,
    UnderscoreItem,
    UnderscoreMD5,
    UnderscoreRoot,
    UnderscoreStringToBytes,
    UnderscoreTotalSeconds,
    UnderscoreUnaryOp,
)
from chalk.importer import SQLSourceGroup
from chalk.parsed._proto.utils import (
    seconds_int_to_proto_duration,
    seconds_to_proto_duration,
    timedelta_to_proto_duration,
)
from chalk.parsed.expressions import is_valid_operation
from chalk.queries.named_query import NamedQuery
from chalk.sql import (
    BigQuerySourceImpl,
    CloudSQLSourceImpl,
    DatabricksSourceImpl,
    MySQLSourceImpl,
    PostgreSQLSourceImpl,
    RedshiftSourceImpl,
    SnowflakeSourceImpl,
    SQLiteSourceImpl,
)
from chalk.sql._internal.sql_source import BaseSQLSource, SQLSourceKind
from chalk.streams import KafkaSource, KinesisSource, StreamSource
from chalk.streams._pubsub_source import PubSubSource
from chalk.streams.types import (
    StreamResolverParam,
    StreamResolverParamKeyedState,
    StreamResolverParamMessage,
    StreamResolverParamMessageWindow,
)
from chalk.utils import paths
from chalk.utils.collections import get_unique_item
from chalk.utils.duration import CronTab, Duration, parse_chalk_duration
from chalk.utils.source_parsing import should_skip_source_code_parsing

_CHALK_ANON_SQL_SOURCE_PREFIX = "__chalk_anon_sql_source_"
_CHALK_ANON_STREAM_SOURCE_PREFIX = "__chalk_anon_stream_source_"


class ToProtoConverter:
    _agg_to_protobuf: ClassVar[Mapping[str, "expr_pb.AggregateFunction"]] = {
        "approx_count_distinct": expr_pb.AGGREGATE_FUNCTION_APPROX_DISTINCT,
        "count": expr_pb.AGGREGATE_FUNCTION_COUNT,
        "count_distinct": expr_pb.AGGREGATE_FUNCTION_APPROX_DISTINCT,
        "first": expr_pb.AGGREGATE_FUNCTION_FIRST_VALUE,
        "group": expr_pb.AGGREGATE_FUNCTION_GROUPING,
        "last": expr_pb.AGGREGATE_FUNCTION_LAST_VALUE,
        "max": expr_pb.AGGREGATE_FUNCTION_MAX,
        "mean": expr_pb.AGGREGATE_FUNCTION_AVG,
        "median": expr_pb.AGGREGATE_FUNCTION_MEDIAN,
        "min": expr_pb.AGGREGATE_FUNCTION_MIN,
        "std": expr_pb.AGGREGATE_FUNCTION_STDDEV,
        "std_sample": expr_pb.AGGREGATE_FUNCTION_STDDEV,
        "stddev": expr_pb.AGGREGATE_FUNCTION_STDDEV,
        "stddev_sample": expr_pb.AGGREGATE_FUNCTION_STDDEV,
        "sum": expr_pb.AGGREGATE_FUNCTION_SUM,
        "var": expr_pb.AGGREGATE_FUNCTION_VARIANCE,
        "var_sample": expr_pb.AGGREGATE_FUNCTION_VARIANCE,
        "variance": expr_pb.AGGREGATE_FUNCTION_VARIANCE,
        "variance_sample": expr_pb.AGGREGATE_FUNCTION_VARIANCE,
        # "product": expr_pb.AGGREGATE_FUNCTION_PRODUCT,
    }
    _arg_taking_aggs: ClassVar = (
        "concat",
        "concat_str",
        "quantile",
    )
    _mode_to_proto: ClassVar[Mapping[str, pb.WindowMode]] = {
        "tumbling": pb.WINDOW_MODE_TUMBLING,
        "continuous": pb.WINDOW_MODE_CONTINUOUS,
        "cdc": pb.WINDOW_MODE_CDC,
    }
    _cache_strategy_to_proto: ClassVar[Mapping[CacheStrategy, "pb.CacheStrategy"]] = {
        CacheStrategy.ALL: pb.CACHE_STRATEGY_ALL,
        CacheStrategy.NO_NULLS: pb.CACHE_STRATEGY_NO_NULLS,
        CacheStrategy.EVICT_NULLS: pb.CACHE_STRATEGY_EVICT_NULLS,
    }
    _source_kind_to_enum: ClassVar[Mapping[SQLSourceKind, "sources_pb.DatabaseSourceType"]] = {
        SQLSourceKind.bigquery: sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_BIGQUERY,
        SQLSourceKind.cloudsql: sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_CLOUDSQL,
        SQLSourceKind.databricks: sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_DATABRICKS,
        SQLSourceKind.mysql: sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_MYSQL,
        SQLSourceKind.postgres: sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_POSTGRES,
        SQLSourceKind.redshift: sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_REDSHIFT,
        SQLSourceKind.snowflake: sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_SNOWFLAKE,
        SQLSourceKind.sqlite: sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_SQLITE,
    }
    _supported_stream_source_types: ClassVar[tuple[type[StreamSource], ...]] = (KafkaSource, KinesisSource)
    _supported_db_source_types: ClassVar[tuple[type[BaseSQLSource], ...]] = (
        BigQuerySourceImpl,
        CloudSQLSourceImpl,
        DatabricksSourceImpl,
        MySQLSourceImpl,
        PostgreSQLSourceImpl,
        RedshiftSourceImpl,
        SnowflakeSourceImpl,
        SQLiteSourceImpl,
    )

    @classmethod
    def convert_underscore(cls, v: Union[Underscore, TPrimitive]) -> expr_pb.LogicalExprNode:
        if isinstance(v, UnderscoreRoot):
            return expr_pb.LogicalExprNode(identifier=expr_pb.Identifier(name="_"))
        elif isinstance(v, DoubleUnderscore):
            return expr_pb.LogicalExprNode(identifier=expr_pb.Identifier(name="__"))
        elif isinstance(v, UnderscoreAttr):
            return expr_pb.LogicalExprNode(
                get_attribute=expr_pb.ExprGetAttribute(
                    parent=cls.convert_underscore(v._chalk__parent),  # pyright: ignore[reportPrivateUsage]
                    attribute=expr_pb.Identifier(name=v._chalk__attr),  # pyright: ignore[reportPrivateUsage]
                )
            )
        elif isinstance(v, UnderscoreItem):
            raw_key = v._chalk__key  # pyright: ignore[reportPrivateUsage]
            converted_keys: list[expr_pb.LogicalExprNode] = []
            if isinstance(raw_key, tuple):
                converted_keys.extend([cls.convert_underscore(k) for k in raw_key])
            else:
                converted_keys.append(cls.convert_underscore(raw_key))

            return expr_pb.LogicalExprNode(
                get_subscript=expr_pb.ExprGetSubscript(
                    parent=cls.convert_underscore(v._chalk__parent),  # pyright: ignore[reportPrivateUsage]
                    subscript=converted_keys,
                )
            )
        elif isinstance(v, UnderscoreCall):
            args = [cls.convert_underscore(arg) for arg in v._chalk__args]  # pyright: ignore[reportPrivateUsage]
            kwargs = {
                k: cls.convert_underscore(v) for k, v in v._chalk__kwargs.items()  # pyright: ignore[reportPrivateUsage]
            }
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=cls.convert_underscore(v._chalk__parent),  # pyright: ignore[reportPrivateUsage]
                    args=args,
                    kwargs=kwargs,
                )
            )
        elif isinstance(v, UnderscoreBinaryOp):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(
                        identifier=expr_pb.Identifier(name=v._chalk__op)  # pyright: ignore[reportPrivateUsage]
                    ),
                    args=[
                        cls.convert_underscore(v._chalk__left),  # pyright: ignore[reportPrivateUsage]
                        cls.convert_underscore(v._chalk__right),  # pyright: ignore[reportPrivateUsage]
                    ],
                )
            )
        elif isinstance(v, UnderscoreUnaryOp):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(
                        identifier=expr_pb.Identifier(name=v._chalk__op)  # pyright: ignore[reportPrivateUsage]
                    ),
                    args=[cls.convert_underscore(v._chalk__operand)],  # pyright: ignore[reportPrivateUsage]
                )
            )
        elif isinstance(v, UnderscoreIfThenElse):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(identifier=expr_pb.Identifier(name="if_then_else")),
                    args=[
                        cls.convert_underscore(v._chalk__condition),  # pyright: ignore[reportPrivateUsage]
                        cls.convert_underscore(v._chalk__if_true),  # pyright: ignore[reportPrivateUsage]
                        cls.convert_underscore(v._chalk__if_false),  # pyright: ignore[reportPrivateUsage]
                    ],
                )
            )
        elif isinstance(v, UnderscoreMD5):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(identifier=expr_pb.Identifier(name="md5")),
                    args=[cls.convert_underscore(v._chalk__value)],  # pyright: ignore[reportPrivateUsage]
                )
            )
        elif isinstance(v, UnderscoreCoalesce):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(identifier=expr_pb.Identifier(name="coalesce")),
                    args=[cls.convert_underscore(arg) for arg in v._chalk__vals],  # pyright: ignore[reportPrivateUsage]
                )
            )
        elif isinstance(v, UnderscoreBytesToString):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(identifier=expr_pb.Identifier(name="bytes_to_string")),
                    args=[
                        cls.convert_underscore(v._chalk__value),  # pyright: ignore[reportPrivateUsage]
                        cls.convert_underscore(v._chalk__encoding),  # pyright: ignore[reportPrivateUsage]
                    ],
                )
            )
        elif isinstance(v, UnderscoreStringToBytes):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(identifier=expr_pb.Identifier(name="string_to_bytes")),
                    args=[
                        cls.convert_underscore(v._chalk__value),  # pyright: ignore[reportPrivateUsage]
                        cls.convert_underscore(v._chalk__encoding),  # pyright: ignore[reportPrivateUsage]
                    ],
                )
            )
        elif isinstance(v, UnderscoreGetJSONValue):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(identifier=expr_pb.Identifier(name="json_value")),
                    args=[
                        cls.convert_underscore(v._chalk__value),  # pyright: ignore[reportPrivateUsage]
                        cls.convert_underscore(v._chalk__path),  # pyright: ignore[reportPrivateUsage]
                    ],
                )
            )
        elif isinstance(v, UnderscoreGunzip):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(identifier=expr_pb.Identifier(name="gunzip")),
                    args=[cls.convert_underscore(v._chalk__value)],  # pyright: ignore[reportPrivateUsage]
                )
            )
        elif isinstance(v, UnderscoreCosineSimilarity):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(identifier=expr_pb.Identifier(name="cosine_similarity")),
                    args=[
                        cls.convert_underscore(v._chalk__a),  # pyright: ignore[reportPrivateUsage]
                        cls.convert_underscore(v._chalk__b),  # pyright: ignore[reportPrivateUsage]
                    ],
                )
            )
        elif isinstance(v, UnderscoreTotalSeconds):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(identifier=expr_pb.Identifier(name="total_seconds")),
                    args=[cls.convert_underscore(v._chalk__delta)],  # pyright: ignore[reportPrivateUsage]
                )
            )
        elif isinstance(v, UnderscoreFunction):
            return expr_pb.LogicalExprNode(
                call=expr_pb.ExprCall(
                    func=expr_pb.LogicalExprNode(
                        identifier=expr_pb.Identifier(
                            name=v._chalk__function_name  # pyright: ignore[reportPrivateUsage]
                        )
                    ),
                    args=[cls.convert_underscore(arg) for arg in v._chalk__vals],  # pyright: ignore[reportPrivateUsage]
                )
            )
        else:
            if isinstance(v, Underscore):
                raise TypeError(f"Unknown underscore type: {type(v).__name__}")
            else:
                converter = FeatureConverter(name="convert_underscore", is_nullable=False, rich_type=type(v))
                return expr_pb.LogicalExprNode(
                    literal_value=expr_pb.ExprLiteral(value=converter.from_rich_to_protobuf(v))
                )

    @staticmethod
    def _convert_stream_source(source: StreamSource) -> sources_pb.StreamSource:
        source_name = source.name
        if isinstance(source, KafkaSource):
            return sources_pb.StreamSource(
                kafka=sources_pb.KafkaSource(
                    name=source_name,
                    bootstrap_servers=(
                        [source.bootstrap_server]
                        if isinstance(source.bootstrap_server, str)
                        else source.bootstrap_server
                    ),
                    topic=source.topic,
                    ssl_keystore_location=source.ssl_keystore_location,
                    ssl_ca_file=source.ssl_ca_file,
                    client_id_prefix=source.client_id_prefix,
                    group_id_prefix=source.group_id_prefix,
                    security_protocol=source.security_protocol,
                    sasl_mechanism=source.sasl_mechanism,
                    sasl_username=source.sasl_username,
                    sasl_password=source.sasl_password,
                    late_arrival_deadline=timedelta_to_proto_duration(
                        parse_chalk_duration(source.late_arrival_deadline)
                    ),
                    dead_letter_queue_topic=source.dead_letter_queue_topic,
                )
            )
        elif isinstance(source, KinesisSource):
            return sources_pb.StreamSource(
                kinesis=sources_pb.KinesisSource(
                    name=source_name,
                    stream_name=source.stream_name,
                    stream_arn=source.stream_arn,
                    region_name=source.region_name,
                    late_arrival_deadline=timedelta_to_proto_duration(
                        parse_chalk_duration(source.late_arrival_deadline)
                    ),
                    dead_letter_queue_stream_name=source.dead_letter_queue_stream_name,
                    aws_access_key_id=source.aws_access_key_id,
                    aws_secret_access_key=source.aws_secret_access_key,
                    aws_session_token=source.aws_session_token,
                    endpoint_url=source.endpoint_url,
                    consumer_role_arn=source.consumer_role_arn,
                )
            )
        elif isinstance(source, PubSubSource):
            return sources_pb.StreamSource(
                pubsub=sources_pb.PubSubSource(
                    name=source_name,
                    project_id=source.project_id,
                    subscription_id=source.subscription_id,
                    late_arrival_deadline=timedelta_to_proto_duration(
                        parse_chalk_duration(source.late_arrival_deadline)
                    ),
                    dead_letter_queue_topic=source.dead_letter_queue_topic_id,
                )
            )
        else:
            raise TypeError(f"Unknown stream source type: {type(source).__name__}")

    @staticmethod
    def _convert_named_query(source: NamedQuery) -> pb.NamedQuery:
        # Ignoring source.errors when converting named queries because structured errors in named queries
        # prevent that specific query from being used at runtime.
        if source.planner_options is not None:
            try:
                parsed_planner_options = {k: str(v) for k, v in source.planner_options.items()}
            except Exception as e:
                raise ValueError(f"Could not parse provided planner options '{source.planner_options}'") from e
        else:
            parsed_planner_options = None

        parsed_duration: dict[str, duration_pb2.Duration] | None = (
            None
            if source.staleness is None
            else {k: timedelta_to_proto_duration(parse_chalk_duration(v)) for (k, v) in source.staleness.items()}
        )

        try:
            return pb.NamedQuery(
                name=source.name,
                query_version=source.version,
                input=source.input,
                output=source.output,
                tags=source.tags,
                description=source.description,
                owner=source.owner,
                meta=source.meta,
                staleness=parsed_duration,
                planner_options=parsed_planner_options,
                file_name=source.filename,
            )
        except Exception as e:
            raise ValueError(f"Could not convert named query '{source.name}'") from e

    @staticmethod
    def convert_stream_source(source: StreamSource) -> sources_pb.StreamSource:
        try:
            return ToProtoConverter._convert_stream_source(source)
        except Exception as e:
            raise ValueError(f"Could not convert stream source '{source.name}'") from e

    @staticmethod
    def convert_engine_args(engine_args: Mapping[str, Any]) -> dict[str, arrow_pb.ScalarValue]:
        res: dict[str, arrow_pb.ScalarValue] = {}
        for k, v in engine_args.items():
            try:
                json_val = json.dumps(v)
            except Exception as e:
                raise ValueError(f"Could not convert engine arg '{k}' to JSON") from e
            res[k] = arrow_pb.ScalarValue(large_utf8_value=json_val)
        return res

    @staticmethod
    def _convert_sql_source(source: BaseSQLSource) -> sources_pb.DatabaseSource:
        source_name = source.name
        if isinstance(source, BigQuerySourceImpl):
            return sources_pb.DatabaseSource(
                bigquery=sources_pb.BigQuerySource(
                    name=source_name,
                    project=source.project,
                    dataset=source.dataset,
                    location=source.location,
                    credentials_base64=source.credentials_base64,
                    credentials_path=source.credentials_path,
                    engine_args=ToProtoConverter.convert_engine_args(source.engine_args),
                    async_engine_args=ToProtoConverter.convert_engine_args(source.async_engine_args),
                )
            )
        elif isinstance(source, CloudSQLSourceImpl):
            return sources_pb.DatabaseSource(
                cloudsql=sources_pb.CloudSQLSource(
                    name=source_name,
                    db=source.db,
                    user=source.user,
                    password=source.password,
                    instance_name=source.instance_name,
                    engine_args=ToProtoConverter.convert_engine_args(source.engine_args),
                    async_engine_args=ToProtoConverter.convert_engine_args(source.async_engine_args),
                )
            )
        elif isinstance(source, DatabricksSourceImpl):
            return sources_pb.DatabaseSource(
                databricks=sources_pb.DatabricksSource(
                    name=source_name,
                    host=source.host,
                    port=str(source.port),
                    db=source.db,
                    http_path=source.http_path,
                    access_token=source.access_token,
                    engine_args=ToProtoConverter.convert_engine_args(source.engine_args),
                    async_engine_args=ToProtoConverter.convert_engine_args(source.async_engine_args),
                )
            )
        elif isinstance(source, MySQLSourceImpl):
            return sources_pb.DatabaseSource(
                mysql=sources_pb.MySQLSource(
                    name=source_name,
                    host=source.host,
                    port=str(source.port),
                    db=source.db,
                    user=source.user,
                    password=source.password,
                    engine_args=ToProtoConverter.convert_engine_args(source.engine_args),
                    async_engine_args=ToProtoConverter.convert_engine_args(source.async_engine_args),
                )
            )
        elif isinstance(source, RedshiftSourceImpl):
            return sources_pb.DatabaseSource(
                redshift=sources_pb.RedshiftSource(
                    name=source_name,
                    host=source.host,
                    port=str(source.port),
                    db=source.db,
                    user=source.user,
                    password=source.password,
                    s3_bucket=source.s3_bucket,
                    engine_args=ToProtoConverter.convert_engine_args(source.engine_args),
                    async_engine_args=ToProtoConverter.convert_engine_args(source.async_engine_args),
                )
            )
        elif isinstance(source, SnowflakeSourceImpl):
            return sources_pb.DatabaseSource(
                snowflake=sources_pb.SnowflakeSource(
                    name=source_name,
                    db=source.name,
                    schema=source.schema,
                    role=source.role,
                    user=source.user,
                    password=source.password,
                    account_identifier=source.account_identifier,
                    warehouse=source.warehouse,
                    engine_args=ToProtoConverter.convert_engine_args(source.engine_args),
                    async_engine_args=ToProtoConverter.convert_engine_args(source.async_engine_args),
                )
            )
        elif isinstance(source, SQLiteSourceImpl):
            return sources_pb.DatabaseSource(
                sqlite=sources_pb.SQLiteSource(
                    name=source_name,
                    file_name=None if source.filename is None else str(source.filename),
                    engine_args=ToProtoConverter.convert_engine_args(source.engine_args),
                    async_engine_args=ToProtoConverter.convert_engine_args(source.async_engine_args),
                )
            )
        elif isinstance(source, PostgreSQLSourceImpl):
            return sources_pb.DatabaseSource(
                postgres=sources_pb.PostgresSource(
                    name=source_name,
                    host=source.host,
                    port=str(source.port),
                    db=source.db,
                    user=source.user,
                    password=source.password,
                    engine_args=ToProtoConverter.convert_engine_args(source.engine_args),
                    async_engine_args=ToProtoConverter.convert_engine_args(source.async_engine_args),
                )
            )
        else:
            raise ValueError(f"Unknown database source type: {type(source).__name__}")

    @staticmethod
    def convert_sql_source(source: BaseSQLSource) -> sources_pb.DatabaseSource:
        try:
            return ToProtoConverter._convert_sql_source(source)
        except Exception as e:
            raise ValueError(f"Could not convert SQL source '{source.name}'") from e

    @staticmethod
    def convert_cron_filter(cron: Union[CronTab, Duration, Cron]) -> Optional[CronFilterWithFeatureArgs]:
        if isinstance(cron, Cron) and cron.filter is not None:
            sig = inspect.signature(cron.filter)
            features: list[pb.FeatureReference] = []
            for parameter in sig.parameters.values():
                try:
                    feature = ensure_feature(parameter.annotation)
                except Exception as e:
                    raise ValueError("Cron filter arguments must be features") from e
                if not feature.is_feature_time and not feature.is_scalar:
                    raise ValueError("Cron filters must be scalars or feature time features")
                features.append(ToProtoConverter.create_feature_reference(feature))
            return CronFilterWithFeatureArgs(
                filter=ToProtoConverter.create_function_reference(cron.filter),
                args=features,
            )
        return None

    @staticmethod
    def convert_feature_to_filter_node(raw: Feature) -> expr_pb.LogicalExprNode:
        if raw.path:
            path_converted: list[expr_pb.Column] = []
            for p in raw.path:
                path_converted.append(
                    expr_pb.Column(name=p.parent.name, relation=expr_pb.ColumnRelation(relation=p.parent.namespace))
                )
            path_converted.append(
                expr_pb.Column(name=raw.name, relation=expr_pb.ColumnRelation(relation=raw.namespace))
            )

            return expr_pb.LogicalExprNode(
                binary_expr=expr_pb.BinaryExprNode(
                    operands=[expr_pb.LogicalExprNode(column=p) for p in path_converted],
                    op="foreign_feature_access",
                )
            )

        return expr_pb.LogicalExprNode(
            column=expr_pb.Column(name=raw.name, relation=expr_pb.ColumnRelation(relation=raw.namespace)),
        )

    @classmethod
    def convert_filter(cls, f: Filter) -> expr_pb.LogicalExprNode:
        if not is_valid_operation(f.operation):
            raise ValueError(f"Unknown operation '{f.operation}'")

        if f.operation in ("and", "or"):
            if not isinstance(f.lhs, Filter):
                raise ValueError("lhs of and/or must be a Filter")
            if not isinstance(f.rhs, Filter):
                raise ValueError("rhs of and/or must be a Filter")
            return expr_pb.LogicalExprNode(
                binary_expr=expr_pb.BinaryExprNode(
                    operands=[
                        ToProtoConverter.convert_filter(f.lhs),
                        ToProtoConverter.convert_filter(f.rhs),
                    ],
                    op=f.operation,
                ),
            )

        raw_lhs = f.lhs
        raw_rhs = f.rhs

        if isinstance(raw_lhs, FeatureWrapper):
            raw_lhs = unwrap_feature(raw_lhs)
        if isinstance(raw_rhs, FeatureWrapper):
            raw_rhs = unwrap_feature(raw_rhs)

        converted_lhs = raw_lhs
        converted_rhs = raw_rhs

        if isinstance(raw_lhs, Feature):
            if not raw_lhs.is_scalar and not raw_lhs.is_feature_time:
                raise ValueError("lhs of filter is a feature that is not scalar or feature-time")
            converted_lhs = ToProtoConverter.convert_feature_to_filter_node(raw_lhs)

        if isinstance(raw_rhs, Feature):
            if not raw_rhs.is_scalar and not raw_rhs.is_feature_time:
                raise ValueError("rhs of filter is a feature that is not scalar or feature-time")
            converted_rhs = ToProtoConverter.convert_feature_to_filter_node(raw_rhs)

        if isinstance(raw_lhs, Feature) and isinstance(raw_rhs, TimeDelta):
            # This means that the filter was a before() or after()
            duration_converter = PrimitiveFeatureConverter(
                name="helper", is_nullable=False, pyarrow_dtype=pa.duration("us")
            )
            converted_rhs = expr_pb.LogicalExprNode(
                literal=duration_converter.from_primitive_to_protobuf(raw_rhs.to_std())
            )
            assert isinstance(converted_lhs, expr_pb.LogicalExprNode), f"lhs is {converted_lhs}"
            return expr_pb.LogicalExprNode(
                binary_expr=expr_pb.BinaryExprNode(
                    operands=[converted_lhs, converted_rhs],
                    op=f.operation,
                ),
            )

        if not isinstance(raw_lhs, Feature):
            if not isinstance(raw_rhs, Feature):
                raise ValueError("One side must be a feature")
            if isinstance(raw_lhs, Underscore):
                converted_lhs = cls.convert_underscore(raw_lhs)
            else:
                converted_lhs = expr_pb.LogicalExprNode(
                    literal=raw_rhs.converter.from_primitive_to_protobuf(converted_lhs),
                )

        if not isinstance(raw_rhs, Feature):
            if not isinstance(raw_lhs, Feature):
                raise ValueError("One side must be a feature")
            if f.operation in ("in", "not in"):
                if not isinstance(raw_rhs, collections.abc.Iterable):
                    raise ValueError("rhs must be an iterable when operation is 'in'/'not in'")
                prim_values = tuple(raw_lhs.converter.from_rich_to_primitive(x) for x in raw_rhs)
                list_dtype = pa.large_list(raw_lhs.converter.pyarrow_dtype)
                list_converter = PrimitiveFeatureConverter(name="helper", is_nullable=False, pyarrow_dtype=list_dtype)
                converted_rhs = expr_pb.LogicalExprNode(
                    literal=list_converter.from_primitive_to_protobuf(prim_values),
                )
            elif isinstance(raw_rhs, Underscore):
                converted_rhs = cls.convert_underscore(raw_rhs)
            else:
                converted_rhs = expr_pb.LogicalExprNode(literal=raw_lhs.converter.from_rich_to_protobuf(raw_rhs))

        assert isinstance(converted_lhs, expr_pb.LogicalExprNode), f"lhs is {converted_lhs}"
        assert isinstance(converted_rhs, expr_pb.LogicalExprNode), f"rhs is {converted_rhs}"
        return expr_pb.LogicalExprNode(
            binary_expr=expr_pb.BinaryExprNode(
                operands=[converted_lhs, converted_rhs],
                op=f.operation,
            )
        )

    @staticmethod
    def create_database_source_reference(source: BaseSQLSource | SQLSourceGroup) -> sources_pb.DatabaseSourceReference:
        if source.kind == SQLSourceKind.bigquery:
            source_type = sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_BIGQUERY
        elif source.kind == SQLSourceKind.cloudsql:
            source_type = sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_CLOUDSQL
        elif source.kind == SQLSourceKind.databricks:
            source_type = sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_DATABRICKS
        elif source.kind == SQLSourceKind.dynamodb:
            source_type = sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_DYNAMODB
        elif source.kind == SQLSourceKind.mysql:
            source_type = sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_MYSQL
        elif source.kind == SQLSourceKind.postgres:
            source_type = sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_POSTGRES
        elif source.kind == SQLSourceKind.redshift:
            source_type = sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_REDSHIFT
        elif source.kind == SQLSourceKind.snowflake:
            source_type = sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_SNOWFLAKE
        elif source.kind == SQLSourceKind.sqlite:
            source_type = sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_SQLITE
        elif source.kind == SQLSourceKind.spanner:
            source_type = sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_SPANNER
        elif source.kind == SQLSourceKind.trino:
            source_type = sources_pb.DatabaseSourceType.DATABASE_SOURCE_TYPE_TRINO
        else:
            raise ValueError(f"Unknown database source kind: {source.kind}")

        return sources_pb.DatabaseSourceReference(
            name=source.name,
            type=source_type,
        )

    @staticmethod
    def convert_rich_type_to_protobuf(rich_type: type[TRich]) -> arrow_pb.ArrowType:
        converter = FeatureConverter(name="helper", is_nullable=False, rich_type=rich_type)
        return converter.convert_pa_dtype_to_proto_dtype(converter.pyarrow_dtype)

    @staticmethod
    def create_stream_source_reference(source: StreamSource) -> sources_pb.StreamSourceReference:
        if isinstance(source, KafkaSource):
            source_type = sources_pb.STREAM_SOURCE_TYPE_KAFKA
        elif isinstance(source, KinesisSource):
            source_type = sources_pb.STREAM_SOURCE_TYPE_KINESIS
        elif isinstance(source, PubSubSource):
            source_type = sources_pb.STREAM_SOURCE_TYPE_PUBSUB
        elif isinstance(source, StreamSource):
            # MockStreamSource
            source_type = sources_pb.STREAM_SOURCE_TYPE_UNSPECIFIED
        else:
            raise TypeError(f"Unknown stream source type: {type(source).__name__}")

        return sources_pb.StreamSourceReference(
            name=source.name,
            type=source_type,
        )

    @staticmethod
    def create_function_reference(
        fn: Callable,
        definition: Optional[str] = None,
        filename: Optional[str] = None,
        source_line: Optional[int] = None,
    ) -> pb.FunctionReference:
        module = inspect.getmodule(fn)
        if definition is None and not should_skip_source_code_parsing():
            try:
                definition = inspect.getsource(fn)
            except:
                pass
        return pb.FunctionReference(
            name=fn.__name__,
            module=module.__name__ if module else "",
            file_name=inspect.getfile(fn) if filename is None else filename,
            function_definition=definition,
            source_line=source_line,
        )

    @staticmethod
    def create_feature_reference(feature: Feature) -> pb.FeatureReference:
        df = None
        if feature.is_has_many:
            df = feature.typ.parsed_annotation
            if not isinstance(df, type) or not issubclass(df, DataFrame):
                raise ValueError("has-many feature missing `DataFrame` annotation")

        path: list[pb.FeatureReference] = []
        for path_elem in feature.path:
            converted = ToProtoConverter.create_feature_reference(path_elem.parent)
            if path_elem.parent.is_has_many:
                converted.df.ClearField("optional_columns")
                converted.df.ClearField("required_columns")
                # Selecting only the foreign feature to match
                # https://github.com/chalk-ai/chalk-private/blob/a480c8518ee2f4c3a97250741a3513167ab650ae/chalkruntime/chalkruntime/loader/converter.py#L517
                assert path_elem.parent.foreign_join_key is not None, "has-many must have a join key"
                converted.df.optional_columns.append(
                    ToProtoConverter.create_feature_reference(path_elem.parent.foreign_join_key)
                )
            path.append(converted)

        return pb.FeatureReference(
            name=feature.name,
            namespace=feature.namespace,
            path=path,
            df=ToProtoConverter.convert_dataframe(df) if df else None,
        )

    @staticmethod
    def convert_resolver_inputs(
        resolver_inputs: Sequence[Union[Feature, FeatureWrapper, type[DataFrame]]],
        state: Optional[StateDescriptor],
        default_args: Sequence[object],
    ) -> Sequence[pb.ResolverInput]:
        inputs: list[pb.ResolverInput] = []
        raw_inputs: list[Optional[Union[Feature, FeatureWrapper, type[DataFrame]]]] = list(resolver_inputs)
        if state is not None:
            raw_inputs.insert(state.pos, None)

        is_sole_dataframe_input = (
            len(resolver_inputs) == 1
            and isinstance(resolver_inputs[0], type)
            and issubclass(resolver_inputs[0], DataFrame)
        )
        if is_sole_dataframe_input:
            # TODO: Enforce check when there is uniformity in how many
            #       default args there are if there is a sole DF input
            # if len(resolver_inputs[0].columns) != len(default_args):
            #     raise ValueError(
            #         f"Length mismatch: found {len(resolver_inputs[0].columns)} DF "
            #         + f"columns and {len(default_args)} default arg"
            #     )
            pass
        else:
            if len(raw_inputs) != len(default_args):
                if (
                    resolver_inputs
                    and isinstance(resolver_inputs[0], type)
                    and issubclass(resolver_inputs[0], DataFrame)
                ):
                    # TODO: Remove this exception once we fix the incorrect default args count.
                    #       Currently we take the num columns of the first DF as the num default args,
                    #       regardless of whether it is the sole input.
                    pass
                else:
                    raise ValueError(
                        f"Length mismatch: found {len(raw_inputs)} `inputs` and {len(default_args)} `default_args`"
                    )

        for i in range(len(raw_inputs)):
            raw_input = raw_inputs[i]
            if state and i == state.pos:
                converter = FeatureConverter(
                    name="state", is_nullable=False, rich_type=state.typ, rich_default=state.initial
                )
                inputs.append(
                    pb.ResolverInput(
                        state=pb.ResolverState(
                            initial=converter.from_rich_to_protobuf(state.initial),
                            arrow_type=converter.convert_pa_dtype_to_proto_dtype(converter.pyarrow_dtype),
                        )
                    )
                )
            elif isinstance(raw_input, type) and issubclass(raw_input, DataFrame):
                inputs.append(pb.ResolverInput(df=ToProtoConverter.convert_dataframe(raw_input)))
            else:
                inp = ensure_feature(raw_inputs[i])
                default_arg = default_args[i]
                if default_arg is not None and not isinstance(default_arg, ResolverArgErrorHandler):
                    raise ValueError(f"Invalid default arg: {default_arg}")

                inputs.append(
                    pb.ResolverInput(
                        feature=pb.FeatureInput(
                            feature=ToProtoConverter.create_feature_reference(inp),
                            default_value=(
                                inp.converter.from_primitive_to_protobuf(default_arg.default_value)
                                if default_arg is not None
                                else None
                            ),
                        )
                    )
                )

        return inputs

    @staticmethod
    def convert_resolver_outputs(raw_outputs: Sequence[Union[Feature, type[DataFrame]]]) -> Sequence[pb.ResolverOutput]:
        outputs: list[pb.ResolverOutput] = []
        for o in raw_outputs:
            if isinstance(o, type) and issubclass(o, DataFrame):
                outputs.append(pb.ResolverOutput(df=ToProtoConverter.convert_dataframe(o)))
            elif isinstance(o, Feature):
                outputs.append(pb.ResolverOutput(feature=ToProtoConverter.create_feature_reference(o)))
            else:
                raise TypeError(f"Unknown output type: {type(o).__name__}")
        return outputs

    @staticmethod
    def convert_validations(validations: Sequence[FeatureValidation] | None) -> Sequence[pb.FeatureValidation] | None:
        if validations is None:
            return None

        res: list[pb.FeatureValidation] = []
        for val in validations:
            if val.min is not None:
                res.append(pb.FeatureValidation(min=val.min, strict=val.strict))
            if val.max is not None:
                res.append(pb.FeatureValidation(max=val.max, strict=val.strict))
            if val.min_length is not None:
                res.append(pb.FeatureValidation(min_length=val.min_length, strict=val.strict))
            if val.max_length is not None:
                res.append(pb.FeatureValidation(max_length=val.max_length, strict=val.strict))

        return res

    @staticmethod
    def convert_has_many(f: Feature) -> pb.FeatureType:
        if not f.is_has_many:
            raise ValueError("Should only be called on has_many features")
        if f.path:
            raise ValueError("Should not be called on features with `path`")
        if f.join is None:
            raise ValueError("Feature missing join")

        max_staleness_duration = None
        if f.max_staleness is not None:
            max_staleness_duration = timedelta_to_proto_duration(parse_chalk_duration(f.max_staleness))
        assert f.joined_class is not None
        res = pb.FeatureType(
            has_many=pb.HasManyFeatureType(
                name=f.name,
                namespace=f.namespace,
                is_autogenerated=f.is_autogenerated,
                join=ToProtoConverter.convert_filter(f.join),
                foreign_namespace=f.joined_class.namespace,
                max_staleness_duration=max_staleness_duration,
                tags=f.tags,
                owner=f.owner,
                description=f.description,
                attribute_name=f.attribute_name if hasattr(f, "attribute_name") else None,
            )
        )

        return res

    @staticmethod
    def convert_has_one(f: Feature) -> pb.FeatureType:
        if f.path:
            raise ValueError("Should not be called on features with `path`")
        if f.join is None:
            raise ValueError(f"Feature missing join {f.namespace}.{f.name}")
        if f.joined_class is None:
            raise ValueError("has-one relationships must reference a Features cls")
        if not isinstance(f.join.lhs, Feature):
            raise ValueError("lhs of join must be a Feature")
        if not isinstance(f.join.rhs, Feature):
            raise ValueError("rhs of join must be a Feature")

        res = pb.FeatureType(
            has_one=pb.HasOneFeatureType(
                name=f.name,
                namespace=f.namespace,
                is_nullable=f.typ.is_nullable,
                is_autogenerated=f.is_autogenerated,
                join=ToProtoConverter.convert_filter(f.join),
                foreign_namespace=f.joined_class.namespace,
                tags=f.tags,
                owner=f.owner,
                description=f.description,
                attribute_name=f.attribute_name if hasattr(f, "attribute_name") else None,
            )
        )
        return res

    @staticmethod
    def convert_feature_time_feature(f: Feature) -> pb.FeatureType:
        if not f.is_feature_time:
            raise ValueError("Should only be called on feature time features")

        return pb.FeatureType(
            feature_time=pb.FeatureTimeFeatureType(
                name=f.name,
                namespace=f.namespace,
                is_autogenerated=f.is_autogenerated,
                tags=f.tags,
                owner=f.owner,
                description=f.description,
                attribute_name=f.attribute_name if hasattr(f, "attribute_name") else None,
            )
        )

    @staticmethod
    def convert_windowed(f: Feature) -> pb.FeatureType:
        if not f.is_windowed:
            raise ValueError("Should only be called on windowed features")
        if f.path:
            raise ValueError("Should not be called on features with `path`")

        return pb.FeatureType(
            windowed=pb.WindowedFeatureType(
                name=f.name,
                namespace=f.namespace,
                is_autogenerated=f.is_autogenerated,
                window_durations=[seconds_to_proto_duration(d) for d in f.window_durations],
                attribute_name=f.attribute_name if hasattr(f, "attribute_name") else None,
            )
        )

    @staticmethod
    def convert_group_by_feature(f: Feature) -> pb.FeatureType:
        if not f.is_scalar:
            raise ValueError("Should only be called on scalar features")
        if f.path:
            raise ValueError("Should not be called on features with `path`")
        if f.group_by_windowed is None:
            raise ValueError("Feature is missing group_by_windowed")

        mat = f.group_by_windowed._window_materialization_parsed  # pyright: ignore[reportPrivateUsage]
        if mat is None:
            raise ValueError("Feature is missing window materialization")

        res = pb.FeatureType(
            group_by=pb.GroupByFeatureType(
                name=f.name,
                namespace=f.namespace,
                attribute_name=f.attribute_name if hasattr(f, "attribute_name") else None,
                arrow_type=f.converter.convert_pa_dtype_to_proto_dtype(f.converter.pyarrow_dtype),
                is_nullable=f.typ.is_nullable,
                description=f.description,
                owner=f.owner,
                default_value=f.converter.from_primitive_to_protobuf(f.converter.primitive_default)
                if f.converter.has_default
                else None,
                expression=None,
                # TODO: If we want this underscore expression to exist, we need to extend underscore parsing to handle group_by agg
                # expression=ToProtoConverter.convert_underscore(f.underscore_expression)
                # if f.underscore_expression
                # else None,
                window_durations=[seconds_to_proto_duration(d) for d in f.group_by_windowed.buckets_seconds],
                aggregation=pb.WindowAggregation(
                    namespace=mat.namespace,
                    group_by=[ToProtoConverter.create_feature_reference(feature=g) for g in mat.group_by],
                    bucket_duration=seconds_int_to_proto_duration(mat.bucket_duration_seconds),
                    aggregation=mat.aggregation,
                    aggregate_on=ToProtoConverter.create_feature_reference(feature=mat.aggregate_on)
                    if mat.aggregate_on is not None
                    else None,
                    arrow_type=PrimitiveFeatureConverter.convert_pa_dtype_to_proto_dtype(mat.pyarrow_dtype),
                    filters=[ToProtoConverter.convert_filter(f) for f in mat.filters],
                ),
                tags=f.tags,
                validations=ToProtoConverter.convert_validations(f.all_validations),
            )
        )
        return res

    @classmethod
    def convert_scalar(cls, f: Feature) -> pb.FeatureType:
        if not f.is_scalar:
            raise ValueError("Should only be called on scalar features")
        if f.path:
            raise ValueError("Should not be called on features with `path`")

        res = pb.FeatureType(
            scalar=pb.ScalarFeatureType(
                name=f.name,
                namespace=f.namespace,
                arrow_type=f.converter.convert_pa_dtype_to_proto_dtype(f.converter.pyarrow_dtype),
                is_distance_pseudofeature=f.is_distance_pseudofeature,
                is_nullable=f.typ.is_nullable,
                is_primary=f.primary,
                description=f.description,
                owner=f.owner,
                is_autogenerated=f.is_autogenerated,
                max_staleness_duration=(
                    None
                    if (f.raw_max_staleness is ... or f.raw_max_staleness is None)
                    else timedelta_to_proto_duration(parse_chalk_duration(f.raw_max_staleness))
                ),
                offline_ttl_duration=timedelta_to_proto_duration(parse_chalk_duration(f.offline_ttl)),
                window_info=(
                    pb.WindowInfo(
                        duration=seconds_to_proto_duration(f.window_duration),
                        aggregation=pb.WindowAggregation(
                            namespace=f.window_materialization_parsed.namespace,
                            group_by=[
                                ToProtoConverter.create_feature_reference(feature=g)
                                for g in f.window_materialization_parsed.group_by
                            ],
                            bucket_duration=seconds_int_to_proto_duration(
                                f.window_materialization_parsed.bucket_duration_seconds
                            ),
                            aggregation=f.window_materialization_parsed.aggregation,
                            aggregate_on=ToProtoConverter.create_feature_reference(
                                feature=f.window_materialization_parsed.aggregate_on
                            )
                            if f.window_materialization_parsed.aggregate_on is not None
                            else None,
                            arrow_type=PrimitiveFeatureConverter.convert_pa_dtype_to_proto_dtype(
                                f.window_materialization_parsed.pyarrow_dtype
                            ),
                            filters=[cls.convert_filter(f) for f in f.window_materialization_parsed.filters],
                        )
                        if f.window_materialization_parsed is not None
                        else None,
                    )
                    if f.window_duration is not None
                    else None
                ),
                # The protos are nullable; the type hint is wrong
                etl_offline_to_online=cast(bool, f.raw_etl_offline_to_online),
                tags=f.tags,
                version=(
                    pb.VersionInfo(
                        default=f.version.default,
                        maximum=f.version.maximum,
                    )
                    if f.version
                    else None
                ),
                last_for=ToProtoConverter.create_feature_reference(f.last_for) if f.last_for else None,
                default_value=(
                    f.converter.from_primitive_to_protobuf(f.converter.primitive_default)
                    if f.converter.has_default
                    else None
                ),
                validations=ToProtoConverter.convert_validations(f.all_validations),
                expression=ToProtoConverter.convert_underscore(f.underscore_expression)
                if f.underscore_expression
                else None,
                no_display=f.no_display,
                attribute_name=f.attribute_name if hasattr(f, "attribute_name") else None,
                is_deprecated=f.is_deprecated,
                cache_strategy=ToProtoConverter._cache_strategy_to_proto[f.cache_strategy],
            )
        )
        return res

    @staticmethod
    def _convert_feature(o: Feature) -> pb.FeatureType:
        if o.path:
            raise ValueError("Features with `path` not supported yet")
        elif o.group_by_windowed is not None:
            return ToProtoConverter.convert_group_by_feature(o)
        elif o.is_scalar:
            if o.is_windowed:  # nesting in o.is_scalar to prevent bugs
                return ToProtoConverter.convert_windowed(o)
            return ToProtoConverter.convert_scalar(o)
        elif o.is_feature_time:
            return ToProtoConverter.convert_feature_time_feature(o)
        elif o.is_has_one:
            return ToProtoConverter.convert_has_one(o)
        elif o.is_has_many:
            return ToProtoConverter.convert_has_many(o)

        raise ValueError(f"Unknown Feature object: {o}")

    @staticmethod
    def convert_feature(o: Feature) -> pb.FeatureType:
        try:
            return ToProtoConverter._convert_feature(o)
        except Exception as e:
            raise RuntimeError(f"Error converting feature '{o.namespace}.{o.name}'") from e

    @staticmethod
    def convert_dataframe(df: type[DataFrame]) -> pb.DataFrameType:
        return pb.DataFrameType(
            root_namespace=get_unique_item(x.root_namespace for x in df.columns if x.root_namespace != PSEUDONAMESPACE),
            optional_columns=[ToProtoConverter.create_feature_reference(ensure_feature(c)) for c in df.columns],
            # CHA-3177 -- switch to using this syntax
            # optional_columns=() if df.__references_feature_set__ is not None else [ToProtoConverter.create_feature_reference(ensure_feature(c)) for c in df.columns],
            required_columns=(),
            filter=expr_pb.LogicalExprNode(
                binary_expr=expr_pb.BinaryExprNode(
                    operands=[ToProtoConverter.convert_filter(f) for f in df.filters],
                    op="and",
                )
            )
            if df.filters
            else None,
            limit=df.__limit__ if df.__limit__ is not None else None,
        )

    @staticmethod
    def convert_online_or_offline_resolver(r: Union[OnlineResolver, OfflineResolver]) -> pb.Resolver:
        if r.output is None:
            raise ValueError("Resolver missing `output` attribute")

        outputs = ToProtoConverter.convert_resolver_outputs(r.output.features or [])
        schedule = None
        cron_filter = None
        if r.cron is not None:
            if isinstance(r.cron, Cron):
                duration = None
                crontab = None
                if isinstance(r.cron.schedule, str):
                    try:
                        duration_td = parse_chalk_duration(r.cron.schedule)
                    except ValueError:
                        crontab = r.cron.schedule
                    else:
                        duration = timedelta_to_proto_duration(duration_td)
                elif isinstance(r.cron.schedule, timedelta):
                    duration = timedelta_to_proto_duration(r.cron.schedule)
                else:
                    raise TypeError(f"Unknown cron schedule type: {type(r.cron.schedule).__name__}")

                cron_filter = ToProtoConverter.convert_cron_filter(r.cron) if r.cron.filter else None

                schedule = pb.Schedule(
                    filter=ToProtoConverter.create_function_reference(r.cron.filter)
                    if r.cron.filter is not None
                    else None,
                    sample=ToProtoConverter.create_function_reference(r.cron.sample) if r.cron.sample else None,
                    duration=duration,
                    crontab=crontab,
                )
            elif isinstance(r.cron, str):
                try:
                    duration_td = parse_chalk_duration(r.cron)
                except:
                    schedule = pb.Schedule(crontab=r.cron)
                else:
                    schedule = pb.Schedule(duration=timedelta_to_proto_duration(duration_td))
            elif isinstance(r.cron, timedelta):
                schedule = pb.Schedule(duration=timedelta_to_proto_duration(r.cron))
            else:
                raise TypeError(f"Unknown cron type: {type(r.cron).__name__}")

        if r.resource_hint is None:
            resource_hint = None
        elif r.resource_hint == "cpu":
            resource_hint = pb.RESOURCE_HINT_CPU
        elif r.resource_hint == "io":
            resource_hint = pb.RESOURCE_HINT_IO
        else:
            raise ValueError(f"Unsupported resource hint: {r.resource_hint}")

        return pb.Resolver(
            fqn=r.fqn,
            kind=(
                pb.ResolverKind.RESOLVER_KIND_ONLINE
                if isinstance(r, OnlineResolver)
                else pb.ResolverKind.RESOLVER_KIND_OFFLINE
            ),
            inputs=ToProtoConverter.convert_resolver_inputs(r.inputs, r.state, r.default_args),
            outputs=outputs,
            is_generator=inspect.isgeneratorfunction(r.fn) or inspect.isasyncgenfunction(r.fn),
            data_sources=[ToProtoConverter.create_database_source_reference(s) for s in (r.data_sources or [])],
            machine_type=r.machine_type,
            tags=r.tags,
            resource_hint=resource_hint,
            is_static=r.static,
            owner=r.owner,
            doc=r.doc,
            environments=r.environment,
            timeout_duration=timedelta_to_proto_duration(r.timeout) if r.timeout is not None else None,
            schedule=schedule,
            when=ToProtoConverter.convert_filter(r.when) if r.when else None,
            cron_filter=cron_filter,
            function=ToProtoConverter.create_function_reference(
                r.fn, r.function_definition, r.filename, source_line=r.source_line
            ),
            # TODO(CHA-4831): Include the underscore definition
            is_total=r.total,
        )

    @staticmethod
    def convert_stream_resolver_param(p: StreamResolverParam) -> pb.StreamResolverParam:
        if isinstance(p, StreamResolverParamMessage):
            try:
                maybe_type = ToProtoConverter.convert_rich_type_to_protobuf(p.typ)
            except:
                # TODO: Stream message types are often more expressive than we can
                #       currently serialize. But we don't want to block `chalk apply`
                #       until we absolutely must need the Arrow type to be serialized.
                maybe_type = None

            return pb.StreamResolverParam(
                message=pb.StreamResolverParamMessage(
                    name=p.name,
                    arrow_type=maybe_type,
                )
            )
        elif isinstance(p, StreamResolverParamMessageWindow):
            try:
                maybe_type = ToProtoConverter.convert_rich_type_to_protobuf(p.typ)
            except:
                # TODO: Stream message types are often more expressive than we can
                #       currently serialize. But we don't want to block `chalk apply`
                #       until we absolutely must need the Arrow type to be serialized.
                maybe_type = None
            return pb.StreamResolverParam(
                message_window=pb.StreamResolverParamMessageWindow(
                    name=p.name,
                    arrow_type=maybe_type,
                )
            )
        elif isinstance(p, StreamResolverParamKeyedState):
            converter = FeatureConverter(
                name="helper", is_nullable=False, rich_type=p.typ, rich_default=p.default_value
            )
            arrow_type = None
            if converter:
                try:
                    arrow_type = converter.convert_pa_dtype_to_proto_dtype(converter.pyarrow_dtype)
                except:
                    # TODO: Stream message types are often more expressive than we can
                    #       currently serialize. But we don't want to block `chalk apply`
                    #       until we absolutely must need the Arrow type to be serialized.
                    pass

            initial = None
            if converter:
                try:
                    initial = converter.from_rich_to_protobuf(p.default_value)
                except:
                    # TODO: Stream message types are often more expressive than we can
                    #       currently serialize. But we don't want to block `chalk apply`
                    #       until we absolutely must need the Arrow type to be serialized.
                    pass

            return pb.StreamResolverParam(state=pb.ResolverState(arrow_type=arrow_type, initial=initial))
        else:
            raise TypeError(f"Unknown param type: {type(p).__name__}")

    @classmethod
    def convert_parse_info(cls, info: ParseInfo) -> pb.ParseInfo:
        try:
            maybe_input_type = ToProtoConverter.convert_rich_type_to_protobuf(info.input_type)
        except:
            # TODO: Stream message types are often more expressive than we can
            #       currently serialize. But we don't want to block `chalk apply`
            #       until we absolutely must need the Arrow type to be serialized.
            maybe_input_type = None

        try:
            maybe_output_type = ToProtoConverter.convert_rich_type_to_protobuf(info.output_type)
        except:
            # TODO: Stream message types are often more expressive than we can
            #       currently serialize. But we don't want to block `chalk apply`
            #       until we absolutely must need the Arrow type to be serialized.
            maybe_output_type = None

        return pb.ParseInfo(
            parse_function_input_type=maybe_input_type,
            parse_function_output_type=maybe_output_type,
            parse_function=ToProtoConverter.create_function_reference(info.fn),
            is_parse_function_output_optional=info.output_is_optional,
        )

    @classmethod
    def convert_stream_resolver(cls, r: StreamResolver) -> pb.StreamResolver:
        mode: pb.WindowMode | None = None
        if r.mode:
            mode = cls._mode_to_proto.get(r.mode)
            if mode is None:
                raise ValueError(f"Unknown window mode: {r.mode}")

        return pb.StreamResolver(
            fqn=r.fqn,
            params=[ToProtoConverter.convert_stream_resolver_param(p) for p in r.signature.params],
            outputs=ToProtoConverter.convert_resolver_outputs(r.output.features)
            if r.output and r.output.features
            else [],
            explicit_schema=(ToProtoConverter.convert_rich_type_to_protobuf(r.message) if r.message else None),
            keys=(
                [
                    pb.StreamKey(key=k, feature=ToProtoConverter.create_feature_reference(ensure_feature(v)))
                    for k, v in r.keys.items()
                ]
                if r.keys is not None
                else None
            ),
            source=ToProtoConverter.create_stream_source_reference(r.source),
            parse_info=ToProtoConverter.convert_parse_info(r.parse) if r.parse else None,
            mode=mode,
            environments=r.environment or [],
            timeout_duration=timedelta_to_proto_duration(r.timeout) if r.timeout is not None else None,
            timestamp_attribute_name=r.timestamp,
            owner=r.owner,
            doc=r.doc,
            machine_type=r.machine_type,
            function=ToProtoConverter.create_function_reference(
                r.fn, r.function_definition, r.filename, source_line=r.source_line
            ),
        )

    @staticmethod
    def convert_sink_resolver(r: SinkResolver) -> pb.SinkResolver:
        stream_source = None
        database_source = None

        if r.integration:
            if isinstance(r.integration, BaseSQLSource):
                database_source = ToProtoConverter.create_database_source_reference(r.integration)
            elif isinstance(r.integration, StreamSource):
                stream_source = ToProtoConverter.create_stream_source_reference(r.integration)
            else:
                raise TypeError(f"Unsupported integration type: {type(r.integration).__name__}")

        return pb.SinkResolver(
            fqn=r.fqn,
            inputs=ToProtoConverter.convert_resolver_inputs(r.inputs, r.state, r.default_args),
            buffer_size=r.buffer_size if r.buffer_size is not None else None,
            debounce_duration=timedelta_to_proto_duration(r.debounce) if r.debounce is not None else None,
            max_delay_duration=timedelta_to_proto_duration(r.max_delay) if r.max_delay is not None else None,
            upsert=r.upsert,
            stream_source=stream_source,
            database_source=database_source,
            machine_type=r.machine_type,
            doc=r.doc,
            owner=r.owner,
            environments=r.environment or [],
            timeout_duration=timedelta_to_proto_duration(r.timeout) if r.timeout is not None else None,
            function=ToProtoConverter.create_function_reference(
                r.fn, r.function_definition, r.filename, source_line=r.source_line
            ),
        )

    @staticmethod
    def _convert_resolver(r: Resolver) -> Union[pb.Resolver, pb.StreamResolver, pb.SinkResolver]:
        if isinstance(r, (OnlineResolver, OfflineResolver)):
            return ToProtoConverter.convert_online_or_offline_resolver(r)
        elif isinstance(r, StreamResolver):
            return ToProtoConverter.convert_stream_resolver(r)
        elif isinstance(r, SinkResolver):
            return ToProtoConverter.convert_sink_resolver(r)
        else:
            raise TypeError(f"Unknown resolver type: {type(r).__name__}")

    @staticmethod
    def convert_resolver(r: Resolver) -> Union[pb.Resolver, pb.StreamResolver, pb.SinkResolver]:
        try:
            return ToProtoConverter._convert_resolver(r)
        except Exception as e:
            raise ValueError(f"Error converting resolver '{r.fqn}'") from e

    @staticmethod
    def convert_graph(
        features_registry: dict[str, type[Features]],
        resolver_registry: Collection[Resolver],
        sql_source_registry: Collection[BaseSQLSource],
        stream_source_registry: Collection[StreamSource],
        named_query_registry: dict[tuple[str, Optional[str]], NamedQuery],
    ) -> pb.Graph:
        feature_sets = []
        for feature_set in features_registry.values():
            features = []
            for f in feature_set.features:
                features.append(ToProtoConverter.convert_feature(f))

            feature_sets.append(
                pb.FeatureSet(
                    name=feature_set.namespace,
                    features=features,
                    is_singleton=feature_set.__chalk_is_singleton__,
                    max_staleness_duration=timedelta_to_proto_duration(feature_set.__chalk_max_staleness__),
                    tags=feature_set.__chalk_tags__,
                    owner=feature_set.__chalk_owner__,
                    doc=feature_set.__doc__,
                    etl_offline_to_online=feature_set.__chalk_etl_offline_to_online__,
                    class_path=paths.get_classpath_or_name(feature_set),
                )
            )

        resolvers: list[pb.Resolver] = []
        stream_resolvers: list[pb.StreamResolver] = []
        sink_resolvers: list[pb.SinkResolver] = []
        named_queries: list[pb.NamedQuery] = []

        for resolver in resolver_registry:
            converted = ToProtoConverter.convert_resolver(resolver)
            if isinstance(converted, pb.Resolver):
                resolvers.append(converted)
            elif isinstance(converted, pb.StreamResolver):
                stream_resolvers.append(converted)
            elif isinstance(converted, pb.SinkResolver):
                sink_resolvers.append(converted)
            else:
                raise TypeError(f"Unsupported resolver type: {converted}")
        for named_query in named_query_registry.values():
            named_queries.append(ToProtoConverter._convert_named_query(named_query))

        return pb.Graph(
            feature_sets=feature_sets,
            resolvers=resolvers,
            stream_resolvers=stream_resolvers,
            sink_resolvers=sink_resolvers,
            database_sources=[
                ToProtoConverter.convert_sql_source(s)
                for s in sql_source_registry
                if isinstance(s, ToProtoConverter._supported_db_source_types)
            ],
            stream_sources=[
                ToProtoConverter.convert_stream_source(s)
                for s in stream_source_registry
                if isinstance(s, ToProtoConverter._supported_stream_source_types)
            ],
            named_queries=named_queries,
        )
