"""

Definition: Strategy pattern lets you define a family of behaviors, encapsulate
each one, and swap them at runtime through a common interface.

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Weapon(ABC):
    @abstractmethod
    def attack(self, character: Character) -> None: ...



class Sword(Weapon):
    def attack(self, character: Character) -> None:
        character.enemy = max(0, character.enemy - 10)


class Gun(Weapon):
    def attack(self, character: Character) -> None:
        character.enemy = max(0, character.enemy - 15)


@dataclass()
class Character:
    health: float = 100
    enemy: float = 100
    weapon: Weapon | None = None

    def set_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon

    def attack(self) -> None:
        if self.weapon is None:
            raise RuntimeError("No weapon equipped. Call set_weapon() first.")
        self.weapon.attack(self)



if __name__ == "__main__":

    character: Character = Character()
    weapon: Weapon = Sword()

    character.set_weapon(weapon)
    character.attack()
    print(f"Enemy health: {character.enemy}")

    weapon = Gun()

    character.set_weapon(weapon)
    character.attack()
    print(f"Enemy health: {character.enemy}")
