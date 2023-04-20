from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine=MoneyMachine()
my_coffee_machine=CoffeeMaker()
menu=Menu()
items=menu.get_items()
is_on=True
while is_on:
    choice=input(f"What would you like ? ({items}) :\n")

    if(choice=='off'):
        is_on=False
    elif(choice=='report'):
        my_coffee_machine.report()
        my_money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if(my_coffee_machine.is_resource_sufficient(drink)):
            if (my_money_machine.make_payment(drink.cost)):
                my_coffee_machine.make_coffee(drink)
