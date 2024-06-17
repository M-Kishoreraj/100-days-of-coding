from menu import Menu, MenuItem  # Importing the Menu and MenuItem classes from the menu module
from coffee_maker import CoffeeMaker  # Importing the CoffeeMaker class from the coffee_maker module
from money_machine import MoneyMachine  # Importing the MoneyMachine class from the money_machine module

# Creating instances of MoneyMachine, CoffeeMaker, and Menu classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True  # Variable to control the while loop, allowing the coffee machine to be on or off

while is_on:
    option = menu.get_items()  # Getting the list of available drinks
    choice = input(f"What do you want to have? ({option})")  # Prompting user for their choice of drink

    if choice == "off":  # If user inputs "off", turn off the coffee machine
        is_on = False
    elif choice == "report":  # If user inputs "report", print the reports of the coffee maker and money machine
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)  # Finding the drink object corresponding to the user's choice
        # Check if there are enough resources to make the drink and if the payment is successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)  # Make the coffee if resources and payment are sufficient
