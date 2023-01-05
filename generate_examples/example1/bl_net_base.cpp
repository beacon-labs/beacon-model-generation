
/*
 * BLNetBase
 * ------------------------------
 * An net to connect instance pins (and optionally design ports)
 *
 * IMPORTANT NOTE: DO NOT EDIT THIS FILE, edit bl_net.h instead
 *
 */

#include "bl_net_base.h"


string BLNetBase::get_name()
{
    return this->name;
}

void BLNetBase::observe_name(shared_ptr<IBLObserver<string>> observer)
{
    name_observers.push_back( observer );
}

void BLNetBase::set_name(string value)
{
    this->name = value;
    for ( shared_ptr<IBLObserver<string>> observer : name_observers )
    {
        observer->update( value );
    }
}


list<shared_ptr<BLPin>> BLNetBase::get_pins()
{
    return this->pins;
}

void BLNetBase::observe_pins(shared_ptr<IBLObserver<shared_ptr<BLPin>>> observer)
{
    pins_observers.push_back( observer );
}


void BLNetBase::add_pin(shared_ptr<BLPin> value)
{
    this->pins.push_back( value );
    for ( shared_ptr<IBLObserver<shared_ptr<BLPin>>> observer : pins_observers )
    {
        observer->update( value );
    }
}


list<shared_ptr<BLPort>> BLNetBase::get_ports()
{
    return this->ports;
}

void BLNetBase::observe_ports(shared_ptr<IBLObserver<shared_ptr<BLPort>>> observer)
{
    ports_observers.push_back( observer );
}


void BLNetBase::add_port(shared_ptr<BLPort> value)
{
    this->ports.push_back( value );
    for ( shared_ptr<IBLObserver<shared_ptr<BLPort>>> observer : ports_observers )
    {
        observer->update( value );
    }
}

