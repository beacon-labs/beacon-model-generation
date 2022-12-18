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

class BLDesign
{
    string name;
    list<shared_ptr<BLInstance>> cells;
    
    public:
        
            string get_name();
            string set_name(string value);
        
            list<shared_ptr<BLInstance>> get_cells();
            list<shared_ptr<BLInstance>> set_cells(list<shared_ptr<BLInstance>> value);
        

};

#endif