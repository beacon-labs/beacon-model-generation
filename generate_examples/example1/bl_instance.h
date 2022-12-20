
/*
 * BLInstance
 * ------------------------------
 * An instance of a design
 */

#ifndef _BLINSTANCE_H_
#define _BLINSTANCE_H_

using namespace std;

#include <memory>
#include <string>
#include <list>
#include "bl_design.h"
#include "bl_pin.h"

class BLDesign;
class BLPin;

class BLInstance
{
    
        string name;
    
        shared_ptr<BLDesign> reference;
    
        list<shared_ptr<BLPin>> pins;
    
    public:
        
            string get_name();
            
                void set_name(string value);
            
        
            shared_ptr<BLDesign> get_reference();
            
                void set_reference(shared_ptr<BLDesign> value);
            
        
            list<shared_ptr<BLPin>> get_pins();
            
                void add_pin(shared_ptr<BLPin> value);
            
        

};

#endif