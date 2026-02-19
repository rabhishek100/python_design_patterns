"""

    definition: Mediator: components dont talk to each other directly,
    they talk via a mediator (coordinator)

"""

# example - UI dialog mediator

from __future__ import annotations
from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None: ...


class Component:
    def __init__(self, mediator: Mediator):
        self._mediator = mediator


class TextBox(Component):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator)
        self.text = ""

    def set_text(self, text: str) -> None:
        self.text = text
        self._mediator.notify(self, "text_changed")


class CheckBox(Component):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator)
        self.checked = False

    def set_checked(self, checked: bool) -> None:
        self.checked = checked
        self._mediator.notify(self, "checked_changed")


class Button(Component):
    def __init__(self, mediator: Mediator, label: str):
        super().__init__(mediator)
        self.label = label
        self.enabled = False

    def click(self) -> None:
        if not self.enabled:
            print(f"[{self.label}] disabled (ignored)")
            return
        self._mediator.notify(self, "clicked")


class LoginDialog(Mediator):
    def __init__(self) -> None:
        self.username = TextBox(self)
        self.tos = CheckBox(self)
        self.submit = Button(self, "Submit")

        self._recompute()


    def notify(self, sender: object, event: str) -> None:
        if event in ("text_changed", "checked_changed"):
            self._recompute()
        elif event == "clicked" and sender is self.submit:
            print(f"Logging in as '{self.username.text}' (tos={self.tos.checked})")


    def _recompute(self) -> None:
        self.submit.enabled = bool(self.username.text.strip()) and self.tos.checked
        print(f"[state] submit.enabled = {self.submit.enabled}")


if __name__ == "__main__":
    ui = LoginDialog()

    ui.submit.click()
    ui.username.set_text("abhishek")
    ui.submit.click()
    ui.tos.set_checked(True)
    ui.submit.click()