# ========================================
# RESPONSABILITIES
# ========================================
"""
This module is responsible for handling the command-line interface (CLI)
for the nuxt3 https://nuxt.com/ framework
"""

# ========================================
# MIT License

# Copyright (c) 2024 Shared

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ========================================

# ========================================
# IMPORTS
# ========================================

# PYTHON LIBRARIES
# ========================================
import argparse
import importlib
import importlib.util
import logging
import os
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

# MODULE LIBRARIES
# ========================================
from fast2app.export import build_nuxt_server


class FastApiSpecification(BaseModel):
    """
    Describes a FastApi application i order to be abble to retrieve it as a python object
    """

    module: Path
    "the module path in which the application is defined"

    app_name: str
    "The name of the application within the module"

    @classmethod
    def from_path(cls, path: str) -> "FastApiSpecification":
        """
        Creates a FastApiSpecification from a path

        Args:
            path (str): the path in the form `module_path::app_name`

        Returns:
            FastApiSpecification:
                The FastApiSpecification instance
        """
        # Split the path
        split = path.split("::")

        # return the specifications
        return cls(module=Path(split[0]), app_name=split[1])

    def __str__(self) -> str:
        """
        Return the string representation of the FastApiSpecification
        """
        return_string = ""
        return_string += f"\n{f'`{self.app_name}`':10} in  `{self.module}`"
        return return_string

    @property
    def app(self) -> FastAPI:
        """
        The FastAPI application from this instance specifications

        Raises:
            ModuleNotFoundError: if the module is not found
            ModuleNotFoundError: if the module specification does  not have a loader

        Returns:
            FastAPI: A Fastapi object from the specifications
        """
        # Create the module specification
        module_specification = importlib.util.spec_from_file_location(
            self.module.name, self.module.as_posix()
        )

        if module_specification is None:
            raise ModuleNotFoundError(f"Module specification is None for {self.module}")

        # Load the module from the spec
        fast_api_module = importlib.util.module_from_spec(module_specification)

        if module_specification.loader is None:
            raise ModuleNotFoundError(
                f"Module specification loader is None for {self.module}"
            )

        module_specification.loader.exec_module(fast_api_module)

        # Get the app
        fast_api_app = getattr(fast_api_module, self.app_name)

        # Return the app
        return fast_api_app


class ProcessArguments(BaseModel):
    """
    Provides the arguments from the command line interface in a structured way²

    Args:
        fast_api_specifications(list[FastApiSpecification]):
            The list of FastApiSpecification to process


        export_path(Path):
            The path to the nuxt3 root folder
    """

    fast_api_specifications: list[FastApiSpecification]
    """The list of FastApiSpecification to process"""

    export_path: Path
    """The path to the nuxt root folder """

    export_composables: bool
    """Whether the composables must be exported"""

    logging_level: int
    """The log level"""

    @property
    def fast_api_list(self) -> list[FastAPI]:
        """The list of FastApi applications to export from the list of FastApiSpecification"""
        fastapi_list = [
            fast_api_definition.app
            for fast_api_definition in self.fast_api_specifications
        ]
        return fastapi_list

    def __str__(self) -> str:
        """A string representation of the ProcessArguments"""
        return_string = ""
        return_string += "\n BUILD ARGUMENTS"
        return_string += f"\n{'_' * 70}"
        return_string += (
            f"\n\n{'LOGGING LEVEL :':15}{logging.getLevelName(self.logging_level)}"
        )
        return_string += "\n\nFAST API LIST :"
        for fast_api_definition in self.fast_api_specifications:
            return_string += f"\n{fast_api_definition}"
            return_string += "\n"
        return_string += f"\n\n{'EXPORT PATH :':15}{self.export_path}"
        return_string += f"\n\n{'EXPORT COMPOSABLES :':15}{self.export_composables}"
        return_string += f"\n{'_' * 70}"
        return_string += "\n"

        return return_string


# ========================================
# FUNCTIONS
# ========================================


