from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import Enum
from typing import TYPE_CHECKING

from Pricing import Cost, NormalCost
from RideNotifier import RideObserver

if TYPE_CHECKING:
    from People import Driver, Rider


class RideStatus(str, Enum):
    PENDING = "pending"
    ONGOING = "ongoing"
    COMPLETED = "completed"


@dataclass
class Ride:
    from_place: str | tuple[float, float]
    to: str | tuple[float, float]
    ride_duration: str
    request_time: str
    rider: Rider
    status: RideStatus = RideStatus.PENDING
    accept_time: str | None = None
    driver: Driver | None = None
    base_rate: float = 10.0
    pricing: Cost = field(default_factory=NormalCost)
    _observers: list[RideObserver] = field(default_factory=list, init=False, repr=False)

    def __post_init__(self) -> None:
        self.add_observer(self.rider)
        if self.driver is not None:
            self.add_observer(self.driver)

    def add_observer(self, observer: RideObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: RideObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def assign_driver(self, driver: Driver, accept_time: str | None = None) -> None:
        self.driver = driver
        self.driver.is_available = False
        self.accept_time = accept_time
        self.add_observer(driver)
        self._notify_observers()

    def start_ride(self) -> None:
        self.status = RideStatus.ONGOING
        self._notify_observers()

    def complete_ride(self) -> None:
        self.status = RideStatus.COMPLETED
        if self.driver is not None:
            self.driver.is_available = True
        self._notify_observers()

    def print_status(self) -> None:
        driver_name = self.driver.name if self.driver is not None else "unassigned"
        print(
            f"Ride {self.from_place} -> {self.to} | "
            f"status={self.status.value} | rider={self.rider.name} | driver={driver_name}"
        )

    def distance(self) -> float:
        from_x, from_y = self._to_coords(self.from_place)
        to_x, to_y = self._to_coords(self.to)
        return math.dist((from_x, from_y), (to_x, to_y))

    def base_cost(self) -> float:
        if self.driver is not None:
            return self.distance() * self.driver.vehicle.fare_per_km()
        return self.distance() * self.base_rate

    def calculate_cost(self) -> float:
        return self.pricing.cost(self)

    def print_fare(self) -> None:
        rate = self.driver.vehicle.fare_per_km() if self.driver is not None else self.base_rate
        print(
            f"Ride {self.from_place}->{self.to} fare "
            f"(rate_per_km={rate}, strategy={self.pricing.__class__.__name__}): "
            f"{self.calculate_cost():.2f}"
        )

    def _notify_observers(self) -> None:
        for observer in list(self._observers):
            observer.observe_ride(self)

    @staticmethod
    def _to_coords(point: str | tuple[float, float]) -> tuple[float, float]:
        if isinstance(point, tuple):
            return point
        x, y = point.split()
        return float(x), float(y)


class NormalRide(Ride):
    pass


class LuxRide(Ride):
    pass


@dataclass
class SharingRide(Ride):
    shared_by: int = 1
