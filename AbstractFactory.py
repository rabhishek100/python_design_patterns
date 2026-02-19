"""

definition -> create a class of factories implementing an abstract factory that gives various combinations of implementations of a group of interfaces
Abstract Factory means: define an interface for creating a family of related objects without specifying their concrete classes.

"""

from abc import ABC, abstractmethod



class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class CheckBox(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class WindowsButton(Button):
    def render(self) -> None:
        print("Windows Button")


class MacButton(Button):
    def render(self) -> None:
        print("Mac Button")


class WindowsCheckBox(CheckBox):
    def render(self) -> None:
        print("Windows Checkbox")


class MacCheckBox(CheckBox):
    def render(self) -> None:
        print("Mac Checkbox")


class UIfactory(ABC):
    @abstractmethod
    def button(self) -> Button:
        pass

    @abstractmethod
    def checkbox(self) -> CheckBox:
        pass


class WindowsUIfactory(UIfactory):
    def button(self) -> Button:
        return WindowsButton()

    def checkbox(self) -> CheckBox:
        return WindowsCheckBox()


class MacUIfactory(UIfactory):
    def button(self) -> Button:
        return MacButton()

    def checkbox(self) -> CheckBox:
        return MacCheckBox()


class App:
    def __init__(self, factory):
        self.button = factory.button()
        self.checkbox = factory.checkbox()

    def render(self):
        self.button.render()
        self.checkbox.render()


if __name__ == "__main__":
    factory : UIfactory = WindowsUIfactory() # MacUIfactory()
    app = App(factory)
    app.render()