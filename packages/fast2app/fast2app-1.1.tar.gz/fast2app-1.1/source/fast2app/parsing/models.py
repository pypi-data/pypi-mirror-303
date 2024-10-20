# ========================================
# RESPONSABILITIES
# ========================================
"""
Provides the functions to parse all return pydantic models from an FastApi app
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


from enum import Enum
import inspect
import logging
from types import GenericAlias, UnionType
import typing
from fast2app.utils import to_python_class_name
from fastapi import FastAPI
from fastapi.routing import APIRoute
from pydantic import BaseModel, create_model

# MODULE LIBRARIES
# ========================================

from fast2app.parsing.routes import (
    get_api_routes,
    get_route_arguments,
    get_body_arguments,
    get_query_arguments,
)

# FUNCTIONS
# ========================================


def parse_models(app: FastAPI) -> set[type[BaseModel]]:
    """
    Parse all pydantic `BaseModel` used by the `FastAPI` app

    Args:
        app (FastAPI): The `FastApi` app to process

    Returns:
        set[type[BaseModel]]: The set of all `BaseModel` used by the app
    """

    base_model_set: set[type[BaseModel]] = set()
    "The set of all `BaseModel` type in the app"

    api_routes = get_api_routes(app=app)

    for route in api_routes:

        # Response model
        base_model_set = base_model_set.union(parse_response_models(route=route))

        # Body Model
        base_model_set = base_model_set.union(parse_body_models(route=route))

    return base_model_set


def generate_input_models(app: FastAPI) -> set[type[BaseModel]]:
    """
    Generate input model for each route

    Args:
        app (FastAPI): The `FastApi` app to process
    """
    input_model_set: set[type[BaseModel]] = set()
    "The set of all `BaseModel` type in the app"

    api_routes = get_api_routes(app=app)

    for route in api_routes:

        # Body Model
        input_model = get_route_input_model(route=route)
        if input_model is not None:
            input_model_set.add(input_model)

    return input_model_set


def parse_query_types(route: APIRoute) -> set[type]:
    """
    Returns the `BaseModel`s that a given route has as a response
    """
    logging.info(f"Retrieving route query types from `{route.name}`")

    model_set: set[type] = set()

    query_arguments = get_query_arguments(route=route)

    for argument_name, argument_type in query_arguments:
        model_set.update(parse_types(argument_type, [BaseModel, Enum]))

    return model_set


def parse_response_models(route: APIRoute) -> set[type[BaseModel]]:
    """
    Returns the `BaseModel`s that a given route has as a response

    Args:
        route (APIRoute): the route to process

    Returns:
        set[type[BaseModel]]: the set of `BaseModel` return types
    """
    logging.info(f"Retrieving route response models from `{route.name}`")
    logging.debug({"route.response_model": route.response_model})
    logging.debug({"route.responses": route.responses})

    response_model_list: list[type | GenericAlias | None] = [route.response_model]

    for response_details in route.responses.values():
        if response_details.get("model") is not None:
            response_model_list.append(response_details.get("model"))

    logging.debug({"response_model_list": response_model_list})
    base_model_set: set[type[BaseModel]] = set()

    for response_model in response_model_list:
        base_model_set.update(parse_base_models(type_=response_model))

    logging.debug({"base_model_set": base_model_set})
    return base_model_set


def parse_body_models(route: APIRoute) -> set[type[BaseModel]]:
    """
    Returns the `BaseModel`s that a given route uses in its body

    Args:
        route (APIRoute): the route to process

    Returns:
        set[type[BaseModel]]: the set of `BaseModel` return types
    """
    base_model_set: set[type[BaseModel]] = set()

    body_arguments = get_body_arguments(route=route)

    for argument_name, argument_type in body_arguments:
        base_model_set.update(parse_base_models(type_=argument_type))

    return base_model_set


def parse_base_models(type_: type | GenericAlias | None) -> set[type[BaseModel]]:
    """
    Recursively returns all BaseModel from a given type

    Args:
        type_ (type | GenericAlias | None): The type to evaluate

    Raises:
        ValueError:
            If the type is a BaseModel starting with Body.
             This is  the same pattern that models created by FastApi and
             is not supported

    Returns:
        set[type[BaseModel]]: The set of all BaseModel
    """
    logging.info(f"Parsing base models from `{type_}` of class `{type_.__class__}`")

    base_model_set: set[type[BaseModel]] = set()

    if type_ is None:
        return base_model_set

    # CASE GENERIC ALIAS
    if isinstance(type_, GenericAlias) or isinstance(type_, UnionType) or isinstance(type_, typing._UnionGenericAlias):  # type: ignore
        base_model_set: set[type[BaseModel]] = set()

        for sub_type in type_.__args__:

            base_model_set.update(parse_base_models(type_=sub_type))

        return base_model_set

    # add type to set if type_ is not a body model created by FastApi
    if issubclass(type_, BaseModel) and (type_.__name__.startswith("Body")):

        error_message = (
            f"The type `{type_.__name__}` is not a valid response model because `. "
            "It starts with `Body, and has the same pattern that models created by FastApi."
            "This pattern is not supported."
            "Please use a different name for your model."
        )
        logging.error(error_message)
        raise ValueError(error_message)

    elif issubclass(type_, BaseModel):
        base_model_set.add(type_)
    else:
        return base_model_set

    for model_field in type_.model_fields.values():
        model = model_field.annotation
        base_model_set = base_model_set.union(parse_base_models(type_=model))

    return base_model_set


# def get_route_input_type(route: APIRoute) -> type | GenericAlias | None:
#     """
#     Returns the type of the first argument of a given route

