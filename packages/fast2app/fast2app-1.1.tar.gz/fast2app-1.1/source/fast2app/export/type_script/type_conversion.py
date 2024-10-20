# ========================================
# RESPONSABILITIES
# ========================================
"""
The function tha convert a python type or GenericAlias into a str represneting
the same type in Typescript
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
import logging
from types import GenericAlias, NoneType, UnionType
from typing import _SpecialGenericAlias, _SpecialForm, _UnionGenericAlias  # type: ignore
from astroid import parse, Subscript, NodeNG, Name, Tuple, BinOp, Attribute

# MODULE LIBRARIES
# ========================================
from fast2app.export.type_script.mapping import TYPE_MAP, SUBSCRIPT_FORMAT_MAP
from pydantic import BaseModel


# ========================================
# FUNCTIONS
# ========================================


def convert_to_typescript(
    input_type: (
        type
        | _SpecialGenericAlias
        | _SpecialForm
        | GenericAlias
        | _UnionGenericAlias
        | str
        | BaseModel
        | None
    ),
) -> str:
    """
    Converts a type into its TypesScript equivalent

    Raises :
        ValueError : if the input has an incorect type

    Args:
        input_type (type | _SpecialGenericAlias | _SpecialForm | GenericAlias): the type to convert

    Returns:
        str: The typescript conversion
    """
    if input_type is None:
        return "null"

    if isinstance(input_type, type) and issubclass(input_type, BaseModel):
        return input_type.__name__

    # INPUT STRING

    input_string: str = _parse_input_string(input_type=input_type)

    module = parse(input_string)

    node: NodeNG = module.body[0]

    return _parse_input(input_element=node.value)  # type: ignore


# ========================================
# PRIVATE FUNCTIONS
# ========================================


def _parse_input_string(
    input_type: type | _SpecialGenericAlias | _SpecialForm | GenericAlias | str,
) -> str:
    """Returns the type string to process

    Args:
        input_type (type | _SpecialGenericAlias | _SpecialForm | GenericAlias): The data to parse

    Returns:
        str: The input string
    """

    logging.info(f"input type {input_type} class is `{input_type.__class__}`")

    if isinstance(input_type, type):
        logging.debug(f"{input_type} is a `type`")
        input_string = input_type.__name__.replace("typing.", "")
        logging.debug(f"input_string as `type` : {input_string}")
        return input_string

    if isinstance(input_type, str):
        input_string = input_type.replace("typing.", "")
        logging.debug(f"input_string as `str` : {input_string}")
        return input_string

    if isinstance(input_type, GenericAlias):
        input_string = str(input_type).replace("typing.", "")
        logging.debug(f"input_string as `GenericAlias` : {input_string}")
        return input_string

    if isinstance(input_type, _UnionGenericAlias):
        input_string = str(input_type).replace("typing.", "")
        logging.debug(f"input_string as `_UnionGenericAlias` : {input_string}")
        return input_string

    if isinstance(input_type, UnionType):
        # raise BaseException(input_type)

        union_type_string = [
            _parse_input_string(input_type=element) for element in input_type.__args__
        ]

        input_string = " | ".join(union_type_string)
        logging.debug(f"input_string as `UnionType` : {input_string}")
        return input_string

    else:
        input_string = input_type.__name__.replace("typing.", "")  # type: ignore
        logging.debug(f"input_string as `other` : {input_string}")
        return input_string


def _parse_input(input_element: Subscript | Name | BinOp | NoneType) -> str:
    """
    Parses the input element into its typescript equivalent.

    Args:
        input_element (Subscript | Name | BinOp | NoneType): The element to parse

    Raises:
        ValueError: If the element is not convertible.

    Returns:
        str: The converrted element into typescript syntax
    """
    logging.debug(f"{input_element.__class__ =}")
    logging.debug(f"{input_element =}")

    if isinstance(input_element, NoneType):
        return "null"

    elif isinstance(input_element, Name):

        core_type = _map_core_type(input_string=input_element.name)

        if core_type is not None:
            return core_type

        else:

            return input_element.name

    elif isinstance(input_element, BinOp) and input_element.op == "|":
        children_map: list[str] = [
            _parse_input(child) for child in input_element.get_children()  # type: ignore
        ]

        return " | ".join(children_map)

    elif isinstance(input_element, Attribute):
        logging.info({"input_element Attribute": input_element.repr_name()})
        return input_element.repr_name()

    elif not hasattr(input_element, "slice"):
        return _parse_input(input_element.value)  # type: ignore

    else:
        root_type_as_string: str = input_element.value.name  # type: ignore

        root_string = _map_root_name(root_name=root_type_as_string)

        logging.debug(f"{root_type_as_string =}")
        logging.debug(f"{root_string =}")

        logging.debug(f"{input_element.slice =}")  # type: ignore

        if root_string is None:
            error_message = (
                f"root_type_as_string `{root_type_as_string}` is not mappable"
            )
            logging.error(error_message)
            raise ValueError(error_message)

        if root_type_as_string == "Union":
            return_separator = " | "
        else:
            return_separator = ", "

        logging.debug(f"{return_separator =}")

        if isinstance(input_element.slice, Name):  # type: ignore
            child_string = _map_core_type(input_element.slice.name)  # type: ignore

        elif isinstance(input_element.slice, Subscript):  # type: ignore
            child_string = _parse_input(input_element.slice)  # type: ignore

        elif isinstance(input_element.slice, BinOp):  # type: ignore
            child_string = _parse_input(input_element.slice)  # type: ignore

        elif isinstance(input_element.slice, Tuple):  # type: ignore

            children_map: list[str] = [
                _parse_input(node) for node in input_element.slice.elts  # type: ignore
            ]

            logging.debug(f"{children_map =}")

            child_string = return_separator.join(children_map)

        elif isinstance(input_element.slice, Attribute):  # type: ignore
            child_string = _parse_input(input_element.slice)  # type: ignore

        return root_string % (child_string,)


def _map_root_name(root_name: str) -> str | None:
    """
    Returns the TypeScript mapping if the input_string matches a mapped type

    Args:
        root_name (str): The root name to look up

    Returns:
        str | None:
            A `str` with a % in it if the input_string is mapped as a core type
            `None` otherwise.
    """
    return SUBSCRIPT_FORMAT_MAP.get(root_name)


def _map_core_type(input_string: str) -> str | None:
    """
    Returns the TypeScript mapping if the input_string matches a mapped type

    Args:
        input_string (str): THe string to map

    Returns:
        str|None:
            A `str` if the input_string is mapped as a core type
            `None` otherwise.
    """

    return TYPE_MAP.get(input_string)
