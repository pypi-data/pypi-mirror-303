from __future__ import annotations

from typing import TYPE_CHECKING, Any

SUPPORTED_UNDERSCORE_OPS_BINARY = set("+ - * / // % ** < <= > >= == != & | ^ << >>".split())
SUPPORTED_UNDERSCORE_OPS_UNARY = set("- + ~".split())


class Underscore:
    """An unevaluated underscore expression.

    Examples
    --------
    >>> class X:
    ...     y: DataFrame[Y] = has_many(...)
    ...     s: int = _.y[_.z].sum()
    """

    def __getattr__(self, attr: str) -> "Underscore":
        if attr.startswith("__") or attr.startswith("_chalk__"):
            raise AttributeError(f"{self.__class__.__name__!r} {attr!r}")
        return UnderscoreAttr(self, attr)

    def __getitem__(self, key: Any) -> "Underscore":
        return UnderscoreItem(self, key)

    def __call__(self, *args: Any, **kwargs: Any) -> "Underscore":
        return UnderscoreCall(self, *args, **kwargs)

    def __add__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("+", self, other)

    def __radd__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("+", other, self)

    def __sub__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("-", self, other)

    def __rsub__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("-", other, self)

    def __mul__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("*", self, other)

    def __rmul__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("*", other, self)

    def __truediv__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("/", self, other)

    def __rtruediv__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("/", other, self)

    def __floordiv__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("//", self, other)

    def __rfloordiv__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("//", other, self)

    def __mod__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("%", self, other)

    def __rmod__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("%", other, self)

    def __pow__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("**", self, other)

    def __rpow__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("**", other, self)

    def __lt__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("<", self, other)

    def __le__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("<=", self, other)

    def __gt__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp(">", self, other)

    def __ge__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp(">=", self, other)

    def __eq__(self, other: Any) -> "Underscore":  # pyright: ignore[reportIncompatibleMethodOverride]
        return UnderscoreBinaryOp("==", self, other)

    def __ne__(self, other: Any) -> "Underscore":  # pyright: ignore[reportIncompatibleMethodOverride]
        return UnderscoreBinaryOp("!=", self, other)

    def __and__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("&", self, other)

    def __rand__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("&", other, self)

    def __or__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("|", self, other)

    def __ror__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("|", other, self)

    def __xor__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("^", self, other)

    def __rxor__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("^", other, self)

    def __lshift__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("<<", self, other)

    def __rlshift__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp("<<", other, self)

    def __rshift__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp(">>", self, other)

    def __rrshift__(self, other: Any) -> "Underscore":
        return UnderscoreBinaryOp(">>", other, self)

    def __neg__(self) -> "Underscore":
        return UnderscoreUnaryOp("-", self)

    def __pos__(self) -> "Underscore":
        return UnderscoreUnaryOp("+", self)

    def __invert__(self) -> "Underscore":
        return UnderscoreUnaryOp("~", self)

    def __hash__(self):
        return hash(repr(self))

    if not TYPE_CHECKING:

        def if_then_else(self: Any, *args: Any, **kwargs: Any):
            """
            This function is used to provide a better error message for when it is accidentally
            called on a non-root underscore expression.

            This overload should not actually be called - call the method directly on `_` instead.
            """
            raise ValueError(
                f"You cannot call .if_then_else on expression '{repr(self)}'; call it on the root _ instead, as in '_.if_then_else(condition, if_true, if_false)'"
            )


