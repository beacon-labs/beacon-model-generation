
/*
 * BLPin
 * ------------------------------
 * Pin of an instance
 */

#ifndef _BLPIN_H_
#define _BLPIN_H_

using namespace std;

#include <memory>
#include <string>


class BLPin
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