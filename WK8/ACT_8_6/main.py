# ============================================================
# Exercise 1.1: Car Customisation (Decorator Pattern)
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. A basic car costs $25,000. Customers can add GPS, a sunroof, leather
#      seats and a premium sound system in any combination.
#   2. Making one class per combination (CarWithGPS, CarWithGPSAndSunroof,
#      ...) would need 2 x 2 x 2 x 2 = 16 classes, and every new feature would
#      double that number.
#   3. Instead, each feature is a small DECORATOR class. A decorator IS a Car
#      (so it can be used anywhere a car is expected) and it HAS a Car inside
#      it (the car it is wrapping).
#   4. A decorator answers get_description() and get_cost() by asking the
#      wrapped car first, then adding its own feature name and price.
#   5. Wrapping decorators around each other stacks the features:
#          SunroofDecorator(GPSDecorator(BasicCar()))
#      Cost = 25,000 (basic) + 500 (GPS) + 1,000 (sunroof) = 26,500.
#
# WHY BOTHER? Four feature classes cover every combination, features are
# chosen at run time, and a new feature is one new class with no changes to
# the existing ones.
# ============================================================

from abc import ABC, abstractmethod


# ==========================================
# 1. COMPONENT - what every car (and every decorator) can do
# ==========================================
class Car(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    def show_car(self):
        print(f"Car  : {self.get_description()}")
        print(f"Cost : ${self.get_cost():,}")


# ==========================================
# 2. CONCRETE COMPONENT - the plain car that gets decorated
# ==========================================
class BasicCar(Car):
    def get_description(self):
        return "Basic Car"

    def get_cost(self):
        return 25000


# ==========================================
# 3. BASE DECORATOR - a Car that wraps another Car
# ==========================================
class CarDecorator(Car):
    def __init__(self, car):
        self._car = car

    def get_description(self):
        return self._car.get_description()

    def get_cost(self):
        return self._car.get_cost()


# ==========================================
# 4. CONCRETE DECORATORS - one per optional feature
# ==========================================
class GPSDecorator(CarDecorator):
    def get_description(self):
        return self._car.get_description() + ", GPS"

    def get_cost(self):
        return self._car.get_cost() + 500


class SunroofDecorator(CarDecorator):
    def get_description(self):
        return self._car.get_description() + ", Sunroof"

    def get_cost(self):
        return self._car.get_cost() + 1000


class LeatherSeatsDecorator(CarDecorator):
    def get_description(self):
        return self._car.get_description() + ", Leather Seats"

    def get_cost(self):
        return self._car.get_cost() + 1500


class PremiumSoundDecorator(CarDecorator):
    def get_description(self):
        return self._car.get_description() + ", Premium Sound System"

    def get_cost(self):
        return self._car.get_cost() + 800


# ==========================================
# Demonstration
# ==========================================
if __name__ == "__main__":
    print("--- Basic car (no features) ---")
    BasicCar().show_car()

    print("\n--- Basic car + GPS ---")
    GPSDecorator(BasicCar()).show_car()

    print("\n--- Basic car + GPS + Sunroof ---")
    SunroofDecorator(GPSDecorator(BasicCar())).show_car()

    print("\n--- Fully loaded car (all four features) ---")
    full = PremiumSoundDecorator(
        LeatherSeatsDecorator(
            SunroofDecorator(
                GPSDecorator(BasicCar())
            )
        )
    )
    full.show_car()

    # Features can be added one at a time, at run time, as the customer decides.
    print("\n--- Customer adds features step by step ---")
    car = BasicCar()
    print(f"Start          -> ${car.get_cost():,}")
    car = LeatherSeatsDecorator(car)
    print(f"+ Leather Seats -> ${car.get_cost():,}")
    car = PremiumSoundDecorator(car)
    print(f"+ Premium Sound -> ${car.get_cost():,}")
    car.show_car()

    # Each wrapper only adds its own price, so the stacking order does not
    # change the total (only the order of the names in the description).
    print("\n--- Order of decorators does not change the cost ---")
    a = SunroofDecorator(GPSDecorator(BasicCar()))
    b = GPSDecorator(SunroofDecorator(BasicCar()))
    print(f"GPS then Sunroof : ${a.get_cost():,}")
    print(f"Sunroof then GPS : ${b.get_cost():,}")
