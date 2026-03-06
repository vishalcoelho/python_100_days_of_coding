from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

import os


BANNER = r"""
  ____       __  __             __  __            _     _
 / ___|___  / _|/ _| ___  ___  |  \/  | __ _  ___| |__ (_)_ __   ___
| |   / _ \| |_| |_ / _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
| |__| (_) |  _|  _|  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
 \____\___/|_| |_|  \___|\___| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
"""


def render_banner() -> None:
    """Render the banner on each loop

    :returns None:
    """
    _ = os.system("clear")
    print(BANNER)

def process_coins() -> float:
    """
    Prompt user for coins

    :return: Total dollar value of coins inserted
    :rtype: float
    """
    print("Insert Coins...\n")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total_coins_inserted = (
        quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    )

    return total_coins_inserted

def check_transaction_successful(money_inserted: float, cost_of_drink: float) -> bool:
    """
    Check that the user inserted enough money to pay for the chosen drink.

    :param money_inserted: dollar amount from the inserted coins
    :type money_inserted: float
    :param cost_of_drink: Cost of chosen drink espresso/latte/cappuccino
    :type drink: float
    :return: True if enough money was inserted to pay for drink, False otherwise
    :rtype: bool
    """
    if money_inserted >= cost_of_drink:
        return True
    else:
        return False

def coffee_machine() -> None:
    """
    Simulate a Coffee Machine
    """

    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        render_banner()

        # 1. Prompt user asking "What would you like (espresson/latte/cappuccino)?"
        choice = input(f"What would you like ({menu.get_items()})? ")

        match choice:
            case "off":
                # 2. Turn off coffee machine by entering "off" to the prompt
                print("Coffee Machine turning off!")
                break
            case "report":
                # 3. Print report of all coffee machine resources
                coffee_maker.report()
                money_machine.report()
            case _:
                drink = menu.find_drink(choice)
                if drink :
                    # 4. Check resources sufficient to make drink order
                    if coffee_maker.is_resource_sufficient(drink):
                        # 5, 6. Process coins, check transaction successful
                        if money_machine.make_payment(drink.cost):
                            # 7. Make Coffee
                            coffee_maker.make_coffee(drink)
                else:
                    # do nothing
                    pass

        _ = input("press ENTER to continue.....")


if __name__ == "__main__":
    coffee_machine()
