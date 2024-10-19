from .generics import GenericType
from .object import CObject, COpNotImplemented, CAny
from .numbers import CInt, CBool


class CSequence(GenericType):
    """
    Abstract class inherited by all sequence types.
    """

    def sequence_op(self: type[CObject], other: type[CObject]) -> type[CObject]:
        """
        Helper function for binary operations with another sequence.
        The least inherited type is returned.

        :param other: Other type in binary operation.
        :returns: The resultant type of this operation, or :py:class:`~pyg3a.types.object.COpNotImplemented` if the operation cannot be performed.
        """

        if not isinstance(other, CSequence):
            return COpNotImplemented

        if issubclass(other, self):
            return self

        if issubclass(self, other):
            return other

        return COpNotImplemented

    def sequence_access(self, other: type[CObject]) -> type[CObject]:
        """
        Helper function for operations that include access to items of this sequence.

        :param other: Type of index used to access a sequence element.
        :returns: The resultant type of this operation, or :py:class:`~pyg3a.types.object.COpNotImplemented` if the operation cannot be performed.
        """

        if issubclass(other, CInt):
            return CAny

        return COpNotImplemented

    def __add__(self, other: type[CObject]) -> type[CObject]:
        return self.sequence_op(other)

    def __getitem__(self, other: type[CObject]) -> type[CObject]:
        return self.sequence_access(other)

    def __contains__(self, other: type[CObject]) -> type[CObject]:
        if self.sequence_access(other):
            return CBool

        return COpNotImplemented


class CMutableSequence(CSequence):
    """
    Abstract class inherited by all mutable sequence types.
    Inherits from :py:class:`CSequence` and implements :py:meth:`__setitem__` and :py:meth:`__delitem__` .
    """

    def __setitem__(self, other: type[CObject]) -> type[CObject]:
        return self.sequence_access(other)

    def __delitem__(self, other: type[CObject]) -> type[CObject]:
        return self.sequence_access(other)
