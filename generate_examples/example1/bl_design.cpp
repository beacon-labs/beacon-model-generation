/*
 * BLDesign
 * ------------------------------
 * A design or module used to group functions and cells
 */

#include "bl_design.h"


string BLDesign::get_name()
{
    return name;
}

void BLDesign::set_name(string value)
{
    name = value;
}

list<shared_ptr<BLInstance>> BLDesign::get_instances()
{
    return instances;
}

void BLDesign::set_instances(list<shared_ptr<BLInstance>> value)
{
    instances = value;
}
