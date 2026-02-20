from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Rides import Ride


class Cost(ABC):
    @abstractmethod
    def cost(self, ride: Ride) -> float: ...


class NormalCost(Cost):
    def cost(self, ride: Ride) -> float:
        return ride.base_cost()


class SurgeCost(Cost):
    def __init__(self, multiplier: float = 1.5):
        self.multiplier = multiplier

    def cost(self, ride: Ride) -> float:
        return ride.base_cost() * self.multiplier


class SharingCost(Cost):

    def __init__(self, num_share: int):
        self.num_share = max(1, num_share)

    def cost(self, ride: Ride) -> float:
        return ride.base_cost() / self.num_share


class LuxCost(Cost):
    def __init__(self, multiplier: float = 2.0):
        self.multiplier = multiplier

    def cost(self, ride: Ride) -> float:
        return ride.base_cost() * self.multiplier
