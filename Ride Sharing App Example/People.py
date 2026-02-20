from __future__ import annotations

from typing import TYPE_CHECKING

from RideNotifier import RideObserver

if TYPE_CHECKING:
    from Rides import Ride
    from Vehicles import Vehicle

class Person(RideObserver):
    def __init__(self, name: str, phone: str, rating: int, location: tuple[float, float] | str):
        self.name = name
        self.phone = phone
        self.rating = rating
        self.location = self._to_coords(location)
        self.notifications: list[str] = []
    
    def observe_ride(self, ride: Ride) -> None:
        driver_name = ride.driver.name if ride.driver is not None else "unassigned"
        message = (
            f"{self.__class__.__name__} {self.name}: "
            f"Ride {ride.from_place}->{ride.to} is {ride.status.value} "
            f"(driver={driver_name})"
        )
        self.notifications.append(message)
        print(message)

    def print_notifications(self) -> None:
        print(f"Notifications for {self.__class__.__name__} {self.name}:")
        if not self.notifications:
            print("  No notifications yet.")
            return
        for notification in self.notifications:
            print(f"  {notification}")

    @staticmethod
    def _to_coords(location: tuple[float, float] | str) -> tuple[float, float]:
        if isinstance(location, tuple):
            return location
        x, y = location.split()
        return float(x), float(y)


class Rider(Person):
    pass


class Driver(Person):
    def __init__(self, name: str, phone: str, rating: int, location: str, vehicle: Vehicle):
        super().__init__(name, phone, rating, location)
        self.vehicle = vehicle
        self.is_available = True