#     Args:
#         route (APIRoute): the route to process
#     route_arguments (list[tuple[str, type | GenericAlias | None]]): the arguments of the route

#     Returns:
#         type | GenericAlias | None:
#             - `None` if the route does not have any input
#             - The input type of the route otherwise
#     """
#     logging.info(f"Retrieving route input type from `{route.name}`")

#     route_arguments = get_route_arguments(route=route)

#     logging.info({"route_arguments": route_arguments})

#     if len(route_arguments) == 0:
#         return None

#     elif len(route_arguments) == 1:
#         argument_name, argument_type, default = route_arguments[0]
#         return argument_type
#     else:
#         return _get_input_model_from_route(route=route)


def get_route_input_model(route: APIRoute) -> type[BaseModel] | None:
    """
    Returns the base model of a given route

    Args:
        route (APIRoute): the route to process

    Returns:
        type[BaseModel] | None:
            - `None` if the route does not have any input
            - The input model of the route otherwise
    """
    logging.info(f"Retrieving route base model from `{route.name}`")

    route_arguments = get_route_arguments(route=route)

    logging.info({"route_arguments": route_arguments})

    if len(route_arguments) == 0:
        return None

    return _get_input_model_from_route(route=route)


def parse_types(type_: type | None, types: list[type]) -> set[type]:
    """
    Returns the base model of a given route
    """
    model_set: set[type[BaseModel] | type[Enum]] = set()

    if type_ is None:
        return model_set

    # CASE GENERIC ALIAS
    if isinstance(type_, GenericAlias) or isinstance(type_, UnionType) or isinstance(type_, typing._UnionGenericAlias):  # type: ignore

        for sub_type in type_.__args__:

            for type_ in types:
                logging.debug({"sub_type": sub_type, "type_": type_})
                if inspect.isclass(type_) and issubclass(sub_type, type_):
                    model_set.add(sub_type)

    return model_set


# ========================================
# PRIVATE FUNCTIONS
# ========================================
def _get_input_model_from_route(route: APIRoute) -> type[BaseModel]:
    route_arguments = get_route_arguments(route=route)
    model_name = _get_input_model_name_from_route(route=route)

    route_model = create_model(
        model_name,
        **{
            argument_name: (
                argument_type,
                ... if default is inspect.Parameter.empty else default,
            )
            for argument_name, argument_type, default in route_arguments
        },  # type: ignore
    )

    return route_model


# def _get_input_model_from_generic_alias(
#     type_: GenericAlias,
# ) -> type[BaseModel] | None:
#     """
#     Returns the base model of a given generic alias
#     Args:
#         type_ (GenericAlias): the generic alias to process
#         Returns:
#         type[BaseModel] | None:
#             - `None` if the route does not have any input
#             - The input model of the route otherwise
#     """
#     logging.info(f"Retrieving route base model from `{type_}`")

#     for arg in type_.__args__:
#         if issubclass(arg, BaseModel):
#             return arg
#         if isinstance(arg, GenericAlias):
#             return _get_input_model_from_generic_alias(type_=arg)


def _get_input_model_name_from_route(route: APIRoute) -> str:
    """
    Returns the name of the model from a given route

    Args:
        route (APIRoute): the route to process

    Examples:
        route_name = get_object
        model_name = GetObjectInputModel
    Returns:
        str: the name of the model
    """
    route_name = route.name
    model_name = to_python_class_name(f"{route_name}InputModel")
    logging.debug({"route_name": route_name, "model_name": model_name})
    return model_name
