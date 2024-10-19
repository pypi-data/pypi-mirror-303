from typing import Any, Callable, override, Self, Iterable, cast

import pyg3a.types.numbers as numbers
from pyg3a.errors import CTypeNotConcreteError

_maths_operators: tuple[str, ...] = (
    "add",
    "sub",
    "mul",
    "truediv",
    "floordiv",
    "mod",
    "pow",
    "lshift",
    "rshift",
    "and",
    "xor",
    "or",
)

_unary_maths_operators: tuple[str, ...] = ("neg", "pos", "abs", "invert")

_comparisons: tuple[str, ...] = (
    "le",
    "ge",
    "lt",
    "gt",
    "eq",
    "ne",
)

_container_operators: tuple[str, ...] = ("getitem", "delitem", "contains")

_mutable_container_operators: tuple[str, ...] = ("setitem",)


class classproperty[T](property):
    """
    Decorator for a Class-level property.
    No, I don't really know where it works.
    Credit to hottwaj on GitHub: https://github.com/hottwaj/classproperties
    """

    @override
    def __init__(self, func: Callable[[Any], T]) -> None:
        super().__init__(func)

    @override
    def __get__(self, owner_self: object, owner_cls: type | None = None) -> T:
        if not owner_cls:
            raise TypeError
        if self.fget:
            return cast(T, self.fget(owner_cls))
        raise TypeError(f"{owner_cls.__name__} has no property {self.fget.__name__}")


def _ctype_meta_factory() -> type[type]:
    """
    Helper function to create the CObjectMeta class.
    :returns: A metaclass for :py:class:`CObject` s named CObjectMeta
    """

    def any_op(operation: str) -> Callable[[type["CObject"]], type["CObject"]]:
        def op_impl(cls: type["CObject"], *args: type["CObject"], **kwargs: type["CObject"]) -> type["CObject"]:
            if operation in type.__dir__(cls):
                return cast(type["CObject"], getattr(cls, operation)(*args, **kwargs))
            return COpNotImplemented

        return op_impl

    def ternary_op(operation: str) -> Callable[[type["CObject"], type["CObject"], type["CObject"]], type["CObject"]]:
        def op_impl(cls: type["CObject"], other: type["CObject"], third: type["CObject"]) -> type["CObject"]:
            if operation in type.__dir__(cls):
                return cast(type["CObject"], getattr(cls, operation)(other, third))
            return COpNotImplemented

        return op_impl

    def binary_op(operation: str) -> Callable[[type["CObject"], type["CObject"]], type["CObject"]]:
        def op_impl(cls: type["CObject"], other: type["CObject"]) -> type["CObject"]:
            if operation in type.__dir__(cls):
                return cast(type["CObject"], getattr(cls, operation)(other))
            return COpNotImplemented

        return op_impl

    def unary_op(operation: str) -> Callable[[type["CObject"]], type["CObject"]]:
        def op_impl(cls: type["CObject"]) -> type["CObject"]:
            if operation in type.__dir__(cls):
                if callable(getattr(cls, operation)):
                    return cast(type["CObject"], getattr(cls, operation)())
                return cast(type["CObject"], getattr(cls, operation))
            return COpNotImplemented

        return op_impl

    def getattr_impl(cls: type["CObject"], attr: str) -> str:
        if "__getattr__" in type.__dir__(cls):
            return cast(str, getattr(cls, "__getattr__")(attr))
        raise AttributeError

    methods: dict[str, Callable[..., Any]] = {"__hash__": type.__hash__, "__getattr__": getattr_impl}

    for op_name in _maths_operators + _comparisons + _container_operators + ("subclasscheck",):
        methods[f"__{op_name}__"] = binary_op(f"__{op_name}__")

    for op_name in _unary_maths_operators + ("str", "bool"):
        methods[f"__{op_name}__"] = unary_op(f"__{op_name}__")

    for op_name in _mutable_container_operators:
        methods[f"__{op_name}__"] = ternary_op(f"__{op_name}__")

    for op_name in ("call",):
        methods[f"__{op_name}__"] = any_op(f"__{op_name}__")

    created_metaclass: type[type] = type("CObjectMeta", (type,), methods)
    return created_metaclass


CObjectMeta: type[type] = _ctype_meta_factory()


class CObject(metaclass=CObjectMeta):  # type: ignore[misc] # mypy complains about our metaclass
    """
    Base class for all C++ types.
    """

    @classproperty
    def c(cls) -> str | None:
        """
        Name of the class in C++.
        ``None`` if the class cannot be converted to a C++ type.
        """
        return None

    @classproperty
    def headers(cls) -> Iterable[str]:
        """
        Tuple of C++ headers to import on usage.
        """
        return tuple()

    @classmethod
    def __str__(cls) -> str:  # type: ignore[override]
        """
        String representation of the C++ type, as specified in :py:attr:`c`.
        """
        if cls.c:
            return cls.c
        raise CTypeNotConcreteError(f"{cls.__name__} cannot be converted to a C++ type.")

    @classmethod
    def __bool__(cls) -> bool:
        """
        Whether this class is concrete.
        """
        return True

    @classmethod
    def __eq__(cls, other: type[Self]) -> type["CObject"]:  # type: ignore[override]
        """
        What type this class returns when compared with equality.
        """
        return numbers.CBool

    @classmethod
    def __ne__(cls, other: type[Self]) -> type["CObject"]:  # type: ignore[override]
        """
        What type this class returns when compared with inequality.
        """
        return numbers.CBool

    @classmethod
    def __subclasscheck__(cls, subclass: type) -> bool:
        """
        Whether this type is a subclass of ``subclass``.
        """
        if type.__subclasscheck__(cls, subclass):
            return True

        if type.__subclasscheck__(CAny, subclass):
            return True

        return False


class COpNotImplemented(CObject):
    """
    Blank C++ type returned when an operation is not implemented on a class.
    """

    c = None

    @classmethod
    @override
    def __bool__(cls) -> bool:
        """
        Returns that this class is not concrete.
        """
        return False


def _cany_op_impl(_cls: type["CAny"], *_args: type["CObject"]) -> type["CAny"]:
    """
    Helper function to implement :py:class:`CAny`.
    All operations are acceptable and all return :py:class:`CAny`.
    """
    return CAny


CAny: type[CObject] = CObjectMeta(
    "CAny",
    (CObject,),
    {"c": "auto", "__subclasscheck__": classmethod(lambda cls, subclass: isinstance(subclass, CObjectMeta))}
    | {
        f"__{op}__": classmethod(_cany_op_impl)
        for op in _maths_operators
        + _comparisons
        + _container_operators
        + _mutable_container_operators
        + _unary_maths_operators
    },
)
