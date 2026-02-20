from dataclasses import dataclass


@dataclass
class Vehicle:
    name: str
    number: str

    def fare_per_km(self) -> float:
        return float(getattr(self.__class__, "base_fare_per_km", 10.0))


class Bike(Vehicle):
    base_fare_per_km = 7.0


class Car(Vehicle):
    base_fare_per_km = 10.0


class SmallCar(Car):
    base_fare_per_km = 9.0


class LargeCar(Car):
    base_fare_per_km = 12.0


class LuxCar(Car):
    base_fare_per_km = 20.0
