"""

definition: State Pattern lets an object alter its behavior when its internal state changes by delegating behavior to state objects.
State objects encapsulate state-specific behavior and can trigger transitions in the context.

"""


from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def insert_coin(self, ctx) -> str: ...


    @abstractmethod
    def pull_lever(self, ctx) -> tuple[bool, str]: ...



class Idle(State):

    def insert_coin(self, ctx) -> str:
        ctx.state = ctx.coin_state
        return "coin inserted"

    def pull_lever(self, ctx) -> tuple[bool, str]:
        return False, "cannot pull lever without coin"


class Coin(State):

    def insert_coin(self, ctx) -> str:
        return "coin already inserted"

    def pull_lever(self, ctx) -> tuple[bool, str]:
        ctx.state = ctx.idle_state
        return True, "item coming out"


class VendingMachine:

    def __init__(self):
        self.idle_state = Idle()
        self.coin_state = Coin()
        self.state = self.idle_state

    def insert_coin(self):
        message = self.state.insert_coin(self)
        print(message)

    def pull_lever(self):
        dispensed, message = self.state.pull_lever(self)
        print(message)
        if dispensed:
            print("item received")


if __name__ == "__main__":
    
    vend = VendingMachine()

    vend.pull_lever()

    vend.insert_coin()
    vend.insert_coin()

    vend.pull_lever()
