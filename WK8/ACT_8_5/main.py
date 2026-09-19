# ============================================================
# Exercise 3.1: Build a Travel Package (Builder Pattern)
# ============================================================
#
# SIMPLE LOGIC (step by step):
#   1. A travel package has many parts: destination, hotel, transport,
#      meal plan, activities and insurance. One constructor taking all of
#      them at once is hard to read and easy to get in the wrong order.
#   2. So we build the package step by step. TravelPackageBuilder has one
#      set_/add_ method per part. Each method returns `self`, which lets us
#      chain the calls one after another.
#   3. Parts the customer skips get a sensible default (no meals, no
#      activities, no insurance), so build() always makes a complete object.
#   4. build() creates the finished TravelPackage from what was collected.
#   5. TravelDirector holds ready-made "recipes" (budget, family, luxury).
#      It knows the ORDER and the VALUES; the builder knows HOW to build.
#
# WHY BOTHER? The same builder can make many different packages, and the
# code that builds them reads like a sentence.
# ============================================================


# ==========================================
# 1. PRODUCT - the complex object being built
# ==========================================
class TravelPackage:
    def __init__(self, destination, hotel, transport, meal_plan, activities, insurance):
        self.destination = destination
        self.hotel = hotel
        self.transport = transport
        self.meal_plan = meal_plan
        self.activities = activities
        self.insurance = insurance

    def show_package(self):
        activities = ", ".join(self.activities) if self.activities else "None"
        print(f"Destination : {self.destination}")
        print(f"Hotel       : {self.hotel}")
        print(f"Transport   : {self.transport}")
        print(f"Meal plan   : {self.meal_plan}")
        print(f"Activities  : {activities}")
        print(f"Insurance   : {'Yes' if self.insurance else 'No'}")


# ==========================================
# 2. BUILDER - creates the package step by step
# ==========================================
class TravelPackageBuilder:
    HOTELS = ("3-star", "4-star", "5-star")
    TRANSPORTS = ("Flight", "Train", "Bus")
    MEAL_PLANS = ("None", "Breakfast", "Full Board")
    ACTIVITIES = ("City Tour", "Museum", "Adventure Tour")

    def __init__(self):
        self.destination = None
        self.hotel = None
        self.transport = None
        self.meal_plan = "None"
        self.activities = []
        self.insurance = False

    def set_destination(self, destination):
        self.destination = destination
        return self

    def set_hotel(self, hotel):
        self._check(hotel, self.HOTELS, "hotel")
        self.hotel = hotel
        return self

    def set_transport(self, transport):
        self._check(transport, self.TRANSPORTS, "transport")
        self.transport = transport
        return self

    def set_meal_plan(self, meal_plan):
        self._check(meal_plan, self.MEAL_PLANS, "meal plan")
        self.meal_plan = meal_plan
        return self

    def add_activity(self, activity):
        self._check(activity, self.ACTIVITIES, "activity")
        if activity not in self.activities:
            self.activities.append(activity)
        return self

    def set_insurance(self, insurance):
        self.insurance = insurance
        return self

    def build(self):
        # Destination, hotel and transport have no sensible default.
        if not (self.destination and self.hotel and self.transport):
            raise ValueError("A package needs a destination, hotel and transport.")
        return TravelPackage(
            self.destination,
            self.hotel,
            self.transport,
            self.meal_plan,
            list(self.activities),  # copy, so later changes to the builder don't alter this package
            self.insurance,
        )

    @staticmethod
    def _check(value, allowed, label):
        if value not in allowed:
            raise ValueError(f"Invalid {label} '{value}'. Choose from: {', '.join(allowed)}")


# ==========================================
# 3. DIRECTOR - ready-made package recipes
# ==========================================
class TravelDirector:
    def build_budget_package(self, builder):
        return (
            builder.set_destination("Auckland")
            .set_hotel("3-star")
            .set_transport("Bus")
            .build()
        )

    def build_family_package(self, builder):
        return (
            builder.set_destination("Sydney")
            .set_hotel("4-star")
            .set_transport("Flight")
            .set_meal_plan("Breakfast")
            .add_activity("City Tour")
            .add_activity("Museum")
            .set_insurance(True)
            .build()
        )

    def build_luxury_package(self, builder):
        return (
            builder.set_destination("Melbourne")
            .set_hotel("5-star")
            .set_transport("Flight")
            .set_meal_plan("Full Board")
            .add_activity("City Tour")
            .add_activity("Museum")
            .add_activity("Adventure Tour")
            .set_insurance(True)
            .build()
        )


# ==========================================
# Demonstration
# ==========================================
if __name__ == "__main__":
    director = TravelDirector()

    print("--- Budget package (built by the director) ---")
    director.build_budget_package(TravelPackageBuilder()).show_package()

    print("\n--- Family package (built by the director) ---")
    director.build_family_package(TravelPackageBuilder()).show_package()

    print("\n--- Luxury package (built by the director) ---")
    director.build_luxury_package(TravelPackageBuilder()).show_package()

    # A custom package built directly, step by step, without the director.
    print("\n--- Custom package (built step by step by the customer) ---")
    custom = (
        TravelPackageBuilder()
        .set_destination("Melbourne")
        .set_hotel("4-star")
        .set_transport("Train")
        .set_meal_plan("Full Board")
        .add_activity("Adventure Tour")
        .set_insurance(True)
        .build()
    )
    custom.show_package()

    # Invalid choices are rejected while building.
    print("\n--- Invalid choice is rejected ---")
    try:
        TravelPackageBuilder().set_hotel("2-star")
    except ValueError as error:
        print("Error:", error)