class UnderscoreRoot(Underscore):
    # _
    def __repr__(self):
        return "_"

    @property
    def chalk_window(self):
        """Refers to the specific window being evaluated in the context of
        defining an underscore expression.

        Examples
        --------
        >>> from datetime import timedelta
        >>> from chalk.features import features
        >>> from chalk import _, Windowed, DataFrame, windowed
        >>> @features
        ... class Transaction:
        ...     id: int
        ...     user_id: "User.id"
        ...     amount: int
        >>> @features
        ... class User:
        ...     id: int
        ...     transactions: DataFrame[Transaction]
        ...     sum_amounts: Windowed[int] = windowed(
        ...         "30d", "90d",
        ...         expression=_.transactions[
        ...             _.amount,
        ...             _.ts > _.chalk_window
        ...         ].sum(),
        ...     )
        """
        return UnderscoreAttr(self, "chalk_window")

    @property
    def chalk_now(self):
        """Refers to the specific window being evaluated in the context of
        defining an underscore expression.

        Examples
        --------
        >>> from datetime import timedelta
        >>> from chalk.features import features
        >>> from chalk import _, Windowed, DataFrame, windowed
        >>> @features
        ... class Transaction:
        ...     id: int
        ...     user_id: "User.id"
        ...     amount: int
        >>> @features
        ... class User:
        ...     id: int
        ...     transactions: DataFrame[Transaction]
        ...     sum_old_amounts: int = _.transactions[
        ...         _.amount,
        ...         _.ts < _.chalk_now - timedelta(days=30),
        ...     ].sum()
        """
        return UnderscoreAttr(self, "chalk_now")

    def if_then_else(
        self,
        condition: Underscore,
        if_true: Any,
        if_false: Any,
    ) -> Underscore:
        """
        Create a conditional expression, roughly equivalent to

        ```
        if condition:
            return if_true
        else:
            return if_false
        ```

        Unlike a Python if/else, all three inputs `(condition, if_true, if_false)` are evaluated
        in parallel for all rows, and then the correct side is selected based on the result of
        the condition expression.

        Examples
        --------
        >>> from chalk import _
        >>> from chalk.features import features
        >>> @features
        ... class Transaction:
        ...    id: int
        ...    amount: int
        ...    risk_score: bool = _.if_then_else(
        ...        _.amount > 10_000,
        ...        _.amount * 0.1,
        ...        _.amount * 0.05,
        ...    )
        """
        return UnderscoreIfThenElse(
            condition=condition,
            if_true=if_true,
            if_false=if_false,
        )


class DoubleUnderscore(Underscore):
    # __
    def __repr__(self):
        return "__"


class UnderscoreAttr(Underscore):
    # _.a
    def __init__(self, parent: Underscore, attr: str):
        super().__init__()
        self._chalk__parent = parent
        self._chalk__attr = attr

    def __repr__(self):
        return f"{self._chalk__parent}.{self._chalk__attr}"


class UnderscoreItem(Underscore):
    # _[k]
    def __init__(self, parent: Underscore, key: Any):
        super().__init__()
        self._chalk__parent = parent
        self._chalk__key = key

    def __repr__(self):
        if isinstance(self._chalk__key, tuple):
            keys = ", ".join(f"{key}" for key in self._chalk__key)
        else:
            keys = f"{self._chalk__key}"

        return f"{self._chalk__parent}[{keys}]"


class UnderscoreCall(Underscore):
    # _(args, kwargs)
    def __init__(self, parent: Underscore, *args: Any, **kwargs: Any):
        super().__init__()
        self._chalk__parent = parent
        self._chalk__args = args
        self._chalk__kwargs = kwargs

    def __repr__(self):
        args: list[str] = []
        COMMA = ", "
        for arg in self._chalk__args:
            args.append(f"{arg}")
        for key, arg in self._chalk__kwargs.items():
            args.append(f"{key}={arg}")
        return f"{self._chalk__parent}({COMMA.join(args)})"


class UnderscoreBinaryOp(Underscore):
    # _.a + _.b
    # _ and _.c
    def __init__(self, op: str, left: Any, right: Any):
        super().__init__()
        self._chalk__op = op
        self._chalk__left = left
        self._chalk__right = right

    def __repr__(self):
        return f"({self._chalk__left} {self._chalk__op} {self._chalk__right})"


class UnderscoreUnaryOp(Underscore):
    #!_.a
    def __init__(self, op: str, operand: Any):
        super().__init__()
        self._chalk__op = op
        self._chalk__operand = operand

    def __repr__(self):
        return f"{self._chalk__op}{self._chalk__operand}"


class UnderscoreIfThenElse(Underscore):
    # _.if_then_else(...)
    def __init__(
        self,
        condition: Underscore,
        if_true: Any,
        if_false: Any,
    ):
        super().__init__()
        if not isinstance(condition, Underscore):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise ValueError(
                f"The underscore expression .if_then_else() must be given an underscore expression as a condition, but was given '{repr(condition)}'"
            )
        self._chalk__condition = condition
        self._chalk__if_true = if_true
        self._chalk__if_false = if_false

    def __repr__(self):
        return f"_.if_then_else({self._chalk__condition}, {self._chalk__if_true}, {self._chalk__if_false})"


