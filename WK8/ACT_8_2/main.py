# ============================================================
# Exercise 1.4: Online Notification System (Factory Method Pattern)
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. Every notification type (Email, SMS, Push) must have a send()
#      method. We describe that rule once in an abstract class.
#   2. Each notification type is its own small class that fills in
#      send() in its own way.
#   3. Each notification type also gets its own FACTORY -- a class
#      whose only job is to create that one type of notification.
#   4. The client (the code that wants to send a message) only talks
#      to a factory. It never writes Email(), SMS() or Push() itself.
#
# WHY BOTHER? If the client wrote `Email()` directly, it would be
# tied to the Email class. With a factory, the client just says
# "factory, give me a notification" and then calls send(). To add a
# new type later (e.g. WhatsApp) we add one new class + one new
# factory -- the client code does not need to change.
# ============================================================

from abc import ABC, abstractmethod


# ==========================================
# 1. ABSTRACT PRODUCT
# ==========================================
# "Product" = the thing the factory makes (here: a notification).
# This class is a rule book: every notification MUST have send().
# It is abstract, so you cannot create it directly -- you can only
# create classes that inherit from it and fill in send().
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


# ==========================================
# 2. CONCRETE PRODUCTS
# ==========================================
# "Concrete" = a real, usable class. Each one inherits from
# Notification and writes its own version of send().
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending EMAIL: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Sending PUSH notification: {message}")


# ==========================================
# 3. ABSTRACT FACTORY / CREATOR
# ==========================================
# This is the rule book for factories: every factory MUST have a
# create_notification() method that returns a Notification.
# It does not say WHICH notification -- each concrete factory decides.
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass


# ==========================================
# 4. CONCRETE FACTORIES
# ==========================================
# One factory per notification type. Each one builds and returns
# exactly one kind of notification. This is the ONLY place where
# EmailNotification(), SMSNotification() and PushNotification()
# are written.
class EmailFactory(NotificationFactory):
    def create_notification(self):
        return EmailNotification()


class SMSFactory(NotificationFactory):
    def create_notification(self):
        return SMSNotification()


class PushFactory(NotificationFactory):
    def create_notification(self):
        return PushNotification()


# ==========================================
# 5. CLIENT
# ==========================================
# The client only knows about factories and the send() method.
# It never mentions EmailNotification, SMSNotification or
# PushNotification.
#
# __name__ == "__main__" means: only run this block when the file
# is executed directly (python main.py), not when it is imported.
if __name__ == "__main__":
    # Step A: pick a factory (this decides which type we get).
    factory = EmailFactory()
    # Step B: ask the factory to create the notification for us.
    notification = factory.create_notification()
    # Step C: use it. We just call send() -- same call for every type.
    notification.send("Your order has been confirmed.")

    # Same three steps with a different factory -- only the factory
    # on the first line changes.
    factory = SMSFactory()
    notification = factory.create_notification()
    notification.send("Your OTP is 482913.")

    factory = PushFactory()
    notification = factory.create_notification()
    notification.send("You have a new message.")

    # Optional: loop over all factories to show the client code
    # is exactly the same no matter which factory is used.
    print("\n--- Sending the same message through every factory ---")
    for factory in [EmailFactory(), SMSFactory(), PushFactory()]:
        notification = factory.create_notification()
        notification.send("System maintenance tonight at 10 PM.")
