/*
 * BLInstance
 * ------------------------------
 * An instance of a design
 */

#include "bl_instance.h"


string BLInstance::get_name()
{
    return name;
}

void BLInstance::set_name(string value)
{
    name = value;
}

weak_ptr<BLDesign> BLInstance::get_reference()
{
    return reference;
}

void BLInstance::set_reference(weak_ptr<BLDesign> value)
{
    reference = value;
}
