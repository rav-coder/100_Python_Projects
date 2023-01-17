from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

running = True
coffee_maker = CoffeeMaker()
menu = Menu()
money_mach = MoneyMachine()

while running:
    user_sel = input(f"What would you like? ({menu.get_items()}): ").lower()

    if user_sel == 'report':
        coffee_maker.report()
        money_mach.report()
    elif user_sel == 'off':
        running = False
    else:
        coffee_sel = menu.find_drink(user_sel)
        if coffee_sel:
            if coffee_maker.is_resource_sufficient(coffee_sel):
                if money_mach.make_payment(coffee_sel.cost):
                    coffee_maker.make_coffee(coffee_sel)







