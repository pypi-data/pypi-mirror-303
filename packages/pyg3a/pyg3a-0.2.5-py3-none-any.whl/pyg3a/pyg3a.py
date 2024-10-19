#!/usr/bin/env python3

import argparse
import re
import shutil
import subprocess
from pathlib import Path
from sys import exit
from types import EllipsisType
from typing import Final

import libcst as cst

from pyg3a.modules import Module, ModuleSet
from pyg3a.types import Types
from .functions import Function
from .logging import logger, setup_logger
from .scope import Scope

"""
Main module, executed when ``pyg3a`` command is run.
Also contains many utility functions, the low-level ``Project`` class used to create and build your project, 
and the ``Main`` singleton storing global settings.
"""


class PyG3A:
    """
    Utility class with static methods to:
        * Add C functions to project
        * Include headers in project
        * Import module for project
        * Convert CST node to Python code
        * Generate string to indicate the type requirements of a function

    Also provides main() function which is run when pyg3a is executed
    """

    @staticmethod
    def add_c_func(name: str, c: str, param_types: list[Types.type] | EllipsisType, return_type: Types.type) -> None:
        """
        Add function to output C code and global scope.

        :param name: name of C function to add
        :param c: definition and body of C function
        :param param_types: list of types of C function's parameters
        :param return_type: return type of C function
        """
        if name in Main.project.extra_funcs and Main.project.extra_funcs[name] != c:
            logger.warning(f"Overriding function {name}!")

        Main.project.extra_funcs[name] = c
        Main.globs.set_func(name, param_types, return_type)

    @staticmethod
    def import_module(module_name: str) -> None:
        """
        Include header in output C code.

        :param module_name: header name, e.g. "list.hpp"
        :raises ImportError: If the header cannot be found
        """
        if module_name in Main.project.modules:
            return

        # Find module_name.py in Main.package_locs
        # Final location has priority
        file_name: Path = Path()
        for loc in Main.package_locs:
            if loc.joinpath(f"{module_name}.py").is_file():
                file_name = loc.joinpath(f"{module_name}.py")

        # If module doesn't exist, raise error
        if not file_name.is_file():
            raise ImportError(name=module_name)

        Main.project.modules.add(Module(module_name, file_name))

    @staticmethod
    def gen_tmp_var(scope: Scope, name: str = "var") -> str:
        if name in Main.tmp_nums:
            Main.tmp_nums[name] += 1
        else:
            Main.tmp_nums[name] = 0

        temp_name: str = f"__tmp_{name}_" + str(Main.tmp_nums[name])
        if temp_name not in scope:
            return temp_name

        raise RuntimeError(f"Too many temporary variables called {name}! Try using multiple files.")

    @staticmethod
    def main() -> None:
        """
        Main function - executed when pyg3a command is run. Steps:
            #. Parse arguments
            #. Set up logging
            #. Check if input file exists, else raise error
            #. Set up Main singleton
            #. Write C file and compile output G3A

        :raises FileNotFoundError: If the input python file doesn't exist.
        :raises IsADirectoryError: If the input python file is actually a directory.
        """

        # Parse arguments
        # usage: pyg3a [-h] [--debug] [--verbose] -l path/to/libfxcg py_file
        #
        # positional arguments:
        #   py_file               name of python file to convert
        #
        # options:
        #   -h, --help            show this help message and exit
        #   --debug               use debug mode
        #   --verbose             print command names in make
        #   -l path/to/libfxcg, --libfxcg path/to/libfxcg
        #                         libfxcg location

        parser = argparse.ArgumentParser()
        parser.add_argument("--debug", dest="debug", action="store_true", help="use debug mode")
        parser.add_argument("--verbose", dest="verbose", action="store_true", help="print command names in make")
        parser.add_argument("py_file", type=Path, nargs=1, help="name of python file to convert")
        parser.add_argument(
            "-l",
            "--libfxcg",
            dest="libfxcg",
            metavar="path/to/libfxcg",
            required=True,
            type=Path,
            nargs=1,
            help="libfxcg location",
        )
        args = parser.parse_args()

        # Setup logging for project
        setup_logger(args.debug)

        # Raise errors if file does not exist or is a directory
        if not args.py_file[0].is_file():
            raise FileNotFoundError(args.py_file[0])

        # Initialise Main singleton
        Main()

        # Setup Main singleton
        Main.project = Project(args.py_file[0].stem)
        Main.libfxcg = Path(args.libfxcg[0]).expanduser().absolute()
        Main.verbose = args.verbose
        Main.debug = args.debug

        Main.system_includes = [
            Path(path.replace("\n ", ""))
            for path in re.findall(
                r"\n .+",
                subprocess.run(
                    ("sh3eb-elf-gcc", "-xc++", "-E", "-Wp,-v", "-"), stdin=subprocess.PIPE, capture_output=True
                ).stderr.decode(),
            )
        ]

        # If a custom selected.bmp or unselected.bmp exist, use them, else use the system ones
        Main.project.create(
            (
                Path("selected.bmp")
                if Path("selected.bmp").is_file()
                else Path(__file__).parent.joinpath("selected.bmp")
            ),
            (
                Path("unselected.bmp")
                if Path("unselected.bmp").is_file()
                else Path(__file__).parent.joinpath("unselected.bmp")
            ),
        )

        # Load input python file
        Main.project.load(args.py_file[0])

        # Generate C code for project!
        Main.project.write()

        # Try to compile project
        try:
            Main.project.make()
        except subprocess.CalledProcessError as e:
            exit(e.returncode)


