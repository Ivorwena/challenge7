from person import Person
from random import randint

"""This is a class implementation, class Customer"""


class Customer(Person):
    def __init__(self, firstname, lastname, balance):
        super(Customer, self).__init__(firstname, lastname)
        self.account_number = random.randint(1000000, 9999999)
        self.balance = balance

    def print_client(self):
        print(f"Name: {self.firstname}\nSurname: {self.lastname}\nAccount number: {self.account_number}.")
        print(f"Balance: {self.balance}$.")

    def deposit(self, add):
        self.balance = self.balance + add
        return f"New account balance: {self.balance}$."

    def withdraw(self, take):
        self.balance = self.balance - int(take)
        return self.balance

    def prepare_to_withdraw(self):
        if self.balance == 0:
            print("You don't have enough money.")
        else:
            how_much = input("How much money do you want to withdraw? (accept only whole number, could be 0) [$]\n")
            k = 0
            while k < 2:
                if not how_much.isnumeric():
                    while not how_much.isnumeric():
                        print("That was not a whole number")
                        how_much = input("How much money do you want to withdraw? (could be 0) [$]\n")
                else:
                    k += 1
                how_much2 = int(how_much)
                if how_much2 > self.balance:
                    print("You don't have enough money.")
                    how_much = input("How much money do you want to withdraw? (could be 0) [$]\n")
                    print("\n")
                    self.print_client()
                else:
                    k += 1
                if k < 2:
                    k = 0
            self.withdraw(how_much2)
