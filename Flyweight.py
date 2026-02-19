"""

    definition: share heavy, repeatable state across many objects to save memory

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Tuple
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class TreeType:
    name: str
    color: str
    texture: str

    def draw(self, x: int, y: int) -> None:
        print(f"Draw {self.name} ({self.color}, {self.texture}) at ({x},{y})")


class TreeTypeFactory:
    def __init__(self) -> None:
        self._cache: Dict[Tuple[str, str, str], TreeType] = {}

    def get(self, name: str, color: str, texture: str) -> TreeType:
        key = (name, color, texture)
        if key not in self._cache:
            self._cache[key] = TreeType(name, color, texture)
        return self._cache[key]

    def count(self) -> int:
        return len(self._cache)


@dataclass(slots=True)
class Tree:
    x: int
    y: int
    type: TreeType  # shared flyweight


class Forest:
    def __init__(self, factory: TreeTypeFactory) -> None:
            self._factory = factory
            self._trees: list[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        t = self._factory.get(name, color, texture)
        self._trees.append(Tree(x, y, t))

    def draw(self) -> None:
        for tree in self._trees:
            tree.type.draw(tree.x, tree.y)


if __name__ == "__main__":
    factory = TreeTypeFactory()
    forest = Forest(factory)

    # 1000 trees, but only 2 shared TreeType objects
    for i in range(500):
        forest.plant_tree(i, i, "Oak", "Green", "oak_texture_v1")
        forest.plant_tree(i, i + 1, "Pine", "DarkGreen", "pine_texture_v2")

    print("Unique TreeTypes:", factory.count())  # -> 2
    forest.draw()

