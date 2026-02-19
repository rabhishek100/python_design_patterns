"""

    definition: Prototype: create new objects by cloning an existing object (shallow or deep copy), then optionally tweak a few fields.

"""


from __future__ import annotations
from dataclasses import dataclass, field
from copy import deepcopy
from typing import Dict, List, Protocol


class Prototype(Protocol):

    def clone(self) -> "Prototype":
        ...
    


@dataclass
class Character:
    name: str
    hp: int
    inventory: List[str] = field(default_factory=list)
    skills: Dict[str, int] = field(default_factory=dict)

    def clone(self) -> "Character":
        # Deep copy prevents shared mutable state (inventory/skills)
        return deepcopy(self)



class CharacterRegistry:

    def __init__(self):
        self._prototypes : Dict[str, Character] = {}


    def register(self, key : str, prototype: Character) -> None:
        self._prototypes[key] = prototype

    
    def create(self, key : str, **overrides) -> Character:
        obj = self._prototypes[key].clone()
        for k, v in overrides.items():
            setattr(obj, k, v)
        return obj



if __name__ == "__main__":
    registry = CharacterRegistry()

    # Store “templates”
    registry.register(
        "warrior",
        Character(name="TEMPLATE", hp=120, inventory=["sword"], skills={"slash": 3})
    )
    registry.register(
        "mage",
        Character(name="TEMPLATE", hp=70, inventory=["staff"], skills={"fireball": 4})
    )

    # Create new instances by cloning prototypes + overriding
    a = registry.create("warrior", name="Arjun")
    b = registry.create("warrior", name="Bheem")

    a.inventory.append("shield")          # should NOT affect b
    a.skills["slash"] = 10                # should NOT affect b

    print(a)  # Arjun has shield, slash=10
    print(b)  # Bheem unchanged