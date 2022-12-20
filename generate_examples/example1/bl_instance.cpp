
/*
 * BLInstance
 * ------------------------------
 * An instance of a design
 */

#include "bl_instance.h"


    string BLInstance::get_name()
    {
        return this->name;
    }

    void BLInstance::set_name(string value)
        {
            this->name = value;
        }
    

    shared_ptr<BLDesign> BLInstance::get_reference()
    {
        return this->reference;
    }

    void BLInstance::set_reference(shared_ptr<BLDesign> value)
        {
            this->reference = value;
        }
    

    list<shared_ptr<BLPin>> BLInstance::get_pins()
    {
        return this->pins;
    }

    
        void BLInstance::add_pin(shared_ptr<BLPin> value)
        {
            this->pins.push_back( value );
        }
    
