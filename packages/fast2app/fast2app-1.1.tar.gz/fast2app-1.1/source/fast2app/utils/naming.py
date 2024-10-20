# ========================================
# RESPONSABILITIES
# ========================================
"""
This module contains the functions to rename object in this package.
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
import random
import string
from camel_converter import to_camel, to_pascal, to_snake  # noqa: F401

# MODULE LIBRARIES
# ========================================


# ========================================
# TO PYTHON FUNCTIONS
# ========================================


def to_python_name(string: str) -> str:
    """
    This function converts a string to a python name.
    aka:
    - snake_case
    - no double underscores
    - no spaces
    - no dots

    Args:
        string (str): The string to convert.

    Returns:
        str: The converted string.

    Examples:
        to_python_name("Hello World")
        'hello_world'

        to_python_name("Hello _world")
        'hello_world'

    """

    snake_string: str
    # to snake
    first_character = string[0]
    if first_character in ["_", "-"]:

        snake_string = "_" + to_snake(string)
    else:
        snake_string = to_snake(string)

    logging.debug(f"snake_string: {snake_string}")

    # remove dots
    snake_string = snake_string.replace(".", "_")

    # remove space
    snake_string = snake_string.replace(" ", "_")
    logging.debug(f"no space: {snake_string}")

    # replace dashes
    snake_string = snake_string.replace("-", "_")
    logging.debug(f"no dashes: {snake_string}")

    # remove double underscores
    while "__" in snake_string:
        snake_string = snake_string.replace("__", "_")

    logging.debug(f"no double underscores: {snake_string}")
    return snake_string


def to_python_class_name(string: str) -> str:
    """
    This function converts a string to a python class name.
    aka:
    - PascalCase
    - no underscores
    - no dashes
    - no spaces
    - no dots

    Args:
        string (str): The string to convert.
    Returns:
        str: The converted string.

    Examples:
        to_python_class_name("hello world")
        'HelloWorld'
    """

    python_class_string: str = string

    # no dots
    python_class_string = string.replace(".", "_")
    logging.debug(f"no dots: {python_class_string}")

    # no dashes
    python_class_string = python_class_string.replace("-", "_")
    logging.debug(f"no dashes: {python_class_string}")

    # no spaces
    python_class_string = python_class_string.replace(" ", "_")
    logging.debug(f"no spaces: {python_class_string}")

    # to pascal
    python_class_string = to_pascal(to_snake(python_class_string))

    logging.debug(f"to pascal: {python_class_string}")

    return python_class_string


# ========================================
# TO JAVASCRIPT FUNCTIONS
# ========================================


def to_javascript_name(string: str) -> str:
    """
    This function converts a string to a javascript name.
    aka:
    - camelCase
    - no double underscores
    - no dashes
    - no spaces
    - no dots

    Args:
        string (str): The string to convert.
    Returns:
        str: The converted string.

    Examples:
        to_javascript_name("hello world")
        'helloWorld'
    """
    javascript_name: str = string

    # no dots
    javascript_name = javascript_name.replace(".", "_")
    logging.debug(f"no dots: {javascript_name}")

    # no spaces
    javascript_name = javascript_name.replace(" ", "_")
    logging.debug(f"no spaces: {javascript_name}")

    # no dashes
    javascript_name = javascript_name.replace("-", "_")
    logging.debug(f"no dashes: {javascript_name}")

    # to camel
    javascript_name = to_camel(to_snake(javascript_name))

    return javascript_name


def to_javascript_type_name(string: str) -> str:
    """
    This function converts a string to a javascript class name.
    aka:
    - PascalCase
    - no underscores
    - no dashes
    - no spaces
    - no dots

    Args:
        string (str): The string to convert.
    Returns:
        str: The converted string.

    Examples:
        to_javascript_type_name("hello world")
        'HelloWorld'
    """
    javascript_class_name: str = string

    # no dots
    javascript_class_name = javascript_class_name.replace(".", "_")
    logging.debug(f"no dots: {javascript_class_name}")

    # no dashes
    javascript_class_name = javascript_class_name.replace("-", "_")
    logging.debug(f"no dashes: {javascript_class_name}")

    # no spaces
    javascript_class_name = javascript_class_name.replace(" ", "_")
    logging.debug(f"no spaces: {javascript_class_name}")

    # to pascal
    javascript_class_name = to_pascal(to_snake(javascript_class_name))

    return javascript_class_name


# ========================================
# URL FUNCTIONS
# ========================================


def to_url(string: str) -> str:
    """
    This function converts a string to a url name.
    aka:
    - kebab_case
    - no double underscores
    - no spaces
    - no dots

    Args:
        string (str): The string to convert.
    Returns:
        str: The converted string.

    Examples:
        to_url("hello world")
        'hello-world'
    """
    url_name: str = string

    # no spaces
    url_name = url_name.replace(" ", "_")
    logging.debug(f"no spaces: {url_name}")

    # no dots
    url_name = url_name.replace(".", "_")

    # to snake
    url_name = to_snake(url_name)
    logging.debug(f"to snake: {url_name}")

    # to kebab
    url_name = url_name.replace("_", "-")
    logging.debug(f"to kebab: {url_name}")

    # remove double dashes
    while "--" in url_name:
        url_name = url_name.replace("--", "-")

    return url_name


# ========================================
# STRING FUNCTIONS
# ========================================
def generate_random_string(length: int = 10):
    "Define the characters to use (letters, digits, and punctuation if needed)"
    characters = (
        string.ascii_letters + string.digits
    )  # + string.punctuation for special chars
    random_string = "".join(random.choice(characters) for _ in range(length))
    return random_string


# ========================================
# PRIVATE FUNCTIONS
# ========================================
