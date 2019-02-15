# # Create a BankAccount class

class BankAccount:

# Every bank account should have balance and interest_rate attributes (instance variables)
# Since we want these fields to be set for every account, you'll need to add an __init__ method to your class
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

# At this point you should test out creating an instance of your class to make sure it works
# Define a __str__() instance method so you can print bank account objects and see a nice, meaningful string.
# Make sure this method returns a string, rather than printing it!

    def __str__(self):
        return "Your balanace is {} and your interest rate is {}%.".format(self.balance, self.interest_rate)

# Your class should have an instance method called deposit that accepts one amount argument
# and adds that amount to the total balance

    def deposit(self, d_amount):
        self.balance += d_amount
        return self.balance

# Test out your method by calling it on an instance of your class
# There should be a withdraw instance method that accepts one amount argument and subtracts it from
# the total balance
    def withdraw(self, w_amount):
        self.balance -= w_amount
        return self.balance

# Don't forget to test it out!
# Finally, there should be a gain_interest instance method that increases the total balance
# according to the interest rate.
    def gain_interest(self):
        self.balance *= (self.interest_rate/100) + 1
        return self.balance


account_1 = BankAccount(200, 6)

print(account_1)

account_1.deposit(10)

print(account_1)

account_1.withdraw(30)

print(account_1)

account_1.gain_interest()

print(account_1)
