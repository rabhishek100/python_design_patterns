"""

definition: Visitor: add new operations to a set of object types without modifying those types

"""


from dataclasses import dataclass

class Shape:
    def accept(self, v):
        raise NotImplementedError


@dataclass(frozen=True)
class Circle(Shape):
    r: float
    def accept(self, v): return v.visit_circle(self)


@dataclass(frozen=True)
class Rect(Shape):
    w: float; h: float
    def accept(self, v): return v.visit_rect(self)


# ---- Visitors (operations) ----
class Area:
    def visit_circle(self, c: Circle): return 3.14159 * c.r * c.r
    def visit_rect(self, r: Rect):     return r.w * r.h

class ToJSON:
    def visit_circle(self, c: Circle): return {"type": "circle", "r": c.r}
    def visit_rect(self, r: Rect):     return {"type": "rect", "w": r.w, "h": r.h}


if __name__ == "__main__":
    shapes = [Circle(2), Rect(3, 4)]
    print([s.accept(Area()) for s in shapes])     # [12.56636, 12]
    print([s.accept(ToJSON()) for s in shapes])   # [{'type':...}, {'type':...}]