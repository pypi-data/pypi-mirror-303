import abc
from types import EllipsisType
from typing import override

from .sequence import CSequence
from .generics import GenericType, GenericArg, GenericNotImplemented
from .numbers import CInt, CPointer
from .object import CObject, COpNotImplemented, CObjectMeta, CAny


class CTuple(CSequence, GenericType):
    """
    Tuples are an immutable sequence which can either have arguments specifying the exact types of the elements
    (see :py:class:`CSpecificTuple`) or an unspecified number of elements of type T (see :py:class:`CArbitraryLengthTuple`).
    """

    @classmethod
    @abc.abstractmethod
    def acceptable_args(cls, type_args: tuple[GenericArg, ...]) -> bool: ...

    @classmethod
    @override
    def name(cls, bases: tuple[GenericArg, ...]) -> str | None:
        return None

    @classmethod
    def struct(cls, struct_name: str) -> "CSpecificTuple":
        """
        Static helper method to create a tuple type instance from the given name. Particularly useful for structs.

        :param struct_name: The name of the struct.
        :returns: The :py:class:`CSpecificTuple` instance.
        """
        return cls.__class__(struct_name, (CSpecificTuple,), {"name": classmethod(lambda cls_, bases: struct_name)})

    @override
    def __class_getitem__(cls, *args: GenericArg) -> GenericType:
        """
        Specialised CTuple[X] to call :py:class:`CArbitraryLengthTuple`[X] or :py:class:`CSpecificTuple`[X] depending on specified X

        :param args: The type arguments.
        :returns: The :py:class:`CTuple` instance - a :py:class:`CArbitraryLengthTuple` if X is T, ...; otherwise,
        a :py:class:`CSpecificTuple`.
        """
        type_args: tuple[GenericArg, ...] = args[0] if isinstance(args[0], tuple) else args

        if CArbitraryLengthTuple.acceptable_args(type_args):
            return super(cls, CArbitraryLengthTuple).__class_getitem__(*args)

        if CSpecificTuple.acceptable_args(type_args):
            return super(cls, CSpecificTuple).__class_getitem__(*args)

        return GenericNotImplemented


class CArbitraryLengthTuple(CTuple):
    """
    A tuple type with an unspecified number of elements of type T.
    """

    args: tuple[type[CObject], EllipsisType]
    "Accepts one type object followed by an ellipsis as arguments."

    _base_classes: tuple[type[CObject]] = (CPointer,)
    "An arbitrary length tuple is a pointer."

    @classmethod
    @override
    def acceptable_args(cls, type_args: tuple[GenericArg, ...]) -> bool:
        return len(type_args) == 2 and type_args[1] is Ellipsis and isinstance(type_args[0], CObjectMeta)

    @override
    def sequence_access(self, other: type[CObject]) -> type[CObject]:
        if issubclass(other, CInt):
            return self.args[0]

        return COpNotImplemented

    @classmethod
    @override
    def name(cls, bases: tuple[GenericArg, ...]) -> str | None:
        """
        An arbitrary length tuple is a pointer of T.
        """

        return f"{bases[0]}*"

    @override
    def __subclasscheck__(self, subclass: type) -> bool:
        try:
            return super().__subclasscheck__(subclass)
        except NotImplementedError:
            # A[B, ...] is a subclass of tuple[X, ...] if X is a subclass of B
            if (
                issubclass(subclass.origin, CSpecificTuple) and all(issubclass(T, self.args[0]) for T in subclass.args)
            ) or (issubclass(subclass.origin, self.origin) and issubclass(subclass.args[0], self.args[0])):
                return True

        return False

    @override
    def __class_getitem__(cls, *args: GenericArg) -> GenericType:
        # Use the standard GenericType[] syntax
        return super(CTuple, cls).__class_getitem__(*args)


class CSpecificTuple(CArbitraryLengthTuple):
    """
    A tuple with an exact number of elements of different types, as used by structs.
    """

    args: tuple[type[CObject], ...]
    "Accepts one or more type objects as arguments."

    _base_classes: tuple[type[CObject]] = (CObject,)
    "Specific tuples are not pointers."

    @classmethod
    @override
    def acceptable_args(cls, type_args: tuple[GenericArg, ...]) -> bool:
        return all(isinstance(base, CObjectMeta) for base in type_args)

    @classmethod
    @override
    def name(cls, _bases: tuple[GenericArg, ...]) -> str | None:
        return None

    @override
    def sequence_access(self, other: type[CObject]) -> type[CObject]:
        if issubclass(other, CInt):
            # If everything in the tuple is the same, return that
            if self.args.count(self.args[0]) == len(self.args):
                return self.args[0]

            return CAny

        return COpNotImplemented
