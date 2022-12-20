
/*
 * BLNet
 * ------------------------------
 * An net to connect instance pins (and optionally design ports)
 */

#ifndef _BLNET_H_
#define _BLNET_H_

using namespace std;

#include <memory>
#include <string>
#include <list>
#include "bl_pin.h"
#include "bl_port.h"

class BLPin;
class BLPort;

class BLNet
{
    
        string name;
    
        list<shared_ptr<BLPin>> pins;
    
        list<shared_ptr<BLPort>> ports;
    
    public:
        
            string get_name();
            
                void set_name(string value);
            
        
            list<shared_ptr<BLPin>> get_pins();
            
                void add_pin(shared_ptr<BLPin> value);
            
        
            list<shared_ptr<BLPort>> get_ports();
            
                void add_port(shared_ptr<BLPort> value);
            
        

};

#endif