class Project:
    """
    Class used to store project code, write C and Make files and make the project.
    """

    name: Final[str]
    "Name of project, set in constructor."

    build_dir: Final[Path]
    "Absolute path to .pyg3a_build directory for this project."

    modules: Final[ModuleSet]
    "Set of imported modules."

    includes: Final[set[str]]
    "Set of imported headers. Includes 'str.hpp' by default."

    functions: Final[list[Function]]
    "List of functions inside this project."

    custom_funcs: Final[dict[str, str]]
    "Map of modules' custom function names -> Python code."

    extra_funcs: Final[dict[str, str]]
    "Map of modules' extra function names -> C code."

    c: str
    "C code representing the whole project."

    __slots__ = "name", "c", "functions", "modules", "includes", "custom_funcs", "extra_funcs", "build_dir"

    def __init__(self, name: str) -> None:
        """
        Initialise project with a name.

        :param name: Name of project - used in output file name and .pyg3a_build/ subdirectory name.
        """
        self.name = name
        self.build_dir = Path(f".pyg3a_build/{self.name}").absolute()
        self.modules = ModuleSet()
        self.includes = {"str.hpp"}
        self.functions = []
        self.custom_funcs = {}
        self.extra_funcs = {}

        self.c = ""

    def add_func(self, func_def: cst.FunctionDef, scope: Scope) -> None:
        """
        Add function to project from CST Function definition.

        :param func_def: Node's function definition to convert to a :py:class:`~pyg3a.functions.Function` and add to the project.
        :param scope: The scope in which the function is defined (the function's parent scope).
        """

        self.functions.append(Function(func_def, scope))

    def include_from_python_name(self, header: str) -> None:
        for loc in [Path(Main.libfxcg).joinpath("include"), Path("include"), *Main.system_includes]:
            # If it's a C++ header
            if loc.joinpath(header.replace(".", "/") + ".hpp").exists():
                self.includes.add(header.replace(".", "/") + ".hpp")

            # If it's a C header
            elif loc.joinpath(header.replace(".", "/") + ".h").exists():
                self.includes.add(header.replace(".", "/") + ".h")

    def write(self) -> None:
        """
        Write C file from stored C code.

        :raises RuntimeError: If the project has not been created with ``self.create()`` first.
        """
        if not self.build_dir.joinpath("src/").is_dir():
            raise RuntimeError("Please run create() first")

        with self.build_dir.joinpath("src/main.cpp").open("w") as f:
            f.write(self.c.replace("\\\\x", "\\x").replace("__pyg3a_double_escaped_x", "\\\\x"))

    # noinspection SpellCheckingInspection
    def create(
        self,
        selected_img: Path = Path("selected.bmp"),
        unselected_img: Path = Path("unselected.bmp"),
    ) -> None:
        """
        Create .pyg3a_build/`name`/src dir and write Makefile

        :param selected_img: Location of BMP/PNG image to show when addin is selected in the OS menu.
        Defaults to "selected.bmp" in the current dir.
        :param unselected_img: Location of BMP/PNG image to show when addin is unselected imin the OS menu.
        Defaults to "unselected.bmp" in the current dir.
        """
        src_dir: Path = self.build_dir.joinpath("src")

        # Make .pyg3a_build/`name` dir and src/ dir inside it.
        src_dir.mkdir(parents=True, exist_ok=True)

        new_makefile: str = (
            ".SUFFIXES:\n" + f"export FXCGSDK := {Main.libfxcg.absolute()}\n"
            # Use libfxcg location from -l/--libfxcg option
            + "include $(FXCGSDK)/toolchain/prizm_rules\n"
            + (
                "export CXX    := @$(CXX)\n" if not Main.verbose else ""
            )  # If we're in --verbose mode, print to the console when running G++ and mkg3a
            + ("export MKG3A  := @$(MKG3A)\n" if not Main.verbose else "")
            + """TARGET		:=	$(notdir $(CURDIR))
BUILD		:=	build
SOURCES		:=	src
DATA		:=	data
"""  # Allow includes from pyg3a_loc/include/ dir
            + f"INCLUDES := {Path(__file__).parent.joinpath("include")}\n"
            + f"MKG3AFLAGS := -n basic:{self.name} -i uns:{unselected_img.absolute()} -i sel:{selected_img.absolute()}\n"
            + f"CFLAGS	= -Os {'-Wall' if Main.verbose else ''} $(MACHDEP) $(INCLUDE) -ffunction-sections "
            "-fdata-sections -fno-exceptions\n"
            + """CXXFLAGS	=	$(CFLAGS)

LDFLAGS	= $(MACHDEP) -T$(FXCGSDK)/toolchain/prizm.x -Wl,-static -Wl,-gc-sections -fno-exceptions

LIBS	:=	 -lc -lfxcg -lgcc
"""
            + f"LIBDIRS	:= {Path(__file__).parent}"
            + """
ifneq ($(BUILD),$(notdir $(CURDIR)))

export OUTPUT	:=	$(CURDIR)/$(TARGET)

export VPATH	:=	$(foreach dir,$(SOURCES),$(CURDIR)/$(dir)) \\
                    $(foreach dir,$(DATA),$(CURDIR)/$(dir))

export DEPSDIR	:=	$(CURDIR)/$(BUILD)

CFILES		:=	$(foreach dir,$(SOURCES),$(notdir $(wildcard $(dir)/*.c)))
CPPFILES	:=	$(foreach dir,$(SOURCES),$(notdir $(wildcard $(dir)/*.cpp)))
sFILES		:=	$(foreach dir,$(SOURCES),$(notdir $(wildcard $(dir)/*.s)))
SFILES		:=	$(foreach dir,$(SOURCES),$(notdir $(wildcard $(dir)/*.S)))
BINFILES	:=	$(foreach dir,$(DATA),$(notdir $(wildcard $(dir)/*.*)))

ifeq ($(strip $(CPPFILES)),)
\texport LD	:=	$(CC)
else
\texport LD	:=	$(CXX)
endif

export OFILES	:=	$(addsuffix .o,$(BINFILES)) \\
                    $(CPPFILES:.cpp=.o) $(CFILES:.c=.o) \\
                    $(sFILES:.s=.o) $(SFILES:.S=.o)

export INCLUDE	:=	$(foreach dir,$(INCLUDES), -iquote $(CURDIR)/$(dir)) \\
                    $(foreach dir,$(LIBDIRS),-I$(dir)/include) \\
                    -I$(CURDIR)/$(BUILD) -I$(LIBFXCG_INC)

export LIBPATHS	:=	$(foreach dir,$(LIBDIRS),-L$(dir)/lib) \\
                    -L$(LIBFXCG_LIB)

export OUTPUT	:=	$(CURDIR)/$(TARGET)
.PHONY: all clean

all: $(BUILD)
\t@make --no-print-directory -C $(BUILD) -f $(CURDIR)/Makefile

$(BUILD):
\t@mkdir $@

export CYGWIN := nodosfilewarning
clean:
\t$(call rmdir,$(BUILD))
\t$(call rm,$(OUTPUT).bin)
\t$(call rm,$(OUTPUT).g3a)

else

DEPENDS	:=	$(OFILES:.o=.d)

$(OUTPUT).g3a: $(OUTPUT).bin
$(OUTPUT).bin: $(OFILES)


-include $(DEPENDS)

endif
"""
        )

        # Check if Makefile needs updating
        if self.build_dir.joinpath("Makefile").is_file():
            with self.build_dir.joinpath("Makefile").open() as makefile:
                if makefile.read() == new_makefile:
                    return

        with self.build_dir.joinpath("Makefile").open("w") as makefile:
            makefile.write(new_makefile)

    def make(self) -> None:
        """
        Build the project according to the created Makefile and copy the built G3A to the current dir.

        :raises RuntimeError: If ``self.create()`` has not been run yet.
        :raises FileNotFoundError: If the G3A failed to build.
        """
        try:
            # Use ``make`` to build project
            if self.build_dir.joinpath("Makefile").is_file():
                subprocess.run(["/bin/make"], cwd=self.build_dir, check=True)
            else:
                raise RuntimeError("Please run write() first")
        except FileNotFoundError:
            raise RuntimeError("Please run create() first") from None

        try:
            # Copy built G3A to current directory
            shutil.copyfile(self.build_dir.joinpath(f"{self.name}.g3a"), Path(f"{self.name}.g3a"))
        except FileNotFoundError as err:
            raise err

    def load(self, py_file: Path) -> None:
        """
        High-level function to transpile the input python file into the project's C code:
            #. Parse ``filename`` as a libcst Module.
            #. Make ``int main`` function with Module body.
            #. Import ``stdpy`` package.
            #. Construct (transpile) the main function.
            #. Add included headers to C code.
            #. Add imported packages to C code.
            #. Add all function declarations to C code.
            #. Add function bodies to C code.

        :param py_file: Python file to transpile.
        """

        parsed: cst.Module
        with py_file.open() as f:
            parsed = cst.parse_module(f.read())

        self.functions.append(
            Function(
                cst.FunctionDef(
                    name=cst.Name(value="main"),
                    params=cst.Parameters(params=[]),
                    body=cst.IndentedBlock(body=parsed.body),
                    returns=cst.Annotation(annotation=cst.Name(value="int")),
                ),
                Main.globs,
            )
        )

        lines: list[str] = []
        func_lines: dict[str, str] = {}

        PyG3A.import_module("stdpy")

        # Then re-construct with new knowledge
        for func in self.functions:
            func_lines[func.name] = func.construct() + "\n"

        if Main.debug:
            lines.append("/* --- Imports --- */\n")

        for imp in sorted(self.includes):
            lines.append(f"#include <{imp}>")
        lines.append("")

        if Main.debug:
            lines.append("/* --- Package helpers --- */\n")

        lines.append("\n\n".join(self.extra_funcs.values()))
        lines.append("")

        if Main.debug:
            lines.append("/* --- Function declarations --- */\n")

        lines.extend([fun.declaration() for fun in self.functions if fun.name != "main"])
        lines.append("")

        if Main.debug:
            lines.append("/* --- Functions --- */\n")

        lines.extend(func_lines.values())

        self.c = "\n".join(lines)

        logger.debug(self.c)

        logger.debug(f"modules: {self.modules}")
        logger.debug("imports: " + ", ".join(self.includes))


