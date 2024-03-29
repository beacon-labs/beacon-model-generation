TEMPLATE = """
/*
 * {{ h.get_prefixed_name(name) }}Base
 * ------------------------------
 * {{ description }}
 *
 * IMPORTANT NOTE: DO NOT EDIT THIS FILE, edit {{ h.get_header_filename(name) }} instead
 *
 */

#include "{{ h.get_header_filename(name+'Base') }}"

{% for attribute in attributes: %}
{{ h.get_attribute_type(attribute) }} {{ h.get_prefixed_name(name) }}Base::get_{{ attribute["name"] }}()
{
    return this->{{ attribute["name"] }};
}

void {{ h.get_prefixed_name(name) }}Base::observe_{{ attribute["name"] }}(shared_ptr<I{{ h.get_prefixed_name("Observer") }}<{{ h.get_attribute_type_without_list(attribute) }}>> observer)
{
    {{ attribute["name"] }}_observers.push_back( observer );
}

{% if not attribute.get("list", False): -%}
void {{ h.get_prefixed_name(name) }}Base::set_{{ attribute["name"] }}({{ h.get_attribute_type_without_list(attribute) }} value)
{
    this->{{ attribute["name"] }} = value;
    for ( shared_ptr<I{{ h.get_prefixed_name("Observer") }}<{{ h.get_attribute_type_without_list(attribute) }}>> observer : {{ attribute["name"] }}_observers )
    {
        observer->update( value );
    }
}
{% else %}
void {{ h.get_prefixed_name(name) }}Base::add_{{ h.get_singular_attribute_name(attribute) }}({{ h.get_attribute_type_without_list(attribute) }} value)
{
    this->{{ attribute["name"] }}.push_back( value );
    for ( shared_ptr<I{{ h.get_prefixed_name("Observer") }}<{{ h.get_attribute_type_without_list(attribute) }}>> observer : {{ attribute["name"] }}_observers )
    {
        observer->update( value );
    }
}
{% endif %}
{% endfor %}
"""
