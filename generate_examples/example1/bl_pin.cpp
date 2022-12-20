
/*
 * BLPin
 * ------------------------------
 * Pin of an instance
 */

#include "bl_pin.h"


    string BLPin::get_name()
    {
        return this->name;
    }

    void BLPin::set_name(string value)
        {
            this->name = value;
        }
    

    string BLPin::get_direction()
    {
        return this->direction;
    }

    void BLPin::set_direction(string value)
        {
            this->direction = value;
        }
    
