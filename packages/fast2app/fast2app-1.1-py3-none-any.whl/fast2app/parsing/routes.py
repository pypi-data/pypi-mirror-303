# ========================================
# RESPONSABILITIES
# ========================================
"""
Provides the functions to retrieve `APIRoute` from an app
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


import inspect
import logging
from typing import Any
from fastapi import FastAPI
from fastapi.routing import APIRoute
import regex

# MODULE LIBRARIES
# ========================================


# ========================================
# FUNCTIONS
# ========================================


def get_api_routes(app: FastAPI) -> list[APIRoute]:
    """
    Returns the `APIRoute` from an app

    Args:
        app (FastAPI): the app to process

    Returns:
        list[APIRoute]: The list of routes
    """
    return [route for route in app.routes if isinstance(route, APIRoute)]


def get_route_arguments(route: APIRoute) -> list[tuple[str, type, Any]]:
    """
    Returns the arguments of the endpoint of the route
    Args:
        route (APIRoute): The route to process
    Returns:
        list[tuple[str, type, Any]]: the (<argument name>, <argument type>, <default value>) of the endpoint
    """
    signature = inspect.signature(route.endpoint)
    route_arguments = [
        (
            param.name,
            param.annotation if param.annotation != inspect.Parameter.empty else Any,
            param.default,
        )
        for param in signature.parameters.values()
        if param.name != "return"
    ]
    logging.debug({"route_arguments": route_arguments})
    return route_arguments  # type: ignore


def get_path_arguments(route: APIRoute) -> list[tuple[str, type]]:
    """
    Returns the arguments of the endpoint that are defined in the path

    Args:
        route (APIRoute): The route to process

    Returns:
        list[tuple[str, type]]: the (<argument name>,<argument type>) that are defined in the path
    """

    path_arguments = [
        (model_field.name, model_field.field_info.annotation)
        for model_field in route.dependant.path_params
        if model_field.field_info.annotation is not None
        # if argument_name not in path_argument_names
        # and not issubclass(argument_type, BaseModel)
    ]
    path_arguments.sort(key=lambda x: x[0])
    logging.debug(
        {
            "path_arguments": path_arguments,
        }
    )

    return path_arguments


def get_query_arguments(route: APIRoute) -> list[tuple[str, type]]:
    """
    Returns the arguments of the endpoint that are not defined in the path and
    must be defined in the query

    Args:
        route (APIRoute): The route to process

    Returns:
        list[tuple[str, type]]: the (<argument name>,<argument type>) that are not defined in the path
    """
    path_argument_names: list[str] = _get_path_argument_names(route=route)

    query_arguments = [
        (model_field.name, model_field.field_info.annotation)
        for model_field in route.dependant.query_params
        if model_field.field_info.annotation is not None
        # if argument_name not in path_argument_names
        # and not issubclass(argument_type, BaseModel)
    ]
    query_arguments.sort(key=lambda x: x[0])
    logging.debug(
        {
            "path_argument_names": path_argument_names,
            "query_arguments": query_arguments,
        }
    )

    return query_arguments


def get_body_arguments(route: APIRoute) -> list[tuple[str, type]]:
    """
    Returns the arguments of the endpoint that are BaseModels

    Args:
        route (APIRoute): The route to process

    Returns:
        list[tuple[str, type]]: the (<argument name>,<argument type>) that are BaseModel
    """

    body_arguments = [
        (model_field.name, model_field.field_info.annotation)
        for model_field in route.dependant.body_params
        if model_field.field_info.annotation is not None
        # if argument_name not in body_argument_names
        # and not issubclass(argument_type, BaseModel)
    ]
    body_arguments.sort(key=lambda x: x[0])
    logging.debug(
        {
            "body_arguments": body_arguments,
        }
    )

    return body_arguments


# ========================================
# PRIVATE FUNCTIONS
# ========================================
def _get_path_argument_names(route: APIRoute) -> list[str]:
    """
    Returns the arguments of the endpoint that are defined in the path

    Args:
        route (APIRoute): The route to process

    Returns:
        list[str]: The list of arguments defined in the path
    """
    route_parameter_names_with_brackets: list[str] = regex.findall(
        r"\{.*?\}", route.path
    )

    def filter_name(name: str) -> str:
        return_value: str = (
            name.removeprefix("{").removesuffix("}").replace(":path", "")
        )

        return return_value

    route_parameter_names: list[str] = [
        filter_name(argument_name)
        for argument_name in route_parameter_names_with_brackets
    ]

    return route_parameter_names
