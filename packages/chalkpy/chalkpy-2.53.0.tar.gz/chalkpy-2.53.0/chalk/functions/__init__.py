from __future__ import annotations

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

########################################################################################################################
# String Functions                                                                                                     #
########################################################################################################################


def like(expr: Underscore | Any, pattern: str):
    """
    Evaluates if the string matches the pattern.

    Patterns can contain regular characters as well as wildcards.
    Wildcard characters can be escaped using the single character
    specified for the escape parameter. Matching is case-sensitive.

    Note: The wildcard `%` represents 0, 1 or multiple characters
    and the wildcard `_` represents exactly one character.

    For example, the pattern `John%` will match any string that starts
    with `John`, such as `John`, `JohnDoe`, `JohnSmith`, etc.

    The pattern `John_` will match any string that starts with `John`
    and is followed by exactly one character, such as `JohnD`, `JohnS`, etc.
    but not `John`, `JohnDoe`, `JohnSmith`, etc.

    Parameters
    ----------
    expr
        The string to check against the pattern.
    pattern
        The pattern to check the string against.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class User:
    ...    id: Primary[str]
    ...    name: str
    ...    is_john: bool = F.like(_.name, "John%")
    """
    return UnderscoreFunction("like", expr, pattern)


def regexp_like(expr: Underscore | Any, pattern: str):
    """
    Evaluates the regular expression pattern and determines if it is contained within string.

    This function is similar to the `like` function, except that the pattern only needs to be
    contained within string, rather than needing to match all the string.
    In other words, this performs a contains operation rather than a match operation.
    You can match the entire string by anchoring the pattern using `^` and `$`.

    Parameters
    ----------
    expr
        The string to check against the pattern.
    pattern
        The regular expression pattern to check the string against.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class User:
    ...    id: Primary[str]
    ...    name: str
    ...    is_john: bool = F.regexp_like(_.name, "^John.*$")
    """
    return UnderscoreFunction("regexp_like", expr, pattern)


def trim(expr: Underscore | Any):
    """
    Remove leading and trailing whitespace from a string.

    Parameters
    ----------
    expr
        The string to trim.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class User:
    ...    id: Primary[str]
    ...    name: str
    ...    trimmed_name: str = F.trim(_.name)
    """
    return UnderscoreFunction("trim", expr)


def starts_with(expr: Underscore | Any, prefix: Underscore | Any):
    """
    Evaluates if the string starts with the specified prefix.

    Parameters
    ----------
    expr
        The string to check against the prefix.
    prefix
        The prefix or feature to check if the string starts with.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    category: str
    ...    is_food: bool = F.starts_with(_.name, "Food")
    """
    return UnderscoreFunction("starts_with", expr, prefix)


def ends_with(expr: Underscore | Any, suffix: Underscore | Any):
    """
    Evaluates if the string ends with the specified suffix.

    Parameters
    ----------
    expr
        The string to check against the suffix.
    suffix
        The suffix or feature to check if the string ends with.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    category: str
    ...    is_food: bool = F.ends_with(_.name, "Food")
    """
    return UnderscoreFunction("ends_with", expr, suffix)


def reverse(expr: Underscore | Any):
    """
    Reverse the order of a string.

    Parameters
    ----------
    expr
        The string to reverse.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class MyFeatures:
    ...    id: Primary[str]
    ...    name: str
    ...    reversed_name: str = F.reverse(_.name)
    """
    return UnderscoreFunction("reverse", expr)


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


########################################################################################################################
# Misc                                                                                                                 #
########################################################################################################################


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


########################################################################################################################
# Mathematical Functions                                                                                               #
########################################################################################################################


def power(a: Underscore | Any, b: Underscore | Any):
    """
    Raise a to the power of b. Alias for `a ** b`.

    Parameters
    ----------
    a
        The base.
    b
        The exponent.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Merchant:
    ...    id: Primary[str]
    ...    amount_std: float
    ...    amount_var: float = F.power(_.amount_std, 2)
    """
    return UnderscoreFunction("power", a, b)


def sin(expr: Underscore | Any):
    """
    Compute the sine of an angle in radians.

    Parameters
    ----------
    expr
        The angle in radians.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Triangle:
    ...    id: Primary[str]
    ...    angle: float
    ...    sin_angle: float = F.sin(_.angle)
    """
    return UnderscoreFunction("sin", expr)


def cos(expr: Underscore | Any):
    """
    Compute the cosine of an angle in radians.

    Parameters
    ----------
    expr
        The angle in radians.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Triangle:
    ...    id: Primary[str]
    ...    angle: float
    ...    cos_angle: float = F.cos(_.angle)
    """
    return UnderscoreFunction("cos", expr)


