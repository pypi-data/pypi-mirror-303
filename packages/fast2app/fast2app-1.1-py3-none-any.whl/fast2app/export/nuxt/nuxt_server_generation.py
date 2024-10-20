# ========================================
# RESPONSABILITIES
# ========================================
"""
Provides the core  functionality for the nuxt server generation.

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

from datetime import datetime
from enum import Enum
import logging
from pathlib import Path
from types import GenericAlias
from typing import Any
from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.types import UnionType
from jinja2 import Environment, FileSystemLoader
import os

from pydantic import BaseModel

# MODULE LIBRARIES
# ========================================
from fast2app.utils import (
    to_javascript_type_name,
    to_javascript_name,
    to_url,
    generate_random_string,
    load_config,
)
from fast2app.parsing import (
    get_api_routes,
    parse_response_models,
    parse_query_types,
    parse_body_models,
    get_path_arguments,
    get_query_arguments,
    get_body_arguments,
    get_route_input_model,
    parse_types,
)

from fast2app.export.type_script import convert_to_typescript

import fast2app


# ========================================
# VARIABLAES
# ========================================


# TEMPLATE FOLDER
FILE_DIRECTORY = Path(__file__).parent
" The directory where this file is stored"

TEMPLATE_DIRECTORY: Path = FILE_DIRECTORY / "templates"
" The directory where the templates are stored"

logging.info(f"TEMPLATE DIRECTORY : `{TEMPLATE_DIRECTORY.as_posix()}`")
ENVIRONMENT = Environment(loader=FileSystemLoader(TEMPLATE_DIRECTORY.as_posix()))
"The jinja2 environment"


# API TEMPLATES
API_HEADER_TEMPLATE = ENVIRONMENT.get_template("apiHeader.ts")
"The template for the file header and disclaimer"

API_USAGE_TEMPLATE = ENVIRONMENT.get_template("apiUsage.ts")
"The template for the usage explanation of the exported file"

API_IMPORT_TEMPLATE = ENVIRONMENT.get_template("apiImport.ts")
"The template for the imports in the exported file"

API_FUNCTION_TEMPLATE = ENVIRONMENT.get_template("apiFunction.ts")
"The template for the actual server function in the exported file"


# COMPOSABLE TEMPLATES
COMPOSABLE_HEADER_TEMPLATE = ENVIRONMENT.get_template("composableHeader.ts")
"The template for the file header and disclaimer"

COMPOSABLE_USAGE_TEMPLATE = ENVIRONMENT.get_template("composableUsage.ts")
"The template for the usage explanation of the exported file"

COMPOSABLE_IMPORT_TEMPLATE = ENVIRONMENT.get_template("composableImport.ts")
"The template for the imports in the exported file"

COMPOSABLE_FUNCTION_TEMPLATE = ENVIRONMENT.get_template("composableFunction.ts")
"The template for the actual server function in the exported file"


PYTHON_PACKAGE: str = f"{fast2app.__name__}"
"The name of this python package"
# ========================================
# FUNCTIONS
# ========================================


def generate_nuxt_server(
    app: FastAPI,
    server_folder_path: Path,
) -> None:
    """
    Generates the nuxt server api from a `FastApi` app

    Args:
        app (FastAPI):
            The app to process

        server_folder_path (Path):
            The destination path
    """
    routes: list[APIRoute] = get_api_routes(app=app)

    for route in routes:
        _generate_nuxt_server_route(
            route=route, server_folder_path=server_folder_path, app_title=app.title
        )


def generate_nuxt_composables(
    app: FastAPI,
    composables_folder_path: Path,
) -> None:
    """
    Generates the nuxt server api from a `FastApi` app

    Argss:
        app (FastAPI):
            The app to process

        composables_folder_path (Path):
            The destination path


    """
    routes: list[APIRoute] = get_api_routes(app=app)

    for route in routes:

        _generate_nuxt_composable_from_route(
            app_name_url=to_url(app.title),
            route=route,
            composables_folder_path=composables_folder_path,
            app_title=app.title,
        )


# ========================================
# EXPORT SERVER PRIVATE FUNCTIONS
# ========================================
def _generate_nuxt_server_route(
    route: APIRoute, server_folder_path: Path, app_title: str
) -> None:
    """
    Generate a nuxt server typescript file fetching the data from the provided route

    Args:
        route (APIRoute):
            The route to process

        server_folder_path (Path):
            The root folder for the nuxt server

        root_folder_name (str):
            the server root folder name

        app_title (str):
            The app title
    """

    for method in route.methods:
        _export_server_file(
            route=route,
            method=method,
            server_folder_path=server_folder_path,
            app_title=app_title,
        )


def _export_server_file(
    route: APIRoute, method: str, server_folder_path: Path, app_title: str
) -> None:
    """
    Generates and export the server file

    Args:
        route (APIRoute):
            The route to process

        method (str):
            The method to export

        server_folder_path (Path):
            The root folder for the nuxt server

        app_title (str):
            The app title

            the server root folder name
    """
    # FILE
    # ----------------------

    ## file path
    api_file_path = _get_api_file_path(
        route_path=route.path, method=method, server_folder_path=server_folder_path
    )

    ## create folder if not exists
    api_file_path.parent.mkdir(parents=True, exist_ok=True)

    ## file name
    file_name = api_file_path.as_posix()

    # CONTENT
    # ----------------------

    runtime_config_base_url_variable = get_runtime_config_variable_name(
        app_title=app_title
    )
    content = _get_api_file_content(
        route=route,
        method=method,
        runtime_config_base_url_variable=runtime_config_base_url_variable,
    )

    # EXPORT
    # ----------------------
    logging.info(f"Exporting Nuxt server file to `{file_name}`")

    with open(file_name, mode="w", encoding="utf-8") as message:
        message.write(content)


def _get_api_file_path(route_path: str, method: str, server_folder_path: Path) -> Path:
    """
    Returns the file paths from the route

    Args:
        route_path (str):
            the route path from the APIRoute

        method (str):
            the method to export

        server_folder_path (Path):
            the root server path


    Returns:
        Path: The path of the exporter file
    """

    # REPLACE {} with []
    route_path_with_bracket = route_path.replace("{", "[").replace("}", "]")

    route_elements = route_path_with_bracket.split("/")

    def replace_path_by_ellipsis(path_element: str) -> str:
        if ":path" in path_element:
            value = path_element.replace(":path", "")
            return value
        else:
            return path_element

    processed_path_path_elements: list[str] = [
        replace_path_by_ellipsis(path_element)
        for path_element in route_elements
        if path_element != ""
    ]

    processed_path = "/".join(processed_path_path_elements)

    if processed_path == "":
        relative_route_path: str = f"{method.lower()}.ts"
    else:
        relative_route_path: str = f"{processed_path}.{method.lower()}.ts"

    api_file_path: Path = server_folder_path / relative_route_path
    return api_file_path


# ========================================
# CONTENT PRIVATE FUNCTIONS
# ========================================
def _get_api_file_content(
    route: APIRoute, method: str, runtime_config_base_url_variable: str
) -> str:
    """
    Returns the file content for the server file

    Args:
        route (APIRoute):
            The route to process

        method (str):
            The method to process


    Returns:
        str: The connt of the file
    """

    logging.info("Getting API Server file content...")
    api_header_content = _get_api_header_content()

    api_url = f"/api{route.path}"

    api_usage_content = _get_api_usage_content(
        runtime_config_base_url_variable=runtime_config_base_url_variable,
        api_url=api_url,
        method=method,
    )
    api_import_content = _get_api_import_content(route=route)
    api_function_content = _get_api_function_content(
        route=route,
        method=method,
        runtime_config_base_url_variable=runtime_config_base_url_variable,
    )

    content = "\n\n".join(
        [
            api_header_content,
            api_usage_content,
            api_import_content,
            api_function_content,
        ]
    )

    return content


def _get_api_header_content() -> str:
    """
    Generates the header content


    Returns:
        str: _description_
    """
    try:
        username = os.getlogin()
    except OSError as e:
        logging.error(f"Unable to get username: {e}")
        username = "unknown"

    RANDOM_WATER_MARK = _get_watermark()

    input_dictionnary: dict[str, str] = {
        "python_package": PYTHON_PACKAGE,
        "date": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        "username": username,
        "random_watermark": RANDOM_WATER_MARK,
    }

    return API_HEADER_TEMPLATE.render(input_dictionnary)


def _get_api_usage_content(
    runtime_config_base_url_variable: str, api_url: str, method: str
) -> str:
    """
    Generates the usage content from the template.

    Args:

        runtime_config_base_url_variable (str):
            The name of the runtimeConfig private variable pointing to the FastApi baseurl.


    Returns:
        str: The usage content
    """
    input_dictionnary: dict[str, str] = {
        "api_url": api_url,
        "method": method,
        "backend_url": runtime_config_base_url_variable,
    }

    return API_USAGE_TEMPLATE.render(input_dictionnary)


def _get_api_import_content(route: APIRoute) -> str:
    """
    Gets the import lines.
    BaseModel import are un alphabetical order

    Args:
        route (APIRoute): the route to process

    Returns:
        str: The import lines
    """

    # Only reponse model are requiered
    model_set: set[type] = set()
    model_set.update(parse_response_models(route=route))

    model_set.update(parse_query_types(route=route))

    # model_set = model_set.union(parse_body_models(route=route))

    # MODEL NAMES
    logging.debug({"model_set": model_set})
    model_names = [to_javascript_type_name(model.__name__) for model in model_set]
    model_names.sort()
    model_string: str = ", ".join(model_names)

    logging.debug(
        {
            "model_set": model_set,
            "model_names": model_names,
            "model_string": model_string,
        }
    )

    # INPUT DICTIONARY
    input_dictionnary: dict[str, str] = {"model_string": model_string}

    return API_IMPORT_TEMPLATE.render(input_dictionnary)


def _get_api_function_content(
    route: APIRoute, method: str, runtime_config_base_url_variable: str
) -> str:

    response_type: str | None

    logging.debug({"route.response_model": route.response_model})

    input_dictionnary: dict[str, Any] = {}

    # ROUTE
    # --------------------------------
    input_dictionnary["route"] = _get_route_path(route=route)
    input_dictionnary["backend_url"] = runtime_config_base_url_variable

    # RESPONSE TYPE
    # --------------------------------

    is_base_model: bool
    try:
        is_base_model = issubclass(route.response_model, BaseModel)
    except TypeError:
        is_base_model = False

    ## CASE NONE
    if route.response_model is None:
        response_type = None

    ## CASE GENERIC ALIAS
    elif isinstance(route.response_model, GenericAlias):
        response_type = convert_to_typescript(route.response_model)

    # CASE UNION TYPE
    elif isinstance(route.response_model, UnionType):
        response_type = convert_to_typescript(route.response_model)

    ## CASE PYDANTIC BASEMODEL
    elif is_base_model:

        response_type = route.response_model.__name__

    ## CASE GENERIC JSON
    else:
        response_type = convert_to_typescript(route.response_model)

    if response_type is not None:
        input_dictionnary["response_type"] = response_type

    # QUERY
    # --------------------------------
    query_arguments: list[tuple[str, type]] = get_query_arguments(route=route)

    if len(query_arguments) >= 1:

        input_dictionnary["query_arguments"] = [
            (argument_name, convert_to_typescript(input_type=argument_type))
            for argument_name, argument_type in query_arguments
        ]

        # add query function
        def _get_query_string(query_arguments: list[tuple[str, type]]) -> str:

            return ", ".join(
                [
                    f"{argument_name}: {argument_name}"
                    for argument_name, argument_type in query_arguments
                ]
            )

        input_dictionnary["_get_query_string"] = _get_query_string

    # PATH
    # --------------------------------
    path_arguments: list[tuple[str, type]] = get_path_arguments(route=route)

    if len(path_arguments) >= 1:
        input_dictionnary["path_arguments"] = [
            (argument_name, convert_to_typescript(input_type=argument_type))
            for argument_name, argument_type in path_arguments
        ]

        # add path function
        def _get_path_string(path_arguments: list[tuple[str, type]]) -> str:

            return ", ".join(
                [
                    f"{argument_name}: {argument_name}"
                    for argument_name, argument_type in path_arguments
                ]
            )

        input_dictionnary["_get_path_string"] = _get_path_string

    # METHOD
    # --------------------------------
    input_dictionnary["method"] = method.upper()

    # BODY
    # --------------------------------
    body_arguments: list[tuple[str, type]] = get_body_arguments(route=route)

    if len(body_arguments) >= 1:
        input_dictionnary["body_arguments"] = [
            (argument_name, convert_to_typescript(argument_type))
            for argument_name, argument_type in body_arguments
        ]

    # RENDER
    # --------------------------------
    return API_FUNCTION_TEMPLATE.render(input_dictionnary)


# ========================================
# EXPORT COMPOSABLES PRIVATE FUNCTIONS
# ========================================


def _generate_nuxt_composable_from_route(
    app_name_url: str,
    route: APIRoute,
    composables_folder_path: Path,
    app_title: str,
) -> None:
    """
    Get the composable from a route

    Args:
        app_name_url (str):
            The name of the app
        route (APIRoute):
            The route to process

        composables_folder_path (Path): _description_


        app_title (str):
            The app title
    """

    # CASE ONE METHOD

    # CASE MULTIPLE METHODS (I don't know if it's possible)
    for method in route.methods:

        _export_composable_file(
            app_name_url=app_name_url,
            route=route,
            method=method,
            composables_folder_path=composables_folder_path,
            app_title=app_title,
        )


def _export_composable_file(
    app_name_url: str,
    route: APIRoute,
    method: str,
    composables_folder_path: Path,
    app_title: str,
) -> None:
    """
    Exports the composable file

    Args:
        app_name_url (str):
            The name of the app

        route (APIRoute):
            The route to process

        method (str):
            The method to process

        composables_folder_path (Path):
            The destination path


        app_title (str):
            The app title
    """

    # file path
    composable_file_path = _get_composable_file_path(
        route=route,
        method=method,
        composables_folder_path=composables_folder_path,
    )

    ## create folder if not exists
    composable_file_path.parent.mkdir(parents=True, exist_ok=True)

    # file name
    composable_file_name = composable_file_path.as_posix()

    composable_name = composable_file_path.stem

    # CONTENT
    # ----------------------
    runtime_config_base_url_variable = get_runtime_config_variable_name(
        app_title=app_title
    )
    composable_file_content = _get_composable_file_content(
        app_name_url=app_name_url,
        route=route,
        method=method,
        runtime_config_base_url_variable=runtime_config_base_url_variable,
        composable_name=composable_name,
    )

    # EXPORT
    # ----------------------
    logging.info(f"Exporting composable file: {composable_file_name}")

    with open(composable_file_path, "w") as f:
        f.write(composable_file_content)


def _get_composable_file_path(
    route: APIRoute, method: str, composables_folder_path: Path
) -> Path:
    """
    Get the composable file path
    Args:
        route (APIRoute):
            The route to process

        method (str | None):
            The method to process if any

        composables_folder_path (Path):
            The destination path

        use_method_name_in_composable_name (bool):
            Whether to use the method name in the composable name.

    Returns:
        Path:
            The composable file path
    """
    composable_file_name = f"{to_javascript_name(route.name)}.ts"
    composable_file_path = composables_folder_path / composable_file_name
    return composable_file_path


def _get_composable_file_content(
    app_name_url: str,
    route: APIRoute,
    method: str,
    runtime_config_base_url_variable: str,
    composable_name: str,
) -> str:
    """
    Get the composable file content

    Args:
        app_name_url (str):
            The name of the app

        route (APIRoute):
            The route to process

        method (str):
            The method to process

        runtime_config_base_url_variable (str):
            The name of the runtimeConfig private variable pointing to the FastApi baseurl.

        composable_name (str):
            the name of the composable file
    Returns:
            str:
                The composable file content
    """
    logging.info("Getting API Server file content...")
    composable_header_content = _get_composable_header_content()
    composable_usage_content = _get_composable_usage_content(
        runtime_config_base_url_variable=runtime_config_base_url_variable,
        composable_name=composable_name,
    )
    composable_import_content = _get_composable_import_content(route=route)
    composable_function_content = _get_composable_function_content(
        app_name_url=app_name_url,
        route=route,
        method=method,
        # use_method_name_in_composable_name=use_method_name_in_composable_name
    )

    content = "\n\n".join(
        [
            composable_header_content,
            composable_usage_content,
            composable_import_content,
            composable_function_content,
        ]
    )

    return content


def _get_composable_header_content() -> str:
    """
    Get the composable header content

        str:
            The composable header content
    """
    try:
        username = os.getlogin()
    except OSError as e:
        logging.error(f"Unable to get username: {e}")
        username = "unknown"

    RANDOM_WATER_MARK = _get_watermark()

    input_dictionnary: dict[str, str] = {
        "python_package": PYTHON_PACKAGE,
        "date": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        "username": username,
        "random_watermark": RANDOM_WATER_MARK,
    }

    return COMPOSABLE_HEADER_TEMPLATE.render(input_dictionnary)


def _get_composable_usage_content(
    runtime_config_base_url_variable: str, composable_name: str
) -> str:
    """
    Get the composable usage content

    Args:

        runtime_config_base_url_variable (str):
            The name of the runtimeConfig private variable pointing to the FastApi baseurl.

        composable_name (str):
            the name of the composable file


    Returns:
        str:
            The composable usage content
    """

    input_dictionnary: dict[str, str] = {
        "composable_name": composable_name,
        "backend_url": runtime_config_base_url_variable,
    }

    return COMPOSABLE_USAGE_TEMPLATE.render(input_dictionnary)


def _get_composable_import_content(route: APIRoute) -> str:
    """
    Get the composable import content
    Args:
        route (APIRoute):
            The route to process
    Returns:
        str:
            The composable import content
    """
    # MODEL SET
    model_set: set[type[BaseModel]] = set()

    # INPUT MODEL
    input_model = get_route_input_model(route=route)
    if input_model is not None:
        model_set.add(input_model)

    # QUERY MODEL
    model_set.update(parse_query_types(route=route))

    # BODY MODEL

    body_models = parse_body_models(route=route)
    model_set = model_set.union(body_models)

    if len(body_models) == 0 and route.body_field:

        annotation = route.body_field.field_info.annotation

        annotation_model = parse_types(annotation, [BaseModel, Enum])
        model_set = model_set.union(annotation_model)
        logging.debug(
            {
                "route": route.path,
                "method": route.methods,
                "annotation": annotation,
                "annotation_model": annotation_model,
                "model_set": model_set,
            }
        )

    # REPONSE MODEL
    model_set = model_set.union(parse_response_models(route=route))

    # MODEL NAMES
    logging.debug({"model_set": model_set})
    model_names = [to_javascript_type_name(model.__name__) for model in model_set]
    model_names.sort()
    model_string: str = ", ".join(model_names)

    logging.debug(
        {
            "route": route.path,
            "method": route.methods,
            "model_set": model_set,
            "model_names": model_names,
            "model_string": model_string,
        }
    )

    # INPUT DICTIONARY
    input_dictionnary: dict[str, str] = {}
    input_dictionnary["model_string"] = model_string
    return COMPOSABLE_IMPORT_TEMPLATE.render(input_dictionnary)


def _get_composable_function_content(
    app_name_url: str,
    route: APIRoute,
    method: str,
) -> str:
    """
    Get the composable function content
    Args:
        app_name_url (str):
            The name of the app

        route (APIRoute):
            The route to process

        method (str):
            The method to process

        runtime_config_base_url_variable (str):
            The name of the runtimeConfig private variable pointing to the FastApi baseurl.


    Returns:
        str:
            The composable function content
    """

    logging.debug({"route.response_model": route.response_model})

    input_dictionnary: dict[str, Any] = {}

    # ROUTE & APP NAME
    # --------------------------------
    input_dictionnary["route"] = _get_route_path(route=route)
    input_dictionnary["app_name_url"] = app_name_url

    # TYPESCRIPT COMPOSABLE NAME
    # --------------------------------
    typescript_composable_name = to_javascript_name(route.name)

    input_dictionnary["typescript_composable_name"] = typescript_composable_name

    # INPUT TYPE
    # --------------------------------

    # INPUT TYPE DECLARATION
    input_type_declaration: str | None

    input_model = get_route_input_model(route=route)

    if input_model is None:
        input_type_declaration = None

    else:
        input_type_declaration = f"{to_javascript_name(input_model.__name__)}: {convert_to_typescript(input_model)}"

    input_dictionnary["input_type_declaration"] = input_type_declaration

    # INPUT TYPE NAME
    input_type_name: str | None
    if input_model is None:
        input_type_name = None
    else:
        input_type_name = to_javascript_name(input_model.__name__)

    input_dictionnary["input_type_name"] = input_type_name

    # RESPONSE TYPE
    # --------------------------------

    is_base_model: bool
    try:
        is_base_model = issubclass(route.response_model, BaseModel)
    except TypeError:
        is_base_model = False

    response_type: str

    ## CASE NONE
    if route.response_model is None:
        response_type = "void"

    ## CASE GENERIC ALIAS
    elif isinstance(route.response_model, GenericAlias):
        response_type = convert_to_typescript(route.response_model)

    # CASE UNION TYPE
    elif isinstance(route.response_model, UnionType):
        response_type = convert_to_typescript(route.response_model)

    ## CASE PYDANTIC BASEMODEL
    elif is_base_model:

        response_type = route.response_model.__name__

    ## CASE GENERIC JSON
    else:
        response_type = convert_to_typescript(route.response_model)

    if response_type is not None:
        input_dictionnary["response_type"] = response_type

    # PATH ARGUMENTS
    # --------------------------------
    path_arguments: list[tuple[str, type]] = get_path_arguments(route=route)
    if len(path_arguments) >= 1:
        input_dictionnary["path_arguments"] = [
            (argument_name, convert_to_typescript(input_type=argument_type))
            for argument_name, argument_type in path_arguments
        ]

    # QUERY
    # --------------------------------
    query_arguments: list[tuple[str, type]] = get_query_arguments(route=route)

    if len(query_arguments) >= 1:
        input_dictionnary["query_arguments"] = [
            (argument_name, convert_to_typescript(input_type=argument_type))
            for argument_name, argument_type in query_arguments
        ]

        # add query function
        def _get_query_string(query_arguments: list[tuple[str, type]]) -> str:
            return ", ".join(
                [
                    f"{argument_name}: {argument_name}"
                    for argument_name, argument_type in query_arguments
                ]
            )

        input_dictionnary["_get_query_string"] = _get_query_string

    # BODY
    # --------------------------------

    body_arguments: list[tuple[str, type]] = get_body_arguments(route=route)

    if len(body_arguments) >= 1:
        input_dictionnary["body_arguments"] = [
            (argument_name, convert_to_typescript(argument_type))
            for argument_name, argument_type in body_arguments
        ]

        # ADD BODY ARGUMENTS DECLARATION
        def _get_body_arguments_declaration(
            body_arguments: list[tuple[str, type]]
        ) -> str:

            body_declaration: str

            number_of_body_arguments: int = len(body_arguments)

            # SINGLE_ARGUMENT_BODY_IS_BASE_MODEL
            single_argument_body_is_base_model: bool

            if number_of_body_arguments > 1:
                single_argument_body_is_base_model = False
            else:
                argument_type: type = body_arguments[0][1]
                try:
                    single_argument_body_is_base_model = issubclass(
                        argument_type, BaseModel
                    )
                except TypeError:
                    single_argument_body_is_base_model = False

            # SINGLE ARGUMENT IS GENERIC ALIAS
            single_argument_body_is_generic_alias: bool
            if number_of_body_arguments > 1:
                single_argument_body_is_generic_alias = False
            else:
                argument_type: type = body_arguments[0][1]
                try:
                    single_argument_body_is_generic_alias = isinstance(
                        argument_type, GenericAlias
                    )
                except TypeError:
                    single_argument_body_is_generic_alias = False

            # CASE ONE ARGUMENT AND BASE MODEL
            # in that case fast api and api/server are expecting the base model directly and not wrapped in
            # a bigger object
            if single_argument_body_is_base_model:
                logging.debug("CASE ONE ARGUMENT AND BASE MODEL")
                argument_type: type = body_arguments[0][1]
                body_declaration = convert_to_typescript(argument_type)  # type: ignore
                # => because input_model cannot be None in this case

            # CASE ONE ARGUMENT AND GENERIC ALIAS
            elif single_argument_body_is_generic_alias:
                logging.debug("CASE ONE ARGUMENT AND GENERIC ALIAS")
                body_declaration = convert_to_typescript(body_arguments[0][1])

            # CASE OTHER SINGLE BODY ARGUMENTS CASE
            elif number_of_body_arguments == 1:
                logging.debug("CASE OTHER SINGLE BODY ARGUMENTS CASE")
                body_declaration = convert_to_typescript(body_arguments[0][1])

            # REGULAR CASES
            else:
                logging.debug("REGULAR CASES")
                body_declaration = (
                    "{ "
                    + ", ".join(
                        [
                            f"{argument_name}: {convert_to_typescript(argument_type)}"  # Type declartion
                            for argument_name, argument_type in body_arguments
                        ]
                    )
                    + " }"
                )

            logging.debug({"body_declaration": body_declaration})

            return body_declaration

        input_dictionnary["body_arguments_declaration"] = (
            _get_body_arguments_declaration(body_arguments=body_arguments)
        )

        # ADD BODY ARGUMENTS DECLARATION
        def _get_body_arguments_definition(
            body_arguments: list[tuple[str, type]]
        ) -> str:

            body_definition: str
            number_of_body_arguments: int = len(body_arguments)

            if number_of_body_arguments == 1:
                argument_name: str = body_arguments[0][0]
                body_definition = f"{to_javascript_name(input_model.__name__)}.{argument_name}"  # type: ignore
                # => because input_model cannot be None in this case

            # REGULAR CASES
            else:

                body_definition = (
                    "{ "
                    + ", ".join(
                        [
                            f"{argument_name}: {to_javascript_name(input_model.__name__)}.{argument_name}"  # type: ignore
                            # => because input_model cannot be None in this case
                            for argument_name, argument_type in body_arguments
                        ]
                    )
                    + " }"
                )

            logging.debug({"body_definition": body_definition})

            return body_definition

        input_dictionnary["body_arguments_definition"] = _get_body_arguments_definition(
            body_arguments=body_arguments
        )

    # METHOD
    # --------------------------------
    input_dictionnary["method"] = method.upper()

    # API CALL
    # --------------------------------

    has_query_parameters: bool = len(get_query_arguments(route=route)) > 0
    input_dictionnary["has_query_parameters"] = has_query_parameters
    has_body_parameters: bool = len(get_body_arguments(route=route)) > 0
    input_dictionnary["has_body_parameters"] = has_body_parameters

    # ASYNC DATA
    # --------------------------------

    async_data_item: str = (
        f"{typescript_composable_name}Data_{generate_random_string().lower()}"
    )

    input_dictionnary["async_data_item"] = async_data_item
    # RENDER
    # --------------------------------
    return COMPOSABLE_FUNCTION_TEMPLATE.render(input_dictionnary)


# ========================================
# ROUTE FUNCTION
# ========================================
def _get_route_path(route: APIRoute) -> str:
    """
    Get the display path of the route.

    Args:
        route (APIRoute): The route to get the path from.
    Returns:
        str :
            The display path of the route :
            - no `{` or `}`
            - no `:path`
    """
    return route.path.replace("{", "${").replace(":path", "")


# ========================================
# WATER MARK
# ========================================


def _get_watermark() -> str:
    """
    Get the watermark
    Returns:
        str:
            The watermark
    """
    # Get the Path of the current script
    script_path = Path(__file__).resolve()

    # Get the directory containing the script
    script_dir = script_path.parent

    config: dict = load_config(folder_path=script_dir)

    random_water_mark = config["RANDOM_WATER_MARK"]

    return random_water_mark


# ========================================
# RUN TIME CONFIG
# ========================================


def get_runtime_config_variable_name(app_title: str) -> str:
    """
    Generate the runetime config variable name from the server path

    Args:
        app_title (str): The app title

    Returns:
        str: The name of the variable
    """

    return to_javascript_name(app_title + "BaseUrl")
