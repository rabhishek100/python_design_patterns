"""
Template Method pattern:
Defines the skeleton of an algorithm in a base class and lets subclasses
override specific steps without changing the algorithm structure.
"""

from abc import ABC, abstractmethod


class PizzaTemplate(ABC):
    def make_base(self) -> None:
        print("basic base")

    def add_cheese(self) -> None:
        print("basic cheese")

    @abstractmethod
    def add_veggies(self) -> None:
        """Subclasses must provide pizza-specific toppings."""

    def bake(self) -> None:
        print("bake at 300")

    def make_pizza(self) -> None:
        # Template method: fixed order of steps.
        self.make_base()
        self.add_cheese()
        self.add_veggies()
        self.bake()


class VeggiePizza(PizzaTemplate):
    def add_veggies(self) -> None:
        print("added capsicum and onion")

    def bake(self) -> None:
        print("bake at 400")


if __name__ == "__main__":
    pizza = VeggiePizza()
    pizza.make_pizza()
