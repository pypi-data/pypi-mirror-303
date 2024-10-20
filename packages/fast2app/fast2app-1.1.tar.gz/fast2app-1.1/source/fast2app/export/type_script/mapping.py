# ========================================
# RESPONSABILITIES
# ========================================
"""
Provides the mapping between python types and typescript types.
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
from typing import Dict


# MODULE LIBRARIES
# ========================================

# ========================================
# CLASS
# ========================================


TYPE_MAP: Dict[str, str] = {
    "bool": "boolean",
    "str": "string",
    "int": "number",
    "float": "number",
    "complex": "number",
    "Any": "any",
    "Dict": "Record<any, any>",
    "List": "Array<any>",
    "Tuple": "[any]",
    "dict": "Record<any, any>",
    "list": "Array<any>",
    "tuple": "[any]",
    "Union": "any",
    "None": "null",
    "NoneType": "null",
}


SUBSCRIPT_FORMAT_MAP: Dict[str, str] = {
    "Dict": "Record<%s>",
    "List": "Array<%s>",
    "Optional": "%s | null",
    "Tuple": "[%s]",
    "Union": "%s",
    "dict": "Record<%s>",
    "list": "Array<%s>",
    "tuple": "[%s]",
}
