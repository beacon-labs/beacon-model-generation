
#pragma once

#include <string>

template<typename TObserverValue>

class IBLObserver {
 public:
  virtual void update(TObserverValue value) = 0;
};