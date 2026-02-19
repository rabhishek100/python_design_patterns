"""

    definition: add additional behaviour to objects by wrapping it without changing its class

"""


from abc import ABC, abstractmethod


class Drink(ABC):

    @abstractmethod
    def cost(self) -> int:
        pass


class Coffee(Drink):

    def cost(self) -> int:
        return 15


class DrinkDecorator(Drink):

    def __init__(self, drink: Drink):
        if not isinstance(drink, Drink):
            raise TypeError("drink must be an instance of Drink")
        self._drink = drink

    def cost(self) -> int:
        return self._drink.cost()


class MilkCoffeeDecorator(DrinkDecorator):

    def cost(self) -> int:
        return super().cost() + 5


class VanillaCoffeeDecorator(DrinkDecorator):

    def cost(self) -> int:
        return super().cost() + 3



if __name__ == "__main__":

    coffee = Coffee()
    print(f"Coffee: {coffee.cost()}")

    milk_coffee = MilkCoffeeDecorator(coffee)
    print(f"Coffee + Milk: {milk_coffee.cost()}")

    vanilla_milk_coffee = VanillaCoffeeDecorator(milk_coffee)
    print(f"Coffee + Milk + Vanilla: {vanilla_milk_coffee.cost()}")

    double_vanilla_milk_coffee = VanillaCoffeeDecorator(vanilla_milk_coffee)
    print(f"Coffee + Milk + Vanilla + Vanilla: {double_vanilla_milk_coffee.cost()}")