class UnderscoreFunction(Underscore):
    __name__ = "function"

    def __init__(self, name: str, *vals: Any):
        super().__init__()
        self._chalk__vals = vals
        self._chalk__function_name = name

    def __repr__(self):
        return f"chalk.functions.{self._chalk__function_name}{self._chalk__vals}"


class UnderscoreMD5(Underscore):
    __name__ = "md5"
    __qualname__ = "chalk.functions.md5"

    def __init__(self, value: Underscore):
        super().__init__()
        self._chalk__value = value

    def __repr__(self):
        return f"chalk.functions.md5({self._chalk__value})"


class UnderscoreCoalesce(Underscore):
    __name__ = "coalesce"
    __qualname__ = "chalk.functions.coalesce"

    def __init__(self, *vals: Any):
        super().__init__()
        self._chalk__vals = vals

    def __repr__(self) -> str:
        return f"chalk.functions.coalesce({self._chalk__vals})"


class UnderscoreBytesToString(Underscore):
    __name__ = "bytes_to_string"
    __qualname__ = "chalk.functions.bytes_to_string"

    def __init__(self, value: Underscore, encoding: str):
        super().__init__()
        self._chalk__value = value
        self._chalk__encoding = encoding

    def __repr__(self):
        return f"chalk.functions.bytes_to_string({self._chalk__value}, {self._chalk__encoding})"


class UnderscoreStringToBytes(Underscore):
    __name__ = "string_to_bytes"
    __qualname__ = "chalk.functions.string_to_bytes"

    def __init__(self, value: Underscore, encoding: str):
        super().__init__()
        self._chalk__value = value
        self._chalk__encoding = encoding

    def __repr__(self):
        return f"chalk.functions.string_to_bytes({self._chalk__value}, {self._chalk__encoding})"


class UnderscoreGetJSONValue(Underscore):
    __name__ = "json_value"
    __qualname__ = "chalk.functions.json_value"

    def __init__(self, value: Underscore, path: str | Underscore):
        super().__init__()
        self._chalk__value = value
        self._chalk__path = path

    def __repr__(self):
        return f"chalk.functions.json_value({self._chalk__value}, {self._chalk__path})"


class UnderscoreGunzip(Underscore):
    __name__ = "gunzip"
    __qualname__ = "chalk.functions.gunzip"

    def __init__(self, value: Underscore):
        super().__init__()
        self._chalk__value = value

    def __repr__(self):
        return f"chalk.functions.gunzip({self._chalk__value})"


class UnderscoreCosineSimilarity(Underscore):
    __name__ = "cosine_similarity"
    __qualname__ = "chalk.functions.cosine_similarity"

    def __init__(self, a: Underscore, b: Underscore):
        super().__init__()
        self._chalk__a = a
        self._chalk__b = b

    def __repr__(self):
        return f"chalk.functions.cosine_similarity({self._chalk__a}, {self._chalk__b})"


class UnderscoreTotalSeconds(Underscore):
    __name__ = "total_seconds"
    __qualname__ = "chalk.functions.total_seconds"

    def __init__(self, delta: Underscore):
        super().__init__()
        self._chalk__delta = delta

    def __repr__(self):
        return f"chalk.functions.total_seconds({self._chalk__delta})"


_ = underscore = UnderscoreRoot()
__ = DoubleUnderscore()


# NEED `__all__` because `_` is private and can't be auto-imported by i.e. IntelliJ.
__all__ = (
    "SUPPORTED_UNDERSCORE_OPS_BINARY",
    "SUPPORTED_UNDERSCORE_OPS_UNARY",
    "Underscore",
    "UnderscoreAttr",
    "UnderscoreBinaryOp",
    "UnderscoreBytesToString",
    "UnderscoreCall",
    "UnderscoreCoalesce",
    "UnderscoreCosineSimilarity",
    "UnderscoreFunction",
    "UnderscoreGetJSONValue",
    "UnderscoreGunzip",
    "UnderscoreItem",
    "UnderscoreMD5",
    "UnderscoreRoot",
    "UnderscoreStringToBytes",
    "UnderscoreTotalSeconds",
    "UnderscoreUnaryOp",
    "_",
    "__",
    "underscore",
)
