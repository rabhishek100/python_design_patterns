from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from People import Driver
    from Rides import Ride


class Matcher:

    def __init__(self):
        self.ride_requests = []
        self.drivers = []

    def add_ride_request(self, ride_request: Ride):
        self.ride_requests.append(ride_request)

    def remove_ride_request(self, ride_request: Ride):
        if ride_request in self.ride_requests:
            self.ride_requests.remove(ride_request)

    def add_driver(self, driver: Driver):
        self.drivers.append(driver)

    def remove_driver(self, driver: Driver):
        if driver in self.drivers:
            self.drivers.remove(driver)

    def make_matches(self):
        matches = []
        unmatched_ride_requests = []
        available_drivers = [driver for driver in self.drivers if driver.is_available]

        for ride_request in self.ride_requests:
            if not available_drivers:
                unmatched_ride_requests.append(ride_request)
                continue

            rider_x, rider_y = ride_request.rider.location
            closest_driver = min(
                available_drivers,
                key=lambda driver: (driver.location[0] - rider_x) ** 2
                + (driver.location[1] - rider_y) ** 2,
            )
            ride_request.assign_driver(closest_driver)
            available_drivers.remove(closest_driver)
            matches.append((ride_request, closest_driver))

        self.ride_requests = unmatched_ride_requests
        return matches
