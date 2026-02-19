"""

definition: Iterator: provide a standard way to traverse collections
without exposing its internals

"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator, List


@dataclass
class RobotPath:
    waypoints: List[tuple[float, float]]


    def __iter__(self) -> Iterator[tuple[float, float]]:
        return _PathIterator(self.waypoints)



class _PathIterator:

    def __init__(self, waypoints: List[tuple[float, float]]):
        self._wps = waypoints
        self._i = 0

    
    def __iter__(self):
        return self

    
    def __next__(self) -> tuple[float, float]:
        if self._i >= len(self._wps):
            raise StopIteration
        wp = self._wps[self._i]
        self._i += 1
        return wp


if __name__ == "__main__":
    path = RobotPath([(0, 0), (1, 0), (1, 1)])
    for wp in path:
        print("go to", wp)

