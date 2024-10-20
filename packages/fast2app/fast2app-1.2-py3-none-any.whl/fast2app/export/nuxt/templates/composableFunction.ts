// FUNCTION
// ==============================================================

{% if input_type_declaration -%}
export default async function {{ typescript_composable_name }}({{ input_type_declaration }}): Promise<{{ response_type }}> {
{% else -%}
export default async function {{ typescript_composable_name }}(): Promise<{{ response_type }}> {
{% endif -%}

{% if input_type_name -%}
console.debug("{{ input_type_name }} :", {{ input_type_name }});
{% endif %}

// BODY ARGUMENTS
// ======================================
{% if body_arguments -%}
const body: {{ body_arguments_declaration }} = {{ body_arguments_definition }}
console.debug("body :", body);
{% else -%}
// no body arguments
{% endif %}


// QUERY ARGUMENTS
// ======================================
{% if query_arguments -%}
//retrieve arguments
{% for argument_name, argument_type in query_arguments %}
const {{argument_name}}: {{argument_type}} = {{ input_type_name }}.{{argument_name}} as {{argument_type}};
{% endfor %}

// declare params
const params: Record<string, any> = { {{_get_query_string(query_arguments)}} }
console.debug("params :", params);
{% else -%}
// no query arguments
{% endif %}


// PATH ARGUMENTS
// ======================================
{% if path_arguments -%}
//retrieve arguments
{% for argument_name, argument_type in path_arguments %}
const {{argument_name}}: {{argument_type}} = {{ input_type_name }}.{{argument_name}}
{% endfor %}
{% else -%}
// no path arguments
{% endif %}

// URL
// ======================================
const requestURL = `/api/{{ app_name_url }}{{ route }}`;

console.debug("requesting to SSR:", requestURL);

// API CALL
// ======================================
// The async data variabale has a random suffix to not interfere with the useAsyncData cache
const { data, error } = await useAsyncData('{{ async_data_item }}', () => $fetch<{{ response_type }}>(requestURL, {
    method: "{{ method }}",
    {% if has_query_parameters -%}
    params: params,
    {% endif -%}
    {% if has_body_parameters -%}
    body: JSON.stringify(body),
    {% endif -%}
  })
);

console.debug("data :", data);

// RETURN VALUE
// ======================================
{% if response_type == "void" -%}
// This composable function is not returning anything
{% else -%}
  if (error.value) {
    console.error("error :", error.value);
    throw error.value;
  } else if (data.value === null) {
    const error = new Error("No returned data");
    throw error;
  } else {
    return data.value;
  }
{% endif -%}
};