from typing import NamedTuple
import builtins, typing

# Must import first
from .numbers import CInt, CBool, CFloat, CPointer
from .object import CObject, COpNotImplemented, CObjectMeta, CAny

from .misc import CNoneType, CEllipsisType, CExplicit
from .sequence import CSequence
from .callable import CCallable
from .string import CStr
from .list import CList
from .enum import CEnum, CEnumType
from .tuples import CTuple, CSpecificTuple, CArbitraryLengthTuple
from .generics import GenericType
from .generics import GenericType as GenT
from .type_alias import CTypeVar, CGenericTypeAlias


class _Types(NamedTuple):
    """
    Namespace storing references to type objects from their Python name.
    Implemented using a NamedTuple for memory efficiency.
    """

    # Built-ins
    object: type[CObject] = CObject
    int: type[CInt] = CInt
    bool: type[CBool] = CBool
    float: type[CFloat] = CFloat
    str: type[CStr] = CStr
    list: type[CList] = CList
    tuple: type = CTuple
    NotImplemented: type[COpNotImplemented] = COpNotImplemented

    # typing stdlib
    Any: type[CAny] = CAny  # type: ignore
    Callable: type[CCallable] = CCallable
    Sequence: type[type] = CSequence
    Generic: type[type] = GenericType
    TypeVar: type[CTypeVar] = CTypeVar
    TypeAliasType: type[CGenericTypeAlias] = CGenericTypeAlias

    # types stdlib
    NoneType: type[CNoneType] = CNoneType
    EllipsisType: type[CEllipsisType] = CEllipsisType

    # enum stdlib
    Enum: type[CEnum] = CEnum
    EnumType: type[CEnumType] = CEnumType

    # Our custom types
    SpecificTuple: type[CSpecificTuple] = CSpecificTuple
    ArbitraryLengthTuple: type[CArbitraryLengthTuple] = CArbitraryLengthTuple
    Explicit: typing.Callable[[builtins.str], type[CObject]] = CExplicit
    Pointer: type[CPointer] = CPointer
    GenericType: type[type] = type(GenT)

    # Inbuilt type - has to be last
    type: builtins.type[builtins.type] = builtins.type(CObject)  # CType


Types: _Types = _Types()
