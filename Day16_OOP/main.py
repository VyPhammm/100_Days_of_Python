from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffmaker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

is_on = True
while is_on :
    chose = input(f"What would you like ? ({menu.get_items()})")
    if chose == "report" :
        coffmaker.report()
        money.report()
    elif chose == "off" :
        is_on = False
    else :
        drink = menu.find_drink(chose)
        if coffmaker.is_resource_sufficient(drink) and money.make_payment(drink.cost) :
            coffmaker.make_coffee(drink)