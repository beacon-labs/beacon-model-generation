TEMPLATE = """
/*
 * {{ h.get_prefixed_name(name) }}
 * ------------------------------
 * {{ description }}
 */

#include "{{ h.get_header_filename(name) }}"

{% for attribute in attributes: %}
    {{ h.get_attribute_type(attribute) }} {{ h.get_prefixed_name(name) }}::get_{{ attribute["name"] }}()
    {
        return this->{{ attribute["name"] }};
    }

    {% if not attribute.get("list", False): -%}
        void {{ h.get_prefixed_name(name) }}::set_{{ attribute["name"] }}({{ h.get_attribute_type(attribute) }} value)
        {
            this->{{ attribute["name"] }} = value;
        }
    {% else %}
        void {{ h.get_prefixed_name(name) }}::add_{{ h.get_singular_attribute_name(attribute) }}({{ h.get_attribute_type_without_list(attribute) }} value)
        {
            this->{{ attribute["name"] }}.push_back( value );
        }
    {% endif %}
{% endfor %}
"""