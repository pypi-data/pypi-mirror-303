# ========================================
# RESPONSABILITIES
# ========================================
"""
The functions to allow the export a pydantics `BaseModel` list to typescript interfaces
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
from copy import deepcopy
import json
import logging
import shutil
from typing import Tuple
from pydantic import BaseModel
from pathlib import Path
import os
from tempfile import mkdtemp
import re
from pydantic2ts.cli.script import (
    generate_json_schema_v2,
    generate_json_schema_v1,
)
from pydantic import VERSION

V2 = True if VERSION.startswith("2") else False
"Whether the pydantic version is 2 or not"


# MODULE LIBRARIES
# ========================================


# ========================================
# FUNCTIONS
# ========================================


def generate_interfaces(model_classes: set[type[BaseModel]], export_path: Path) -> None:
    """
    Generates Typescript interafaces from the provided `BaseModel`s classes.

    Note :
        Nothing is generated if the model classes set is empty

    This function utilizes the
    pydantic-to-typescript2 (https://github.com/Darius-Labs/pydantic-to-typescript2) library.

    Args:
        model_classes (set[type[BaseModel]): The list of `BaseModel` class to convert
        export_path (Path): The export destination folder
    """

    if len(model_classes) == 0:
        return

    _generate_typescript_defs(model_classes=model_classes, output=export_path)


# ========================================
# PRIVATE FUNCTIONS
# ========================================


def _generate_typescript_defs(
    model_classes: set[type[BaseModel]],
    output: Path,
    exclude: Tuple[str] = (),  # type: ignore
    # json2ts_cmd: str = "json2ts",
) -> None:
    """
    Convert the pydantic models in a python module into typescript interfaces.

    This function replaces the one from pydantic-to-typescript2 in order to directly use the set of `BaseModel`

    Args:
        model_classes (set[type[BaseModel] ]):
            The pydantic `BaseModel` to convert

        output (str):
            file in which the typescript definitions will be written to

        exclude (Tuple[str], optional):
            The command that will execute json2ts. Provide this if the executable is not
            discoverable or if it's locally installed (ex: 'yarn json2ts').
            Defaults to ().

    Raises:
        Exception: If `json2ts` is not installed
        RuntimeError: If `json2ts` exited with an error
    """

    # json2ts_cmd test
    # if " " not in json2ts_cmd and not shutil.which(json2ts_cmd):
    #     raise Exception(
    #         "json2ts must be installed. Instructions can be found here: "
    #         "https://www.npmjs.com/package/json-schema-to-typescript"
    #     )

    # quicktype_cmd test
    quicktype_cmd = "quicktype"
    if " " not in quicktype_cmd and not shutil.which(quicktype_cmd):
        raise Exception(
            "quicktype must be installed. Instructions can be found here: "
            "https://github.com/quicktype/quicktype#installation\n"
            "You can install it using: npm install -g quicktype"
        )

    logging.info("Finding pydantic models...")

    models = [m for m in model_classes if issubclass(m, BaseModel)]

    if exclude:
        models = [m for m in models if m.__name__ not in exclude]

    logging.info("Generating JSON schema from pydantic models...")

    raw_schema = (
        generate_json_schema_v2(models) if V2 else generate_json_schema_v1(models)
    )
    logging.warning({"raw schema as dictionnary": json.loads(raw_schema)})

    schema_dictionnary = _flatten_schema(json.loads(raw_schema))
    # schema_dictionnary = json.loads(raw_schema)
    # schema_dictionnary.pop("required")

    logging.warning({"schema as dictionnary": schema_dictionnary})

    schema = json.dumps(schema_dictionnary, indent=2)

    schema_dir = mkdtemp()
    schema_output = os.path.join(schema_dir, "schema.json")
    temp_output = os.path.join(schema_dir, "fastapi.d.ts")

    logging.debug(f"{schema =}")

    with open(schema_output, "w") as f:
        f.write(schema)

    logging.info("Converting JSON schema to typescript definitions...")

    logging.debug(f"{output =}")

    ## create folder if not exists
    output.parent.mkdir(parents=True, exist_ok=True)

    # with open(temp_output.as_posix(), "w") as fp:
    #     fp.write("")

    # to_typescript_command = (
    #     rf'{json2ts_cmd} -i "{schema_output}" -o "{temp_output}" --bannerComment ""'
    # )

    to_typescript_command = f"quicktype --lang typescript --src-lang schema --no-runtime-typecheck   --src {schema_output} -o {temp_output}  "

    json2ts_exit_code = os.system(to_typescript_command)

    if json2ts_exit_code == 0:
        # clean_output_file(output.as_posix())
        logging.info(f"Saved typescript definitions to {output}.")
    else:
        raise RuntimeError(
            f'"{to_typescript_command}" failed with exit code {json2ts_exit_code}.'
        )

    # CONVERT TO ENUM
    with open(temp_output, "r") as file:
        temp_file = file.read()

    cleaned_content = _clean_content(content=temp_file)

    with open(output, "w") as file:
        # file.write(enum_content)
        file.write(cleaned_content)

    # clean_output_file(output_filename=output.as_posix())

    shutil.rmtree(schema_dir)


def _clean_content(content: str) -> str:
    # Use regex to replace the last occurrence of 'Class'
    modified_content = re.sub(r"\b(\w+)Class\b", r"\1", content)

    return modified_content


# def _replace_union_with_enum(content: str) -> str:
#     """
#     Replace union types with enums in the provided typescript content.

#     Args:
#         content (str): The typescript content to modify

#     Returns:
#         str: The modified typescript content with union types replaced by enums
#     """
#     pattern = re.compile(
#         r'export type (\w+) = ((?:\d+|\d*\.\d+|"[^"]+")(?: \| (?:\d+|\d*\.\d+|"[^"]+"))*)\s*;'
#     )

#     def replace_match(match):

#         type_name = match.group(1)
#         values_str = match.group(2)
#         values = [v.strip('"') for v in values_str.split(" | ")]
#         enum_content = _create_enum_content(type_name, values)
#         return enum_content

#     # Replace union types with enums
#     new_content = pattern.sub(replace_match, content)
#     return new_content


# def _create_enum_content(type_name: str, values: list[str]) -> str:
#     """
#     Create the content for an enum in typescript.

#     Args:
#         type_name (str): The type name to process
#         values (list[str]): The list of the enum values

#     Returns:
#         str: The string content for the enum in typescript
#     """

#     enum_name = type_name

#     def is_number(value: str) -> bool:
#         try:
#             float(value)
#             return True
#         except ValueError:
#             return False

#     def get_key(value: str) -> str:

#         if is_number(value):
#             return_value: str = f"NUMBER_{value}"
#             return_value = return_value.replace(".", "_")
#             return return_value
#         else:
#             return value.upper().replace(" ", "_").replace(".", "_").replace("-", "_")

#     def get_value(value: str) -> str:
#         if is_number(value):
#             return str(value)
#         else:
#             return f'"{value}"'

#     enum_values = [f"{get_key(value)} = {get_value(value)}" for value in values]

#     enum_definition = ",\n  ".join(enum_values)

#     return f"export enum {enum_name} {{\n  { enum_definition} \n}}\n"


def _resolve_ref(schema, ref):
    parts = ref.split("/")
    current = schema
    for part in parts[1:]:  # Skip the first '#' part
        if part in current:
            current = current[part]
        else:
            raise ValueError(f"Invalid reference: {ref}")
    return current


def _flatten_schema(schema):
    flattened = deepcopy(schema)

    def recurse(obj):
        if isinstance(obj, dict):
            if "$ref" in obj:
                ref = obj["$ref"]
                resolved = _resolve_ref(schema, ref)
                obj.clear()
                obj.update(resolved)
                recurse(obj)
            else:
                for key, value in obj.items():
                    obj[key] = recurse(value)
        elif isinstance(obj, list):
            return [recurse(item) for item in obj]
        return obj

    return recurse(flattened)
