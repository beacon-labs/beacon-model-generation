
/*
 * BLInstanceBase
 * ------------------------------
 * An instance of a design
 *
 * IMPORTANT NOTE: DO NOT EDIT THIS FILE, edit bl_instance.cpp instead
 *
 */

#pragma once

using namespace std;

#include <memory>
#include <string>
#include <list>
class BLDesign;
class BLPin;

class BLInstanceBase
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