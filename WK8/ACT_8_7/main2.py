# Target
class Payment:
    def pay(self, amount):
        raise NotImplementedError


# Adaptee
class OldPaymentSystem:
    def make_payment(self, amount):
        print(f"Payment of ${amount} made using Old Payment System.")


# Adapter using Multiple Inheritance
class PaymentAdapter(Payment, OldPaymentSystem):

    def pay(self, amount):
        self.make_payment(amount)


# Client
payment = PaymentAdapter()

payment.pay(500)