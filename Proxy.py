"""

definition: proxy pattern - a stand in object that control access to a real object
virtual proxy
protection proxy
caching proxy
remote proxy

"""

# virtual + caching proxy example

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from time import sleep


class Image(ABC):
    @abstractmethod
    def display(self) -> None: ...
    

@dataclass
class RealImage(Image):
    path: str

    def __post_init__(self) -> None:
        # simulate expensive disk/network load
        print(f"[RealImage] loading {self.path}...")
        sleep(0.2)
        print(f"[RealImage] loaded {self.path}")

    def display(self) -> None:
        print(f"[RealImage] display {self.path}")


class ImageProxy(Image):
    def __init__(self, path: str):
        self._path = path
        self._real: RealImage | None = None  # lazy

    def display(self) -> None:
        # lazy load on first use
        if self._real is None:
            self._real = RealImage(self._path)
        print("[Proxy] delegating to RealImage")
        self._real.display()


if __name__ == "__main__":
    img = ImageProxy("cat.png")

    print("Created proxy (no load yet).")
    img.display()   # triggers load
    img.display()   # uses cached RealImage (no reload)