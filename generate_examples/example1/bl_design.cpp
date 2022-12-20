
/*
 * BLDesign
 * ------------------------------
 * A design or module used to group functions and cells
 */

#include "bl_design.h"


    string BLDesign::get_name()
    {
        return this->name;
    }

    void BLDesign::set_name(string value)
        {
            this->name = value;
        }
    

    list<shared_ptr<BLInstance>> BLDesign::get_instances()
    {
        return this->instances;
    }

    
        void BLDesign::add_instance(shared_ptr<BLInstance> value)
        {
            this->instances.push_back( value );
        }
    
