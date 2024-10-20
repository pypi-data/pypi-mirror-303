# ========================================
# RESPONSABILITIES
# ========================================
"""
This module contains helper functions to handle toml files.
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
from pathlib import Path
import toml


# ========================================
# CONFIGURATION
# ========================================
def load_config(folder_path: Path) -> dict:
    """
    Load configuration from a config.toml file in the specified folder.

    Args:
        folder_path (Path): Path to the folder containing the TOML file

    Raises:
        FileNotFoundError: If no config.toml file is found in the specified folder.
        ValueError: If the config.toml file is not valid TOML.


    Returns:
        dict: Configuration dictionary
    """
    config_path = folder_path / "config.toml"
    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file 'config.toml' not found in {folder_path}"
        )

    try:
        with open(config_path, "r") as config_file:
            return toml.load(config_file)
    except Exception as e:
        raise ValueError(f"Error loading configuration file: {str(e)}")
