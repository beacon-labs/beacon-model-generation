
/*
 * BLDesign
 * ------------------------------
 * A design or module used to group functions and cells
 */

#ifndef _BLDESIGN_H_
#define _BLDESIGN_H_

using namespace std;

#include <memory>
#include <string>
#include <list>
#include "bl_instance.h"

class BLInstance;

class BLDesign
{
    
        string name;
    
        list<shared_ptr<BLInstance>> instances;
    
    public:
        
            string get_name();
            
                void set_name(string value);
            
        
            list<shared_ptr<BLInstance>> get_instances();
            
                void add_instance(shared_ptr<BLInstance> value);
            
        

};

#endif