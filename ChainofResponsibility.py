"""

Chain of Responsibility = pass a request along a chain of handlers until one handles it. This avoids gaint
if / elif blocks and lets you add/reorder handlers easily.

Use it for:

validation pipelines
logging filters
auth checks
request routing (HTTP Middleware style)

"""

# support ticket routing

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Protocol


@dataclass(frozen=True)
class Ticket:
    kind: str
    message: str


class Handler(Protocol):
    def set_next(self, nxt: "Handler") -> "Handler":  ...
    def handle(self, ticket: Ticket) -> Optional[str]: ...


class BaseHandler:
    def __init__(self) -> None:
        self._next: Optional[BaseHandler] = None

    def set_next(self, nxt: "BaseHandler") -> "BaseHandler":
        self._next = nxt
        return nxt
    
    def handle(self, ticket: Ticket) -> Optional[str]:
        if self._next:
            return self._next.handle(ticket)
        return None


class BillingHandler(BaseHandler):
    def handle(self, ticket: Ticket):
        if ticket.kind == "billing":
            return f"[Billing] handled: {ticket.message}"
        return super().handle(ticket)


class TechHandler(BaseHandler):
    def handle(self, ticket: Ticket) -> Optional[str]:
        if ticket.kind == "tech":
            return f"[Tech] handled: {ticket.message}"
        return super().handle(ticket)


class GeneralHandler(BaseHandler):
    def handle(self, ticket: Ticket) -> Optional[str]:
        if ticket.kind == "general":
            return f"[General] handled: {ticket.message}"
        return super().handle(ticket)


if __name__ == "__main__":
    billing = BillingHandler()
    tech = TechHandler()
    general = GeneralHandler()

    billing.set_next(tech).set_next(general)

    tickets = [
        Ticket("tech", "Robot arm stops mid-trajectory."),
        Ticket("billing", "Invoice mismatch."),
        Ticket("general", "Where do I change my password?"),
        Ticket("unknown", "???"),
    ]

    for t in tickets:
        result = billing.handle(t)
        print(result or "[No handler] escalated")