def ln(expr: Underscore | Any):
    """
    Compute the natural logarithm of a number.

    Parameters
    ----------
    expr
        The number to compute the natural logarithm of.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Triangle:
    ...    id: Primary[str]
    ...    hypotenuse: float
    ...    log_hypotenuse: float = F.ln(_.hypotenuse)
    """
    return UnderscoreFunction("ln", expr)


def exp(expr: Underscore | Any):
    """
    Returns Euler’s number raised to the power of x.

    Parameters
    ----------
    expr
        The exponent to raise Euler's number to.

    Examples
    --------
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Triangle:
    ...    id: Primary[str]
    ...    x: float
    ...    e_to_x: float = F.exp(_.x)
    """
    return UnderscoreFunction("exp", expr)


########################################################################################################################
# Date and Time Functions                                                                                              #
########################################################################################################################


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


def unix_seconds(expr: Underscore | Any):
    """
    Extract the number of seconds since the Unix epoch.
    Returned as a float.

    Parameters
    ----------
    expr
        The datetime to extract the number of seconds since the Unix epoch from.

    Examples
    --------
    >>> from datetime import datetime
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: datetime
    ...    unix_seconds: float = F.unix_seconds(_.date)
    """
    return UnderscoreFunction("to_unixtime", expr)


def unix_milliseconds(expr: Underscore | Any):
    """
    Extract the number of milliseconds since the Unix epoch.
    Returned as a float.

    Parameters
    ----------
    expr
        The datetime to extract the number of milliseconds since the Unix epoch from.

    Examples
    --------
    >>> from datetime import datetime
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: datetime
    ...    unix_milliseconds: float = F.unix_milliseconds(_.date)
    """
    return UnderscoreFunction("to_unixtime", expr) * 1000.0


def day_of_month(expr: Underscore | Any):
    """
    Extract the day of the month from a date.

    The supported types for x are date and datetime.

    Parameters
    ----------
    expr
        The date to extract the day of the month from.

    Examples
    --------
    >>> from datetime import date
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction
    ...    id: Primary[str]
    ...    date: date
    ...    day: int = F.day_of_month(_.date)
    """
    return UnderscoreFunction("day_of_month", expr)


def day_of_week(expr: Underscore | Any):
    """
    Returns the ISO day of the week from x. The value ranges from 1 (Monday) to 7 (Sunday).

    Parameters
    ----------
    expr
        The date to extract the day of the week from.

    Examples
    --------
    >>> from datetime import date
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction
    ...    id: Primary[str]
    ...    date: date
    ...    day: int = F.day_of_week(_.date)
    """
    return UnderscoreFunction("day_of_week", expr)


def day_of_year(expr: Underscore | Any):
    """
    Extract the day of the year from a date.

    The value ranges from 1 to 366.

    Parameters
    ----------
    expr
        The date to extract the day of the year from.

    Examples
    --------
    >>> from datetime import date
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: date
    ...    day: int = F.day_of_year(_.date)
    """
    return UnderscoreFunction("day_of_year", expr)


def month_of_year(expr: Underscore | Any):
    """
    Extract the month of the year from a date.

    The value ranges from 1 to 12.

    Parameters
    ----------
    expr
        The date to extract the month of the year from.

    Examples
    --------
    >>> from datetime import date
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: date
    ...    month: int = F.month_of_year(_.date)
    """
    return UnderscoreFunction("month", expr)


def week_of_year(expr: Underscore | Any):
    """
    Extract the week of the year from a date.

    The value ranges from 1 to 53.

    Parameters
    ----------
    expr
        The date to extract the week of the year from.

    Examples
    --------
    >>> from datetime import date
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: date
    ...    week: int = F.week_of_year(_.date)
    """
    return UnderscoreFunction("week_of_year", expr)


def hour_of_day(expr: Underscore | Any):
    """
    Extract the hour of the day from a datetime.

    The value ranges from 0 to 23.

    Parameters
    ----------
    expr
        The datetime to extract the hour of the day from.

    Examples
    --------
    >>> from datetime import datetime
    >>> import chalk.functions as F
    >>> from chalk.features import _, features, Primary
    >>> @features
    ... class Transaction:
    ...    id: Primary[str]
    ...    date: datetime
    ...    hour: int = F.hour_of_day(_.date)
    """
    return UnderscoreFunction("hour_of_day", expr)


__all__ = (
    "bytes_to_string",
    "coalesce",
    "cos",
    "cosine_similarity",
    "day_of_month",
    "day_of_week",
    "day_of_year",
    "exp",
    "gunzip",
    "hour_of_day",
    "json_value",
    "ln",
    "md5",
    "month_of_year",
    "power",
    "reverse",
    "sin",
    "string_to_bytes",
    "total_seconds",
    "unix_milliseconds",
    "unix_seconds",
    "week_of_year",
)
