from types import GenericAlias
from typing import Sequence, Never, Generator

import libcst as cst

import pyg3a
from pyg3a.scope import Scope
from pyg3a.types import Types
from pyg3a.types.generics import GenericArg


def _check_var_is_type(var_name: cst.Name | str, scope: Scope) -> bool:
    """
    Checks that a variable references a class (type).

    :param var_name: The name of the variable or a :py:class:`cst.Name` node representing it.
    :param scope: Scope to lookup types inside.
    :return: ``True`` if the variable is a class, ``False`` otherwise.
    """
    return var_name in scope and issubclass(scope[var_name].type, Types.type) and scope[var_name].value is not Never


def _cst_list_to_generic_args(elements: Sequence[cst.BaseElement], scope: Scope) -> Generator[GenericArg, None, None]:
    """
    Generator that converts the elements of a :py:class:`cst.List` node to a list of :py:class:`GenericArg` s.

    :param elements: The elements of the :py:class:`cst.List` node.
    :param scope: Scope to lookup types inside.
    :returns: Yields a :py:class:`GenericArg` for each element.
    """

    for el in elements:
        match el.value:
            case cst.Ellipsis():
                yield ...
            case cst.Name() as ann if _check_var_is_type(ann, scope):
                yield scope[ann].value
            case cst.List(elements=elements):
                yield list(_cst_list_to_generic_args(elements, scope))


def cst_annotation_to_type(ann: cst.BaseExpression, scope: Scope | None = None) -> Types.type:
    """
    Convert a :py:class:`cst.Annotation` node to the :py:class:`Types.type` it represents.

    :param ann: CST annotation node.
    :param scope: Optional scope to lookup types inside, defaults to :py:attr:`pyg3a.Main.globs`.
    :returns: The type given in the annotation, if found. Returns :py:class:`~pyg3a.types.object.COpNotImplemented` otherwise.
    """
    if scope is None:
        scope = pyg3a.Main.globs

    match ann:
        case cst.Subscript(value=cst.Name(value=generic), slice=indices):
            args: list[GenericArg] = []

            for index in indices:
                match index.slice:
                    case cst.Index(value=cst.Ellipsis()):
                        args.append(...)
                    case cst.Index(value=(cst.Name() as ann)) if _check_var_is_type(ann, scope):
                        args.append(scope[ann].value)
                    case cst.Index(value=cst.List(elements=elements)):
                        args.append(list(_cst_list_to_generic_args(elements, scope)))

            return scope[generic].value[*args]

        case cst.Name(value="None"):
            return Types.NoneType

        case cst.Name() as ann if _check_var_is_type(ann, scope):
            return scope[ann].value

    if ann == "None":
        return Types.NoneType
    return Types.NotImplemented


def str_to_type(s: str, scope: Scope | None = None) -> Types.type:
    """
    Convert a string to the :py:class:`Types.type` it represents.

    :param s: The string to convert.
    :param scope: Optional scope to lookup types inside, defaults to :py:attr:`pyg3a.Main.globs`.
    :returns: The type given in the string, if found. Returns a :py:func:`~pyg3a.types.misc.CExplicit` of the string otherwise.
    """
    if scope is None:
        scope = pyg3a.Main.globs

    if _check_var_is_type(s, scope):
        return scope[s].value
    elif "[" in s and "]" in s:
        generic_name, arguments = s.split("[", maxsplit=1)
        if _check_var_is_type(generic_name, scope):
            return scope[generic_name].value[
                *[str_to_type(s, scope) for s in arguments.replace(" ", "")[:-1].split(",")]
            ]

    if s == "None":
        return Types.NoneType
    return Types.Explicit(s)


def py_annotation_to_type(ann: str | type | None | GenericAlias, scope: Scope | None = None) -> Types.type:
    """
    Convert a Python annotation to the :py:class:`Types.type` it represents.

    :param ann: The annotation to convert.
    :param scope: Optional scope to lookup types inside, defaults to :py:attr:`pyg3a.Main.globs`.
    :returns: The type given in the annotation, if found. Returns :py:class:`~pyg3a.types.object.COpNotImplemented` otherwise.
    """

    if ann is None:
        return Types.NoneType

    if scope is None:
        scope = pyg3a.Main.globs

    if isinstance(ann, str):
        return str_to_type(ann, scope)

    if isinstance(ann, type):
        s: str = ann.__name__
        if _check_var_is_type(s, scope):
            return scope[s].value

    else:
        generic_name: str = ann.__origin__.__name__
        arguments: tuple[type | GenericAlias, ...] = ann.__args__

        if _check_var_is_type(generic_name, scope):
            return scope[generic_name].value[*[py_annotation_to_type(a) for a in arguments]]

    return Types.NotImplemented
