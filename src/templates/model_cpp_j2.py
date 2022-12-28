TEMPLATE = """
/*
 * {{ h.get_prefixed_name(name) }}
 * ------------------------------
 * {{ description }}
 */

#include "{{ h.get_header_filename(name) }}"

// Add your custom code here

"""
