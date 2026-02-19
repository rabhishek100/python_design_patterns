import time
from threading import Thread, Lock

class Singleton(type):
    _instances = {}
    _lock = Lock()

    def __call__(self, *args, **kwargs):
        with self._lock:
            if self not in self._instances:
                instance = super().__call__(*args, **kwargs)
                time.sleep(1)
                self._instances[self] = instance
            return self._instances[self]



class SingletonClass(metaclass=Singleton):

    def __init__(self, item):
        self.item = item

    def print(self):
        print(self)


def create_singleton():
    s = SingletonClass("item1")
    s.print()
    return s



if __name__ == "__main__":

    t1 = Thread(target=create_singleton)
    t2 = Thread(target=create_singleton)

    t1.start()
    t2.start()

