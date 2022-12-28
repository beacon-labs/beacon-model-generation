
/*
 * BLPortBase
 * ------------------------------
 * A port of a design
 *
 * IMPORTANT NOTE: DO NOT EDIT THIS FILE, edit bl_port.cpp instead
 *
 */

#pragma once

using namespace std;

#include <memory>
#include <string>


class BLPortBase
{
    
        string name;
    
        string direction;
    
    public:
        
            string get_name();
            
                void set_name(string value);
            
        
            string get_direction();
            
                void set_direction(string value);
            
        

};
