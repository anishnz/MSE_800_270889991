# ============================================================
# ACT 7.1 - Bank Account Management System
# ============================================================
#
# DEFINITION: Single Inheritance
# -------------------------------
# Single inheritance is a type of inheritance where a CHILD class
# inherits from EXACTLY ONE PARENT (base) class.
#
#          BankAccount        <-- parent (base) class
#               |
#         SavingsAccount      <-- child class (inherits from BankAccount ONLY)
#
# SavingsAccount is a special kind of BankAccount, so it inherits the
# constructor, deposit() and withdraw() behaviour from BankAccount and
# then adds its own extra behaviour (calculate_interest()).
#
# DEFINITION: Method Overriding
# -------------------------------
# SavingsAccount also redefines display_account_details(), which
# REPLACES (overrides) the version defined in BankAccount, while still
# reusing the parent's version internally via super().
# ============================================================


# Define a general class that represents a bank account.
class BankAccount:
	"""Parent (base) class representing a generic bank account."""

	# The constructor runs automatically when a new BankAccount object is created.
	def __init__(self, account_number, customer_name, balance):
		# Store the account number inside the current object.
		self.account_number = account_number
		# Store the customer's name inside the current object.
		self.customer_name = customer_name
		# Store the starting balance inside the current object.
		self.balance = balance

	# Define a method that displays all basic account information.
	def display_account_details(self):
		# Print the account number; self means this particular account object.
		print(f"Account Number: {self.account_number}")
		# Print the customer's name using an f-string to insert its value.
		print(f"Customer Name: {self.customer_name}")
		# Print the balance with exactly two digits after the decimal point.
		print(f"Account Balance: ${self.balance:.2f}")

	# Define a method that adds money to the account.
	def deposit(self, amount):
		# Check that the deposit is a positive amount.
		if amount <= 0:
			# Display an error when the deposit is zero or negative.
			print("Deposit amount must be greater than zero.")
			# Stop this method immediately after the invalid deposit.
			return

		# Add the deposit amount to the current balance.
		self.balance += amount
		# Display the amount that was deposited.
		print(f"Deposited: ${amount:.2f}")
		# Display the balance after the deposit.
		print(f"New Balance: ${self.balance:.2f}")

	# Define a method that removes money from the account.
	def withdraw(self, amount):
		# Check that the withdrawal amount is positive.
		if amount <= 0:
			# Display an error for a zero or negative withdrawal.
			print("Withdrawal amount must be greater than zero.")
		# Check whether the customer is trying to withdraw too much money.
		elif amount > self.balance:
			# Reject the withdrawal when there is not enough money.
			print("Withdrawal denied: insufficient balance.")
		# Run this block only when the withdrawal is valid.
		else:
			# Subtract the withdrawal amount from the current balance.
			self.balance -= amount
			# Display the amount that was withdrawn.
			print(f"Withdrawn: ${amount:.2f}")
			# Display the balance after the withdrawal.
			print(f"New Balance: ${self.balance:.2f}")


# Define SavingsAccount as a child class of BankAccount.
# The "(BankAccount)" in the class definition is what creates the
# INHERITANCE relationship: SavingsAccount is the SUBCLASS (child) and
# BankAccount is the SUPERCLASS (parent). SavingsAccount automatically
# inherits the constructor, deposit method, and withdrawal method,
# without having to redefine any of that logic here.
class SavingsAccount(BankAccount):
	"""Child class that extends BankAccount with interest calculation."""

	# Define extra functionality that is specific to savings accounts.
	def calculate_interest(self, interest_rate):
		# Calculate interest using balance multiplied by rate divided by 100.
		interest = self.balance * interest_rate / 100
		# Display the interest rate and the calculated interest amount.
		print(f"Interest at {interest_rate:.2f}%: ${interest:.2f}")
		# Return the calculated value so other code can use it.
		return interest

	# METHOD OVERRIDING: SavingsAccount provides its OWN version of
	# display_account_details() instead of just reusing BankAccount's
	# version untouched. It still calls the parent's version via
	# super() so the common fields are not duplicated here.
	def display_account_details(self):
		# Identify this object as a Savings Account.
		print("Account Type: Savings Account")
		# super() gives access to the parent class (BankAccount).
		# Call the parent class method to display the common details
		# (account number, customer name, balance) before returning.
		super().display_account_details()


# ------------------------------------------------------------
# Demonstration / Test code
# ------------------------------------------------------------
# NOTE: unlike some of the other exercises in this repo, this script
# runs its demonstration code directly at module level (there is no
# "if __name__ == '__main__':" guard). It still produces the same
# output when executed directly with "python main.py".

# Create a SavingsAccount object with John's account information.
savings_account = SavingsAccount("SA1001", "John", 5000)

# Print a heading before showing the starting account information.
print("Initial Account Details")
# Call the account method that displays John's account details.
savings_account.display_account_details()

# Print a heading; \n creates a blank line before the heading.
print("\nAfter Deposit")
# Deposit $1,000 into the savings account.
savings_account.deposit(1000)

# Print a heading before the withdrawal operation.
print("\nAfter Withdrawal")
# Withdraw $500 from the savings account.
savings_account.withdraw(500)

# Print a heading before calculating interest.
print("\nInterest Calculation")
# Calculate interest using an interest rate of 5 percent.
savings_account.calculate_interest(5)

# Print a heading before showing the final account information.
print("\nFinal Account Details")
# Display the account details after all transactions are complete.
savings_account.display_account_details()