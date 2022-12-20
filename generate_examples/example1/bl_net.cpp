
/*
 * BLNet
 * ------------------------------
 * An net to connect instance pins (and optionally design ports)
 */

#include "bl_net.h"


    string BLNet::get_name()
    {
        return this->name;
    }

    void BLNet::set_name(string value)
        {
            this->name = value;
        }
    

    list<shared_ptr<BLPin>> BLNet::get_pins()
    {
        return this->pins;
    }

    
        void BLNet::add_pin(shared_ptr<BLPin> value)
        {
            this->pins.push_back( value );
        }
    

    list<shared_ptr<BLPort>> BLNet::get_ports()
    {
        return this->ports;
    }

    
        void BLNet::add_port(shared_ptr<BLPort> value)
        {
            this->ports.push_back( value );
        }
    
