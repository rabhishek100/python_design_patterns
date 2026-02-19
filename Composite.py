"""

defintion: treat a single object and a collection of objects similarly

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

class Node(ABC):

    @abstractmethod
    def size(self) -> int:
        pass
    
    @abstractmethod
    def show(self) -> None:
        pass


@dataclass(frozen=True)
class File(Node):
    name : str = None
    bytes : int = 0

    def size(self) -> int:
        return bytes

    def show(self) -> None:
        print(f"filepath: {self.name} size: {self.bytes} bytes")


@dataclass
class Folder(Node):
    name : str = None
    children : List[Node] = field(default_factory=list)


    def add(self, node : Node) -> Node:
        self.children.append(node)


    def size(self) -> int:
        total = 0
        for child in self.children:
            total += self.size(child)
        return total

    
    def show(self) -> None:
        print(f"folderpath: {self.name}")
        print("contents")
        for child in self.children:
            child.show()


if __name__ == "__main__":

    root = Folder("root_folder")

    file1 = File("file1", 10)
    file2 = File("file2", 100)
    folder1 = Folder("folder1")

    file3 = File("file3", 75)
    folder1.add(file3)

    root.add(file1)
    root.add(file2)
    root.add(folder1)

    root.show()