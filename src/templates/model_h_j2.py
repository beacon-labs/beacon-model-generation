TEMPLATE = """
/*
 * {{ h.get_prefixed_name(name) }}
 * ------------------------------
 * {{ description }}
 */

#pragma once

using namespace std;

#include <memory>
{% for include in h.get_setting("includes") -%}
    #include <{{ include }}>
{% endfor -%}
{% if h.has_a_list(name): -%}
    #include <list>
{% endif -%}
{% for include in h.get_model_includes(name) -%}
    #include "{{ include }}"
{% endfor %}
{% for forward in h.get_model_forwards(name) -%}
    class {{ forward }};
{% endfor %}
class {{ h.get_prefixed_name(name) }}
{
    {% for attribute in attributes: %}
        {{ h.get_attribute_type(attribute) }} {{ attribute["name"] }};
    {% endfor %}
    public:
        {% for attribute in attributes: %}
            {{ h.get_attribute_type(attribute) }} get_{{ attribute["name"] }}();
            {% if not attribute.get("list", False): %}
                void set_{{ attribute["name"] }}({{ h.get_attribute_type(attribute) }} value);
            {% else %}
                void add_{{ h.get_singular_attribute_name(attribute) }}({{ h.get_attribute_type_without_list(attribute) }} value);
            {% endif %}
        {% endfor %}

};

"""
