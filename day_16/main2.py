#This is a copy of main.py but done by myself
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cofee_machine = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True 
menu = Menu()


while is_on:
    options = menu.get_items()
    election = input(f"What do you want {options}? ")
    if election == "off":
        is_on = False
    elif election == "report":
        cofee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(election)
        if cofee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                cofee_machine.make_coffee(drink)


