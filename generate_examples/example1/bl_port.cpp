
/*
 * BLPort
 * ------------------------------
 * A port of a design
 */

#include "bl_port.h"


    string BLPort::get_name()
    {
        return this->name;
    }

    void BLPort::set_name(string value)
        {
            this->name = value;
        }
    

    string BLPort::get_direction()
    {
        return this->direction;
    }

    void BLPort::set_direction(string value)
        {
            this->direction = value;
        }
    
