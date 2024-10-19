from typing import override

from .object import CObject, COpNotImplemented


class Number(CObject):
    @classmethod
    def numeric_op(cls, other: type[CObject]) -> type[CObject]:
        """
        Helper class for binary numerical operations.
        - Non-number classes cannot be operated on numerically.
        - Classes that are not subtypes of each other cannot be operated on.
        - The least derived class is returned.

        :param other: The type of the other operand.
        :return: The type of the result.
        """
        if not issubclass(other, Number):
            return COpNotImplemented

        if issubclass(other, cls):
            return cls

        if issubclass(cls, other):
            return other

        return COpNotImplemented

    @classmethod
    def comparison_op(cls, other: type[CObject]) -> type[CObject]:
        """
        Helper class for numerical comparison operations.
        - Non-number classes cannot be operated on numerically.
        - All numbers can be compared against all other numbers.

        :param other: The type of the other operand.
        :return: The type of the result.
        """
        if issubclass(other, Number):
            return CBool

        return COpNotImplemented

    @classmethod
    def __add__(cls, other: type[CObject]) -> type[CObject]:
        return cls.numeric_op(other)

    @classmethod
    def __sub__(cls, other: type[CObject]) -> type[CObject]:
        return cls.numeric_op(other)

    @classmethod
    def __mul__(cls, other: type[CObject]) -> type[CObject]:
        return cls.numeric_op(other)

    @classmethod
    def __truediv__(cls, other: type[CObject]) -> type[CObject]:
        return cls.numeric_op(other)

    @classmethod
    def __mod__(cls, other: type[CObject]) -> type[CObject]:
        return cls.numeric_op(other)

    @classmethod
    def __pow__(cls, other: type[CObject]) -> type[CObject]:
        return cls.numeric_op(other)

    @classmethod
    def __eq__(cls, other: type[CObject]) -> type[CObject]:
        return cls.comparison_op(other)

    @classmethod
    def __ne__(cls, other: type[CObject]) -> type[CObject]:
        return cls.comparison_op(other)

    @classmethod
    def __gt__(cls, other: type[CObject]) -> type[CObject]:
        return cls.comparison_op(other)

    @classmethod
    def __lt__(cls, other: type[CObject]) -> type[CObject]:
        return cls.comparison_op(other)

    @classmethod
    def __ge__(cls, other: type[CObject]) -> type[CObject]:
        return cls.comparison_op(other)

    @classmethod
    def __le__(cls, other: type[CObject]) -> type[CObject]:
        return cls.comparison_op(other)

    @classmethod
    def __neg__(cls) -> type["Number"]:
        return cls

    @classmethod
    def __pos__(cls) -> type["Number"]:
        return cls

    @classmethod
    def __abs__(cls) -> type["Number"]:
        return cls


class CComplex(Number):
    """
    Type representing complex numbers, unimplemented in C++.
    """

    c = ""

    @classmethod
    def __abs__(cls) -> type["CFloat"]:
        """
        The absolute value of a complex number is a :py:class:`CFloat`.
        """
        return CFloat


class CFloat(CComplex):
    """
    Type representing floating-points.
    The Python ``float`` type is very high-precision, so a ``double`` is used in C++.
    """

    c = "double"

    @classmethod
    def __floordiv__(cls, other: type[CObject]) -> type[CObject]:
        """
        Floordiv only exists on :py:class:`CFloat` but not :py:class:`CComplex`.
        """
        return cls.numeric_op(other)


class CInt(CFloat):
    """
    Type representing ints in C++ - unsure if ``int`` has enough range.
    """

    c = "int"

    @classmethod
    def binary_op(cls, other: type[CObject]) -> type[CObject]:
        """
        Helper class for binary operations (e.g. binary and/not/lshift).
        - Any subtype of :py:class:`CInt` works.
        """
        if issubclass(other, CInt):
            return cls

        return COpNotImplemented

    @classmethod
    @override
    def __truediv__(cls, other: type[CObject]) -> type[CObject]:
        """
        Truediv returns a float for two integers.
        Otherwise, use :py:meth:`numeric_op`.
        """
        if issubclass(other, CInt):
            return CFloat

        return cls.numeric_op(other)

    @classmethod
    def __lshift__(cls, other: type[CObject]) -> type[CObject]:
        return cls.binary_op(other)

    @classmethod
    def __rshift__(cls, other: type[CObject]) -> type[CObject]:
        return cls.binary_op(other)

    @classmethod
    def __and__(cls, other: type[CObject]) -> type[CObject]:
        return cls.binary_op(other)

    @classmethod
    def __xor__(cls, other: type[CObject]) -> type[CObject]:
        return cls.binary_op(other)

    @classmethod
    def __or__(cls, other: type[CObject]) -> type[CObject]:
        return cls.binary_op(other)

    # Explicitly ints for inherited bool class
    @classmethod
    def __invert__(cls) -> type["CInt"]:
        """
        Both :py:class:`CInt` and :py:class:`CBool` are inverted as a :py:class:`CInt`.
        """
        return CInt

    @classmethod
    def __abs__(cls) -> type["CInt"]:
        """
        Both :py:class:`CInt` and :py:class:`CBool` are absolute valued as a :py:class:`CInt`.
        """
        return CInt


class CPointer(CInt):
    """
    Underived base class for pointer types - pointers are just fancy ints.
    Allows automatic freeing of deleted/overriden pointers.
    """

    c = None


class CBool(CInt):
    """
    Type representing booleans in C++
    """

    c = "bool"

    @classmethod
    def numeric_op(cls, other: type[CObject]) -> type[CObject]:
        """
        Numeric operations with a :py:class:`CBool` return a :py:class:`CInt` if it is the least derived class.
        """
        if not issubclass(other, Number):
            return COpNotImplemented

        if issubclass(other, cls):
            return CInt

        if issubclass(cls, other):
            return other

        return COpNotImplemented

    @classmethod
    def __neg__(cls) -> type[CInt]:
        return CInt

    @classmethod
    def __pos__(cls) -> type[CInt]:
        return CInt

    @classmethod
    def __abs__(cls) -> type[CInt]:
        return CInt
