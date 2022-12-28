TEMPLATE = """
/*
 * {{ h.get_prefixed_name(name) }}
 * ------------------------------
 * {{ description }}
 */

#pragma once

#include "{{ h.get_header_filename(name+'Base') }}"

using namespace std;

class {{ h.get_prefixed_name(name) }} : public {{ h.get_prefixed_name(name+'Base') }}
{
    // Add your custom code here
};

"""
