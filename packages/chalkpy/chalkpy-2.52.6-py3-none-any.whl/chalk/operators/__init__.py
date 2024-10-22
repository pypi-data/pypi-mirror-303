from __future__ import annotations

from typing import Mapping, Protocol, Sequence


class StaticOperator(Protocol):
    """Base class for all Static Operators.

    Instances of this class are provided as resolver inputs for static resolvers, and an instance of this operator should be returned for static resolvers.

    For resolvers that do not take inputs, use a factory function, such as ``scan_parquet``, to create a root operator.
    """

    column_names: tuple[str, ...]
    """The column names that are returned by this operator"""

    def rename_columns(self, names: Sequence[str] | Mapping[str, str]) -> StaticOperator:
        """Rename the columns.

        Parameters
        ----------
        names
            The new column names. This can either be a sequence of names, or a mapping of the old name to the new name.
            If a sequence, the length must match the number of existing columns, and columns will be renamed in-order.
            If a mapping, only the columns in the mapping will be renamed, and all other columns will be passed through
            as-is.

        Returns
        -------
        A static operator, which can be composed with other static operators.
        """

        from chalk.operators._rename import RenameOperator

        return RenameOperator(self, names)


def scan_parquet(files: str | Sequence[str], columns: Sequence[str]) -> StaticOperator:
    """The Parquet Scan operator scans a filesystem or cloud bucket for data encoded in parquet files.


    Parameters
    ----------
    files
        A glob pattern, URI, or sequence of glob patterns or URIs for the parquet files to ingest. Each URI should be of the form
        ``protocol://bucket/path/to/files/``, where protocol can be ``gs`` for Google Cloud Storage, ``s3`` for Amazon S3, or `local`` for a
        local filepath. Absolute paths (beginning with '/') are treated as local files.
    columns
        A list of columns to select from the parquet files.
    """
    from chalk.operators._parquet_scan import ParquetScanOperator

    return ParquetScanOperator(files, columns)
