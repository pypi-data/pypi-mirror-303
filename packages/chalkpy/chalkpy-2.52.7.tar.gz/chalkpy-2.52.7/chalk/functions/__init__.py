from typing import Any, Literal, Union

from chalk.features.underscore import (
    Underscore,
    UnderscoreBytesToString,
    UnderscoreCoalesce,
    UnderscoreCosineSimilarity,
    UnderscoreFunction,
    UnderscoreGetJSONValue,
    UnderscoreGunzip,
    UnderscoreMD5,
    UnderscoreStringToBytes,
    UnderscoreTotalSeconds,
)


def __getattr__(name: str):
    return lambda *args: UnderscoreFunction(name, *args)


def string_to_bytes(expr: Any, encoding: Literal["utf-8", "hex", "base64"]):
    """
    Convert a string to bytes using the specified encoding.

    Parameters
    ----------
    expr
        An underscore expression for a feature to a
        string feature that should be converted to bytes.
    encoding
        The encoding to use when converting the string to bytes.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    name: str
    ...    hashed_name: bytes = F.string_to_bytes(_.name, encoding="utf-8")
    """
    return UnderscoreStringToBytes(expr, encoding)


def bytes_to_string(expr: Any, encoding: Literal["utf-8", "hex", "base64"]):
    """
    Convert bytes to a string using the specified encoding.

    Parameters
    ----------
    expr
        A bytes feature to convert to a string.
    encoding
        The encoding to use when converting the bytes to a string.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    name: str
    ...    hashed_name: bytes
    ...    decoded_name: str = F.bytes_to_string(_.hashed_name, encoding="utf-8")
    """
    return UnderscoreBytesToString(expr, encoding)


def md5(expr: Any):
    """
    Compute the MD5 hash of some bytes.

    Parameters
    ----------
    expr
        A bytes feature to hash.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    bytes_feature: bytes
    ...    md5_bytes: bytes = F.md5(_.bytes_feature)
    """
    return UnderscoreMD5(expr)


def coalesce(*vals: Any):
    """
    Return the first non-null entry

    Parameters
    ----------
    vals
        Expressions to coalesce. They can be a combination of underscores and literals,
        though types must be compatible (ie do not coalesce int and string).

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    a: int | None
    ...    b: int | None
    ...    c: int = F.coalesce(_.a, _.b, 7)
    """
    return UnderscoreCoalesce(*vals)


def json_value(expr: Underscore, path: Union[str, Underscore]):
    """
    Extract a scalar from a JSON feature using a JSONPath expression. The value of the referenced path must be a JSON
    scalar (boolean, number, string).

    Parameters
    ----------
    expr
        The JSON feature to query.
    path
        The JSONPath-like expression to extract the scalar from the JSON feature.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk import JSON
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    raw: JSON
    ...    foo_value: str = F.json_value(_.raw, "$.foo.bar")
    """

    return UnderscoreGetJSONValue(expr, path)


def gunzip(expr: Underscore):
    """
    Decompress a GZIP-compressed bytes feature.

    Parameters
    ----------
    expr
        The GZIP-compressed bytes feature to decompress.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    compressed_data: bytes
    ...    decompressed_data: bytes = F.gunzip(_.compressed_data)
    """
    return UnderscoreGunzip(expr)


def cosine_similarity(a: Underscore, b: Underscore):
    """
    Compute the cosine similarity between two vectors.

    Parameters
    ----------
    a
        The first vector.
    b
        The second vector.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class User:
    ...    id: Primary[str]
    ...    embedding: Vector[1536]
    >>> @features
    ... class Merchant:
    ...    id: Primary[str]
    ...    embedding: Vector[1536]
    >>> @features
    ... class UserMerchant:
    ...    id: Primary[str]
    ...    user_id: User.id
    ...    user: User
    ...    merchant_id: Merchant.id
    ...    merchant: Merchant
    ...    similarity: float = F.cosine_similarity(_.user.embedding, _.merchant.embedding)
    """
    return UnderscoreCosineSimilarity(a, b)


def total_seconds(delta: Underscore) -> Underscore:
    """
    Compute the total number of seconds covered in a duration.

    Parameters
    ----------
    delta
        The duration to convert to seconds.

    Examples
    --------
    >>> from datetime import date
    >>> from chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    signup: date
    ...    last_login: date
    ...    signup_to_last_login_days: float = F.total_seconds(_.las_login - _.signup) / (60 * 60 * 24)
    """
    return UnderscoreTotalSeconds(delta)


__all__ = (
    "bytes_to_string",
    "coalesce",
    "gunzip",
    "md5",
    "json_value",
    "string_to_bytes",
    "cosine_similarity",
    "total_seconds",
)