class Main:
    """
    Singleton storing global settings, project, info from transpiling, and type registry
    """

    libfxcg: Path = Path("../../").absolute()
    "Libfxcg location provided by -l/--libfxcg flag, defaulting to '../../'."

    verbose: bool = False
    "Verbose mode, enabled by --verbose. False by default."

    package_locs: list[Path] = [Path("~/.local/lib/pyg3a").expanduser(), Path(__file__).parent.joinpath("packages")]
    "Locations that packages can be found. Defaults to ``~/.local/lib/pyg3a/`` and ``/path/to/pyg3a/install/location/packages/``."

    project: Project = Project("NONE")
    "Global Project instance."

    main_function_overridden: bool = False
    (
        "Has the ``main()`` function been overriden? False by default "
        "(i.e. C's ``int main`` function will contain the lines not included in functions in the input python file)."
    )

    tmp_nums: dict[str, int] = {}
    "Dictionary of ``{function_name: temporary_number}``."

    globs: Scope = Scope(None, {name: (Types.type, typ) for name, typ in zip(Types.__annotations__, Types)})
    "Global scope of project, initialised with inbuilt types."

    codegen_module: cst.Module = cst.Module([], default_indent="\t", has_trailing_newline=False)
    "Module used to generate code in :py:meth:`pyg3a.node.node_to_code`."

    debug: bool = False
    "Debug mode, enabled by --debug. False by default."

    system_includes: list[Path] = []
    "System include paths generated from G++ output."


if __name__ == "__main__":
    PyG3A.main()
