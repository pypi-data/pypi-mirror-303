#!/usr/bin/env python3
import builtins
import dataclasses
from pathlib import Path
from typing import Final, Any, Never

import libcst as cst

import pyg3a
from .functions import Function, importer
from ..node import node_to_code
from ..type_utils import py_annotation_to_type
from ..types import Types


@dataclasses.dataclass(slots=True, init=False)
class Module:
    """
    Class for representing and interpreting importable modules.
    """

    name: Final[str]
    "This module's name."

    functions: Final[set[Function]]
    "Set of :py:class:`Function`s contained in this module."

    def __init__(self, name: str, file_name: Path) -> None:
        """
        Set up Module, generating its set of functions and immediately including required C headers and adding custom types.

        :param name: The name of this module.
        :param file_name: Path to the Python file defining this module.
        """

        self.name = name
        self.functions = set()

        # Open the module file and parse its contents
        with file_name.open() as f:
            self.parse_module(f.read())

    def parse_module(self, contents: str) -> None:
        """
        Parse the contents of a Python file defining this module and:
        - Generate this module's :py:attr`functions` set from ``func`` and ``func__iter__`` functions.
        - Register custom types specified in ``__registry_types_pyg3a`` functions.
        - Import C/C++ headers from ``import header`` and ``from header import`` statements. \
        See :py:meth:`~pyg3a.pyg3a.Project.include_from_python_name` for header name rules.

        :param contents: A string representing the contents of a Python file defining this module.
        """

        # For statement in module
        for stmt in cst.parse_module(contents).body:
            # Parse functions in module
            match stmt:
                case cst.ClassDef(name=py_name):
                    custom_builtins: dict[str, Any] = builtins.__dict__.copy()
                    custom_builtins["__import__"] = importer
                    custom_builtins["eval"] = lambda code: eval(code, {"__builtins__": {}}, {})
                    custom_builtins["exec"] = lambda code: eval(code, {"__builtins__": {}}, {})

                    new_type_globs: dict[str, Any] = {
                        "Types": Types,
                        "__builtins__": custom_builtins,
                    }
                    for name, var in pyg3a.Main.globs:
                        if issubclass(var.type, Types.type) and var.value is not Never:
                            new_type_globs[name] = var.value

                    exec(node_to_code(stmt), new_type_globs)

                    if isinstance(new_type_globs[py_name.value], Types.type) or isinstance(
                        new_type_globs[py_name.value], Types.GenericType
                    ):
                        pyg3a.Main.globs.set_var(
                            py_name, type(new_type_globs[py_name.value]), new_type_globs[py_name.value]
                        )

                # Add custom functions and __for_pyg3a_* functions from module to custom_functions dictionary
                case cst.FunctionDef(name=cst.Name(value=name)) if name[-8:] == "__iter__":
                    self.functions.add(Function[cst.For](stmt, self.name, cst.For))
                case cst.FunctionDef():
                    self.functions.add(Function[cst.Call](stmt, self.name, cst.Call))

                # Parse imports in module or constant definitions
                case cst.SimpleStatementLine(body=statements):
                    for simple_stmt in statements:
                        match simple_stmt:
                            case cst.Import(names=headers):
                                # For header in imports
                                for alias in headers:
                                    pyg3a.Main.project.include_from_python_name(node_to_code(alias.name))

                            # Include headers from ``from header import _``
                            case cst.ImportFrom(module=(cst.Module() | cst.Attribute() as header)):
                                pyg3a.Main.project.include_from_python_name(node_to_code(header))

                            # Constant type definitions
                            case cst.Assign(
                                targets=[cst.AssignTarget(target=cst.Name(value="DEFINES"))],
                                value=(cst.Dict() as definitions),
                            ) | cst.AnnAssign(target=cst.Name(value="DEFINES"), value=(cst.Dict() as definitions)):
                                new_type_globs: dict[str, Any] = {"Types": Types, "__builtins__": {}}
                                for name, var in pyg3a.Main.globs:
                                    if issubclass(var.type, Types.type) and var.value is not Never:
                                        new_type_globs[name] = var.value

                                for name, typ in eval(node_to_code(definitions), new_type_globs).items():
                                    pyg3a.Main.globs.set_type(
                                        cst.Name(value=name),
                                        Types.Explicit(typ) if isinstance(typ, str) else typ,
                                    )
