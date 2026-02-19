"""

definition: Command pattern = wrap an action (and its parameters) into an object
so you can queue it, log it, undo it, retry it, etc.

"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Light:

    def __init__(self) -> None:
        self._is_on: bool = False

    def on(self) -> None:
        self._is_on = True
        print("Light: ON")

    def off(self) -> None:
        self._is_on = False
        print("Light: OFF")

    def is_on(self) -> bool:
        return self._is_on


class Command(ABC):

    @abstractmethod
    def execute(self) -> None: ...

    @abstractmethod
    def undo(self) -> None: ...


class LightOn(Command):

    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.on()

    def undo(self) -> None:
        self._light.off()


class LightOff(Command):

    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.off()

    def undo(self) -> None:
        self._light.on()


class Toggle(Command):

    def __init__(self, light: Light) -> None:
        self._light = light
        self._prev: bool | None = None


    def execute(self) -> None:
        self._prev = self._light.is_on()
        (self._light.off() if self._prev else self._light.on())


    def undo(self) -> None:
        if self._prev is None:
            return
        (self._light.on() if self._prev else self._light.off())



class Remote:

    def __init__(self) -> None:
        self._history: list[Command] = []

    def press(self, cmd: Command) -> None:
        cmd.execute()
        self._history.append(cmd)
    
    def undo_last(self) -> None:
        if self._history:
            self._history.pop().undo()


class Macro(Command):

    def __init__(self, commands: list[Command]) -> None:
        self._cmds = commands

    def execute(self) -> None:
        for c in self._cmds:
            c.execute()

    def undo(self) -> None:
        for c in reversed(self._cmds):
            c.undo()


if __name__ == "__main__":
    light = Light()
    remote = Remote()

    remote.press(LightOn(light))
    remote.press(Toggle(light))
    remote.undo_last()

    party_mode = Macro([LightOff(light), LightOn(light), Toggle(light)])
    remote.press(party_mode)
    remote.undo_last()