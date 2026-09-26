# Task 1: Create the Observer

class Observer:
    def update(self, price):
        pass


# Task 2: Create the Concrete Observer

class Investor(Observer):

    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(f"{self.name} received new stock price: {price}")


# Task 3: Create the Subject

class Stock:

    def __init__(self, price):
        self.price = price
        self.investors = []

    # Subscribe an investor
    def subscribe(self, investor):
        self.investors.append(investor)

    # Notify all investors
    def notify(self):
        for investor in self.investors:
            investor.update(self.price)

    # Change stock price
    def set_price(self, price):
        self.price = price
        self.notify()


# Task 4: Create investors

investor1 = Investor("Ali")
investor2 = Investor("John")
investor3 = Investor("Sita")


# Create Stock
stock = Stock(100)


# Subscribe investors
stock.subscribe(investor1)
stock.subscribe(investor2)
stock.subscribe(investor3)


# Change stock price
stock.set_price(105)