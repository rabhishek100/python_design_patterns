"""

definition: split what you do from how you do it so that each set of classes can evolve independently

"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Renderer(ABC):
    
    @abstractmethod
    def circle(self, x, y, r): ...

    @abstractmethod
    def square(self, x, y, a): ...


class VectorRenderer(Renderer):
    
    def circle(self, x, y, r):
        print(f"vector circle at {x} {y} with radius {r}")

    def square(self, x, y, a):
        print(f"vector square at {x} {y} with side {a}")


class RasterRenderer(Renderer):
    
    def circle(self, x, y, r):
        print(f"raster circle at {x} {y} with radius {r}")

    def square(self, x, y, a):
        print(f"raster square at {x} {y} with side {a}")



class Shape(ABC):
    
    def __init__(self, renderer : Renderer):
        self._renderer = renderer

    @abstractmethod
    def draw(self) -> str: ...


@dataclass
class Square(Shape):
    _renderer : Renderer
    x : float
    y : float
    a : float

    def draw(self):
        self._renderer.square(self.x, self.y, self.a)


@dataclass
class Circle(Shape):
    _renderer : Renderer
    x : float
    y : float
    r : float

    def draw(self):
        self._renderer.circle(self.x, self.y, self.r)



if __name__ == "__main__":

    renderer = VectorRenderer() # RasterRenderer()

    shapes = [Square(renderer, 1, 1, 2), Circle(renderer, 2, 2, 3)]

    for shape in shapes:
        shape.draw()

