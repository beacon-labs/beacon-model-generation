TEMPLATE = """
#pragma once

#include <string>

template<typename TObserverValue>

class I{{ h.get_prefixed_name("Observer") }} {
 public:
  virtual void update(TObserverValue value) = 0;
};
"""
