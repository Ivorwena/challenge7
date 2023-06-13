"""
This module starts the whole program
"""
import os
import random
from customer import Customer


def print_possibilities():
    """Prints options, what you can do"""
    print("Hello. What would you like to do?")
    print("1 - print your account details")
    print("2 - deposit money")
    print("3 - withdraw money")
    print("4 - exit")


def choose_possibility():
    """Lets the user chose what to do"""
    k = ["1", "2", "3", "4"]
    a = input()
    if a not in k:
        while a not in k:
            print("That is not such option - try again.")
            print_possibilities()
            a = input()
    return int(a)


def pass_choice(a, your_acc):
    """Passes on user's choice"""
    if a == 1:
        your_acc.print_client()
    elif a == 2:
        m = prepare_to_deposit()
        print(your_acc.deposit(m))
    elif a == 3:
        your_acc.prepare_to_withdraw()
        print(f"Your account balance has been updated: {your_acc.balance}$.")
    input("Press ENTER to continue...")


def prepare_to_deposit():
    """Prepares to deposit money"""
    how_much = input("How much money do you want to deposit? [$]\n")
    if not how_much.isnumeric():
        while not how_much.isnumeric():
            print("That was not a whole number")
            how_much = input("How much money do you want to deposit? [$]\n")
    return int(how_much)


def start(your_acc):
    """Starts whole program"""
    n = 0
    while n != 4:
        os.system('clear')
        print_possibilities()
        n = choose_possibility()
        os.system('clear')
        pass_choice(n, your_acc)


def create_customer():
    """Creates customer"""
    print("Hi! You seem to be new here - let me help you~")
    name = input("I need to know your name: ")
    if not name.isalpha():
        while not name.isalpha():
            print("That is not a name.")
            name = input("I need to know your name: ")
    surname = input("I need to know your surname: ")
    if not surname.isalpha():
        while not surname.isalpha():
            print("That is not a surname.")
            surname = input("I need to know your surname: ")
    money = input("How much money do you want to deposit? [$] ")
    if not money.isnumeric():
        while not money.isnumeric():
            print("You must pass numeric value, should be whole number.")
            money = input("How much money do you want to deposit? [$] ")
    money = int(money)
    your_acc = Customer(name, surname, money)
    print("You just created your bank account. Here are your details")
    your_acc.print_client()
    return your_acc


custom = create_customer()
input("Press ENTER to continue...")
start(custom)
