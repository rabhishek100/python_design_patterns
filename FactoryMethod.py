"""
Factory Method (GoF):
Define an interface for creating an object, but let subclasses decide
which class to instantiate.
"""

from abc import ABC, abstractmethod


class Pizza(ABC):
    @property
    @abstractmethod
    def kind(self) -> str:
        """Return a human-readable pizza type."""


class PineapplePizza(Pizza):
    @property
    def kind(self) -> str:
        return "PineapplePizza"


class CheesePizza(Pizza):
    @property
    def kind(self) -> str:
        return "CheesePizza"


class MakePizza(ABC):
    @abstractmethod
    def factory_method(self) -> Pizza:
        """Create and return a concrete Pizza."""

    def make(self) -> Pizza:
        pizza = self.factory_method()
        print(f"{pizza.kind} is in the oven!")
        return pizza


class MakePineapplePizza(MakePizza):
    def factory_method(self) -> Pizza:
        return PineapplePizza()


class MakeCheesePizza(MakePizza):
    def factory_method(self) -> Pizza:
        return CheesePizza()


if __name__ == "__main__":
    pineapple_maker = MakePineapplePizza()
    cheese_maker = MakeCheesePizza()

    pineapple_maker.make()
    cheese_maker.make()
