from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


isRunning = True

menuObj = Menu()
mmObj = MoneyMachine()
cmObj = CoffeeMaker()

while isRunning:

    items = menuObj.get_items()
    itemsList = items.split('/')
    # print(itemsList)

    user_choice = (input(f"Please Select an Option"
                         f" \n1. {itemsList[0].title()} \n2. {itemsList[1].title()}"
                         f" \n3. {itemsList[2].title()}\n")).lower()

    if user_choice == 'off':
        isRunning = False
    elif user_choice == 'report':
        cmObj.report()
        mmObj.report()
    else:
        user_input = menuObj.find_drink(user_choice)
        if cmObj.is_resource_sufficient(user_input):
            if mmObj.make_payment(user_input.cost):
                cmObj.make_coffee(user_input)
            else:
                pass

    print("----------------------------------------------")
