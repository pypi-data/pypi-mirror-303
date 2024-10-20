# ========================================
# RESPONSABILITIES
# ========================================
"""
Provides functions that allow to parse pydantic `BaseModel` from a `FastAPI` app
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
from fast2app.parsing.routes import (
    get_api_routes,  # noqa: F401
    get_route_arguments,  # noqa: F401
    get_path_arguments,  # noqa: F401
    get_query_arguments,  # noqa: F401
    get_body_arguments,  # noqa: F401
)


from fast2app.parsing.models import (
    parse_models,  # noqa: F401
    generate_input_models,  # noqa: F401
    parse_query_types,  # noqa: F401
    parse_response_models,  # noqa: F401
    parse_body_models,  # noqa: F401
    get_route_input_model,  # noqa: F401
    parse_types,  # noqa: F401
)  # noqa: F401

from fast2app.parsing.validity_checks import (
    FastApiValidityCheck,  # noqa: F401
    check_fast_api_validity,  # noqa: F401
)
