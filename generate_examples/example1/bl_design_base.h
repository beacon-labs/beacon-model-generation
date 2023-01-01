
/*
 * BLDesignBase
 * ------------------------------
 * A design or module used to group functions and cells
 *
 * IMPORTANT NOTE: DO NOT EDIT THIS FILE, edit bl_design.cpp instead
 *
 */

#pragma once

using namespace std;

#include <memory>
#include <string>
#include <list>
// //     #include "bl_instance.h"
// 
class BLInstance;

class BLDesignBase
{
    
        string name;
    
        list<shared_ptr<BLInstance>> instances;
    
    public:
        
            string get_name();
            
                void set_name(string value);
            
        
            list<shared_ptr<BLInstance>> get_instances();
            
                void add_instance(shared_ptr<BLInstance> value);
            
        

};
