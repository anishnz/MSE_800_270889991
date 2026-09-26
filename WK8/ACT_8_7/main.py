#Exercise — Payment System You are developing an online shopping application 
#that supports different payment systems. The application expects every payment 
#service to provide a pay(amount) method. However, an existing third-party
#payment system provides a make_payment(amount) method instead. Since the 
#third-party system cannot be modified, you need to create an Adapter that 
#allows the existing payment system to work with the application's expected 
#interface. Implement the Adapter 17 Pattern using Combination (Composition),
#where the Adapter contains an object of the existing payment system.
#As an extension, implement the same solution using Multiple Inheritance. 
#The final program should allow the client to call pay(500) and produce the 
#message "Payment of $500 made using Old Payment System." Identify the Target,
#Adaptee, and Adapter classes in your implementation.



# Target
# The interface expected by the application
class Payment:
    def pay(self, amount):
        raise NotImplementedError


# Adaptee
# Existing third-party payment system
class OldPaymentSystem:
    def make_payment(self, amount):
        print(f"Payment of ${amount} made using Old Payment System.")


# Adapter
# Converts make_payment() into pay()
class PaymentAdapter(Payment):
    def __init__(self, old_payment_system):
        self.old_payment_system = old_payment_system

    def pay(self, amount):
        self.old_payment_system.make_payment(amount)


# Client
old_system = OldPaymentSystem()
payment = PaymentAdapter(old_system)

payment.pay(500)


