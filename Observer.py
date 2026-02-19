"""
Observer pattern: maintain a one-to-many dependency so that when subject
state changes, all registered observers are notified automatically.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class WeatherUpdate:
    temp: float
    rainy: bool


class WeatherState:
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self.temp: float = 20.0
        self.rainy: bool = False

    def add_observer(self, observer: Observer) -> bool:
        if observer in self._observers:
            return False
        self._observers.append(observer)
        return True

    def remove_observer(self, observer: Observer) -> bool:
        if observer not in self._observers:
            return False
        self._observers.remove(observer)
        return True

    def update_state(self, temp: float, rainy: bool) -> None:
        self.temp = temp
        self.rainy = rainy
        self._notify_observers(WeatherUpdate(temp=temp, rainy=rainy))

    def _notify_observers(self, state: WeatherUpdate) -> None:
        # Iterate over a snapshot so observer list mutation during callbacks is safe.
        for observer in list(self._observers):
            try:
                observer.notify(state)
            except Exception:
                logger.exception("Observer %r failed to handle update", observer)


class Observer(ABC):
    @abstractmethod
    def notify(self, state: WeatherUpdate) -> None:
        pass


class LiveWeatherDisplay(Observer):
    def __init__(self) -> None:
        self.temp: float | None = None
        self.rainy: bool = False

    def notify(self, state: WeatherUpdate) -> None:
        self.temp = state.temp
        self.rainy = state.rainy

    def display(self) -> None:
        print(f"temp is {self.temp} and rainy is {self.rainy}")


class WeatherStats(Observer):
    def __init__(self) -> None:
        self.avg_temp: float = 25.0

    def notify(self, state: WeatherUpdate) -> None:
        self.avg_temp = 0.9 * self.avg_temp + 0.1 * state.temp

    def display(self) -> None:
        print(f"avg temp is {self.avg_temp}")


if __name__ == "__main__":
    weather_state = WeatherState()
    live_display = LiveWeatherDisplay()
    stats = WeatherStats()

    weather_state.add_observer(live_display)
    weather_state.add_observer(stats)

    weather_state.update_state(35, True)
    live_display.display()
    stats.display()

    weather_state.update_state(44, False)
    live_display.display()
    stats.display()