def main(args=None) -> None:
    """
    Run the command line interface.

    Args:
        args (list[str], optional):
            The command line arguments. Defaults to None.
            This argument is used for testing purposes.
    """
    # Header
    _display_text("Running fast2app")

    # Retrieve the build arguments from the command line
    build_arguments = _retrieve_build_arguments(args=args)

    # Export the FastApi applications to the designated nuxt
    try:
        _export(build_arguments=build_arguments)

        # footer
        _display_text(
            "Thanks for using fast2app",
            "repository:https://git.mydh.io/shared/fast2app",
            "contact : https://helpdesk.mydh.io/contact",
            "issues : https://helpdesk.mydh.io/issue-form",
        )

    except ValueError as error:
        _display_text(str(error))


# ========================================
# PRIVATE FUNCTIONS
# ========================================
def _retrieve_build_arguments(args: None) -> ProcessArguments:
    """
    Retrieve the build arguments from the command line.

    Args:
        args (list[str], optional):
            The command line arguments. Defaults to None.
            This argument is used for testing purposes.

    Returns:
        ProcessArguments: The process arguments
    """
    print("Retrieving build arguments\n")
    # Parser
    parser = argparse.ArgumentParser()

    # Fast Api List
    parser.add_argument(
        "-fa",
        "--fast-api-app",
        required=True,
        help="list of fast api module in the form of path/to/module.py::app_name",
        type=os.path.abspath,
        action="append",
    )

    # Export Path
    parser.add_argument(
        "-e",
        "--export-path",
        required=True,
        help="path to the nuxt3 root folder",
        type=os.path.abspath,
    )

    # Option
    parser.add_argument(
        "-c",
        "--composables",
        help="Use this flag to export the composables in adition to the api server",
        default=False,
        action="store_true",
    )

    # Option
    parser.add_argument(
        "-v",
        "--verbose",
        help="set logging level to INFO",
        default=False,
        action="store_true",
    )

    parser.add_argument(
        "-vv",
        "--very-verbose",
        help="set logging level to DEBUG",
        default=False,
        action="store_true",
    )
    # Parse the arguments
    arguments = parser.parse_args(args=args)

    if arguments.verbose:
        logging_level = logging.INFO
    elif arguments.very_verbose:
        logging_level = logging.DEBUG
    else:
        logging_level = logging.WARNING

    # Create the build arguments
    build_arguments = ProcessArguments(
        fast_api_specifications=[
            FastApiSpecification.from_path(path=path) for path in arguments.fast_api_app
        ],
        export_path=arguments.export_path,
        export_composables=arguments.composables,
        logging_level=logging_level,
    )

    print(build_arguments)

    return build_arguments


def _export(build_arguments: ProcessArguments) -> None:
    """
    Exports to nuxt according to the build arguments

    Args:
        build_arguments (ProcessArguments): The arguments to process
    """
    print("\n EXPORT")
    print(f"{'_' * 70}\n")

    print("Exporting to Nuxt3...")

    (
        nuxt_server_folder_path,
        interface_folder_path,
        composables_folder_path,
        runtime_config_variables,
    ) = build_nuxt_server(
        export_folder_path=build_arguments.export_path,
        *build_arguments.fast_api_list,
        export_composables=build_arguments.export_composables,
        logging_level=build_arguments.logging_level,
    )

    print("Exported to Nuxt3")
    print("\nEXPORTED FOLDERS :\n")
    print("______________________________________________________________________")
    print(f"\nNuxt server folder path :\n  `{nuxt_server_folder_path}`")
    print(f"\nInterface folder path :\n  `{interface_folder_path}`")
    print(f"\nComposables folder path :\n  `{composables_folder_path}`")

    # RUNTIM CONFIG
    runtime_config_variable_sequence = "    \n".join(
        [
            f"""
    // for FastAPI titled `{title}`
    {variable}  : process.env.NUXT_XXXXXXXXXX (or an hardcoded value)"""
            for title, variable in runtime_config_variables
        ]
    )

    app: str
    if len(runtime_config_variables) > 1:
        app = "apps"
    else:
        app = "app"

    print(
        f"""

!! IMPORTANT !!
______________________________________________________________________

For the generated files to work you must have ammended your
`nuxt.config.ts` file with rruntimeConfig variable targeting your FastApi {app} :

defineNuxtConfig({{

    // the rest of your config file

         runtimeConfig: {{
{runtime_config_variable_sequence}
     }}
}})"""
    )


def _display_text(*args: str) -> None:
    """
    Display text in the console.
    """
    print("")
    print(f"{'_' * 70}\n")
    for arg in args:
        print(f"{arg:^70}")
    print(f"{'_' * 70}")

    print("")
