from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Rides import Ride

class RideObserver(ABC):
    @abstractmethod
    def observe_ride(self, ride: Ride) -> None: ...
