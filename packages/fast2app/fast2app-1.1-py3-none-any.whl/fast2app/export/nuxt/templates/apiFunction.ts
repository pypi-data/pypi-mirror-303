// FUNCTION
// ==============================================================


{% if response_type -%}
export default defineEventHandler(async (event): Promise<{{ response_type }}> => {
{% else -%}
export default defineEventHandler(async (event) => {
{% endif %}

// PATH ARGUMENTS
// ======================================
{% if path_arguments -%}
{% for argument_name, argument_type in path_arguments %}
const {{argument_name}}: {{argument_type}} | undefined = getRouterParam(event, '{{argument_name}}')
{% endfor %}
{% else -%}
// no path arguments
{% endif %}

// URL
// ======================================
const runtimeConfig = useRuntimeConfig();
const requestURL = `${runtimeConfig.{{backend_url}}}{{ route }}`;
console.debug("backend url :", `${runtimeConfig.{{backend_url}}}`);
console.info("requesting to FastAPI Backend:", requestURL);

// QUERY
// ======================================
{% if query_arguments -%}
// retrieve query
const query = getQuery(event)

//retrieve arguments
{% for argument_name, argument_type in query_arguments %}
const {{argument_name}}: {{argument_type}} = query.{{argument_name}} as {{argument_type}};
{% endfor %}

// declare parmas
const params: Record<string, any> = { {{_get_query_string(query_arguments)}} }
console.debug("params :", params);
{% else -%}
// no query arguments
{% endif %}


// BODY
// ======================================
{% if body_arguments -%}
const body = await readBody(event)
console.debug("body :", body);
{% else -%}
// no body arguments
{% endif %}

// FETCH
// ======================================
{% if response_type -%}
const response: {{ response_type }} = await $fetch(
{% else -%}
const response = await $fetch(
{% endif %}
    requestURL,
    {
      method: "{{method}}",
      headers: { "Content-Type": "application/json" },
      {% if query_arguments -%}
      params: params,
      {% endif %}
      {% if body_arguments -%}
      body: JSON.stringify(body),
      {% endif %}
    }
  );
  console.debug("FastAPI response :", response);
  return response;
});
