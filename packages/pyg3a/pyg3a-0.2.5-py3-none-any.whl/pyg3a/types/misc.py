from .object import (
    CObject,
    CObjectMeta,
)


class CNoneType(CObject):
    """
    Represents the type of the :py:class:`None` singleton, usually represented as just ``None`` in Python.
    """

    c = "void"


class CEllipsisType(CObject):
    """
    Represents the type of the :py:class:`Ellipsis` singleton.
    """

    c = "void"


def CExplicit(cpp_type: str) -> type[CObject]:
    """
    Helper function to create a C++ type from its C++ name.

    :param cpp_type: The C++ name of the type.
    :returns: A type object whose name is ``cpp_type``.
    """

    return CObjectMeta(
        "CExplicit",
        (CObject,),
        {"c": cpp_type, "__bool__": classmethod(lambda cls: False)},
    )
