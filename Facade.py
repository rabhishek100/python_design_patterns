"""

definition: simply access to a codebase by providing an easy to use api

"""

from dataclasses import dataclass


# -------- Subsystem (messy internals) --------
class InventoryService:
    def reserve(self, sku: str, qty: int) -> None:
        print(f"[inventory] reserved {qty} of {sku}")

class PaymentGateway:
    def charge(self, user_id: str, amount: float) -> str:
        txn_id = f"TXN-{user_id}-{int(amount * 100)}"
        print(f"[payment] charged ₹{amount:.2f}, txn={txn_id}")
        return txn_id

class ShippingService:
    def create_shipment(self, user_id: str, sku: str, qty: int) -> str:
        ship_id = f"SHIP-{user_id}-{sku}-{qty}"
        print(f"[shipping] created shipment {ship_id}")
        return ship_id

class EmailService:
    def send_receipt(self, user_id: str, txn_id: str, ship_id: str) -> None:
        print(f"[email] sent receipt to {user_id} for {txn_id} and {ship_id}")


# -------- Facade (clean front door) --------
@dataclass
class OrderFacade:
    inventory: InventoryService
    payments: PaymentGateway
    shipping: ShippingService
    email: EmailService

    def place_order(self, user_id: str, sku: str, qty: int, amount: float) -> dict:
        # Client calls ONE method; facade coordinates the rest.
        self.inventory.reserve(sku, qty)
        txn_id = self.payments.charge(user_id, amount)
        ship_id = self.shipping.create_shipment(user_id, sku, qty)
        self.email.send_receipt(user_id, txn_id, ship_id)
        return {"txn_id": txn_id, "ship_id": ship_id}


if __name__ == "__main__":
    facade = OrderFacade(
        inventory=InventoryService(),
        payments=PaymentGateway(),
        shipping=ShippingService(),
        email=EmailService(),
    )

    result = facade.place_order(user_id="abhishek", sku="SKU123", qty=2, amount=499.0)
    print("result:", result)
