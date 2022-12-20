
/*
 * BLPort
 * ------------------------------
 * A port of a design
 */

#ifndef _BLPORT_H_
#define _BLPORT_H_

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

#endif