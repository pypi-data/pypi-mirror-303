import builtins
from types import EllipsisType
from typing import cast

import libcst as cst

import pyg3a
from pyg3a.logging import logger

type CSTConstant = cst.BaseNumber | cst.BaseString | cst.Ellipsis | cst.Name
"Union type representing all Python constants in the CST."

type Constant = int | float | complex | str | bool | EllipsisType | None
"Union type representing all Python constants."

type QualifiedConstOrTuple[T] = Constant | tuple[T, ...]
type ConstOrTuple = QualifiedConstOrTuple[Constant | cst.CSTNode] | QualifiedConstOrTuple[ConstOrTuple]


def py_const_to_c_str(
    const: ConstOrTuple,
) -> str:
    """
    Convert a Python ``const`` to a string containing a C equivalent.

    :param const: The Python constant to convert.
    :returns: C equivalent of ``const``.
    :raises SyntaxError: If a complex number is passed as ``const`` or an element of ``const`` if it is a tuple.
    """

    match const:
        case bool():
            # Bools are just ints in C
            return "1" if const is True else "0"
        case int() | float():
            # Numbers are the same in Python and C
            return str(const)
        case complex():
            # Complex numbers are unsupported
            raise SyntaxError("No support for complex numbers.")
        case str():
            # Use String class for strings
            escaped_str: str = const.replace('"', '\\"')
            return f'String("{escaped_str}")'
        case tuple():
            # Tuples are structs
            return f"{{{', '.join([py_const_to_c_str(o) for o in const])}}}"
        case builtins.Ellipsis:
            # Ellipses are comments
            return "/* ... */"
        case _:
            # Otherwise const is just None
            pyg3a.Main.project.includes.add("stddef.h")
            return "NULL"


def node_to_py_const(
    const: CSTConstant,
) -> Constant:
    """
    Convert a CST node representing a constant into its equivalent Python object.

    :param const: The constant to convert.
    :returns: The Python constant equivalent of the provided node.
    :raises SyntaxError: If the constant is an f-string.
    :raises TypeError: If the provided node cannot be interpreted.
    """

    match const:
        # ...
        case cst.Ellipsis():
            return ...

        # Numbers
        case cst.Imaginary() | cst.Integer() | cst.Float() as number:
            return number.evaluated_value

        # Strings
        case cst.SimpleString() as string:
            return cst.SimpleString(
                value=(
                    string.value.replace("\\x", "__pyg3a_double_escaped_x")
                    if string.prefix == "r"
                    else string.value.replace("\\x", "\\\\x")
                )
            ).evaluated_value
        case cst.FormattedString():
            raise SyntaxError("Formatted strings cannot be converted to constants")
        case cst.ConcatenatedString(left, right):
            if isinstance(left, cst.FormattedString) or isinstance(right, cst.FormattedString):
                raise SyntaxError("Formatted strings cannot be converted to constants")

            # Recurse over right argument
            return node_to_py_const(left) + cast(str, node_to_py_const(right))

        # True, False, None
        case cst.Name(value="True"):
            return True
        case cst.Name(value="False"):
            return False
        case cst.Name(value="None"):
            return None

        case _:
            raise TypeError(f"Wrong argument passed to node_to_py_const: {const}")
