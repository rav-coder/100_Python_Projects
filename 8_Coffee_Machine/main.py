import copy

from coffee_info import *

# 1. Print report of all system resources
LIQUID = 'ml'
SOLID = 'g'
DOLLAR = '$'


def print_report(money):
    """ Prints the resources available in the machine."""
    for res_type in resources:
        if res_type in ("water", "milk"):
            tag = 'ml'
        elif res_type == "coffee":
            tag = 'g'
        else:
            tag = ''
        print(f"{res_type.capitalize()}: {resources[res_type]}{tag}")
    print(f"Money: {DOLLAR}{money}")


# 2. Prompt user
def print_options():
    option = ''
    for coffee_name in MENU:
        option += coffee_name + '/'
    return option[:-1]


running = True

while running:
    coffee_sel = input(f"What would you like? ({print_options()}): ").lower()
    total_cash = 0

    if coffee_sel == 'report':
        print_report(total_cash)
    elif coffee_sel == 'off':
        running = False
    else:
        flag = False
        for key in MENU:
            if coffee_sel == key:
                # 3.5 Check enough resources
                ingredients = MENU[key]['ingredients']
                new_resources = copy.deepcopy(resources)
                for resource_type in ingredients:
                    if ingredients[resource_type] > resources[resource_type]:
                        print(f"Sorry there is not enough {resource_type}.")
                        break
                    else:
                        new_resources[resource_type] = resources[resource_type] - ingredients[resource_type]
                else:
                    # 3. Process coins.
                    print("Please insert coins.")
                    quarters = int(input("How many quarters?: "))
                    dimes = int(input("How many dimes?: "))
                    nickles = int(input("How many nickles?: "))
                    pennies = int(input("How many pennies?: "))

                    total_cash = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

                    # 4. Check transaction successful
                    cost = MENU[key]['cost']
                    if cost > total_cash:
                        print("Sorry that's not enough money. Money refunded.")
                        break

                    # 5. Make coffee
                    resources = new_resources
                    total_cash -= cost
                    print(f"Here is {DOLLAR}{total_cash} in change.")
                    print(f"Here is your {coffee_sel}. Enjoy!")
            else:
                if not flag:
                    print("Invalid choice! Try again")
                flag = True






