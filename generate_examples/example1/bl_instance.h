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
#include "bl_design.h"

class BLInstance
{
    string name;
    weak_ptr<BLDesign> reference;
    
    public:
        
            string get_name();
            string set_name(string value);
        
            weak_ptr<BLDesign> get_reference();
            weak_ptr<BLDesign> set_reference(weak_ptr<BLDesign> value);
        

};

#endif