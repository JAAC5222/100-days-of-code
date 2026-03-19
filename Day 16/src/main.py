from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    option = input(f"Welcome to the Coffee Maker! What would you like? ({menu.get_items()}): ")

    if option == "report":
        coffe_maker.report()
        money_machine.report()
        continue
    elif option == "off":
        print("Shutting down the Coffee Maker. Goodbye!")
        break

    option = menu.find_drink(option)

    while option is None:
        option = menu.find_drink(input(f"Incorrect option, please select a correct drink ({menu.get_items()}): "))

    if coffe_maker.is_resource_sufficient(option) and money_machine.make_payment(option.cost):
        coffe_maker.make_coffee(option)
