import random
import threading

class SystemState:
    def __init__(self):
        self._lock = threading.Lock()
        self.value = random.random()
        self.entropy = 0.1
        self.collapsed = False

    def observe(self):
        with self._lock:
            if self.collapsed:
                return None
            
            disturbance = random.gauss(0, self.entropy)
            self.value += disturbance
            self.entropy *= 1.05

            if self.entropy >=5.0:
                self.collapsed = True

            return self.value
        
    def raw(self):
        with self._lock:
            return {
                "value": None if self.collapsed else self.value,
                "entropy": self.entropy,
                "collapsed": self.collapsed
            }