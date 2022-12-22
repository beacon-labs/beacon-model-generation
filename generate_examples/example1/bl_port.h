
/*
 * BLPort
 * ------------------------------
 * A port of a design
 */

#pragma once

using namespace std;

#include <memory>
#include <string>


class BLPort
{
    
        string name;
    
        string direction;
    
    public:
        
            string get_name();
            
                void set_name(string value);
            
        
            string get_direction();
            
                void set_direction(string value);
            
        

};
