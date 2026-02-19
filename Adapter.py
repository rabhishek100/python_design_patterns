"""

    definition: create an adapter class to adapt one interface to match another interface without changing the original interfaces

"""

from abc import ABC, abstractmethod


class PayCustomer(ABC):

    @abstractmethod
    def make_customer_payment(self, amount: float) -> None:
        pass


class PaymentProcessor(ABC):

    @abstractmethod
    def send_money(self, amount: float) -> None:
        pass


class PaymentProcessorAdapter(PayCustomer):

    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def make_customer_payment(self, amount: float) -> None:
        self.payment_processor.send_money(amount)



class ConcretePaymentProcessor(PaymentProcessor):

    def send_money(self, amount: float) -> None:
        print(f"Money {amount} sent!")



class Checkout:

    def __init__(self, pay_customer: PayCustomer):
        self.pay_customer = pay_customer

    def pay(self, amount: float) -> None:
        self.pay_customer.make_customer_payment(amount)



if __name__ == "__main__":

    pay_customer: PayCustomer = PaymentProcessorAdapter(ConcretePaymentProcessor())

    checkout: Checkout = Checkout(pay_customer)

    checkout.pay(100)
