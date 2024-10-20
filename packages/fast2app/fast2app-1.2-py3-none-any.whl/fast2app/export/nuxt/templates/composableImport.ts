// IMPORTS
// ==============================================================

// TYPES
{% if model_string -%}
import type { {{ model_string }} } from "~/types/fastapi";
{% else -%}
// No imports requiered
{% endif -%}
