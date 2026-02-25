import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0.0}

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


def check_sufficient_resources(drink: str) -> bool:
    """
    Check if the sufficient resources are available for each drink type

    :param drink: espresso/latte/cappuccino
    """
    ingredients = MENU[drink]["ingredients"]
    for ingredient, amount in ingredients.items():
        if amount > resources[ingredient]:
            print(
                f"Insufficient {ingredient}, need {amount}, have {resources[ingredient]}"
            )
            return False

    return True


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


def check_transaction_successful(money_inserted: float, drink: str) -> bool:
    """
    Check that the user inserted enough money to pay for the chosen drink.

    :param money_inserted: dollar amount from the inserted coins
    :type money_inserted: float
    :param drink: Chosen drink espresso/latte/cappuccino
    :type drink: str
    :return: True if enough money was inserted to pay for drink, False otherwise
    :rtype: bool
    """
    cost_of_drink = MENU[drink]["cost"]
    if money_inserted >= cost_of_drink:
        return True
    else:
        return False


def make_coffee(drink: str) -> None:
    """
    make the selected drink and deduct resources

    :param drink: Chosen drink espresso/latte/cappuccino
    :type drink: str
    """
    ingredients = MENU[drink]["ingredients"]
    for ingredient, amount in ingredients.items():
        # Deduct the amount of each ingredient needed for this drink
        resources[ingredient] -= amount

    # Book the profit for this drink
    resources["money"] += MENU[drink]["cost"]
    print(f"Here is your {drink}. Enjoy!!")


def coffee_machine() -> None:
    """
    Simulate a Coffee Machine
    """
    while True:
        render_banner()

        # 1. Prompt user asking "What would you like (espresson/latte/cappuccino)?"
        choice = input("What would you like (espresso/latte/cappuccino)? ")

        match choice:
            case "off":
                # 2. Turn off coffee machine by entering "off" to the prompt
                print("Coffee Machine turning off!")
                break
            case "report":
                # 3. Print report of all coffee machine resources
                print(
                    f"Water: {resources['water']}ml\n"
                    f"Milk: {resources['milk']}ml\n"
                    f"Coffee: {resources['coffee']}g\n"
                    f"Money: ${resources['money']}\n"
                )

            case "espresso" | "latte" | "cappuccino":
                # 4. Check resources sufficient to make drink order
                if check_sufficient_resources(choice):
                    # 5. Process coins
                    money_inserted = process_coins()
                    # 6. Check transaction successful
                    if check_transaction_successful(money_inserted, choice):
                        print(f"Coins Accepted! Making {choice}\n")
                        # return change
                        if money_inserted > MENU[choice]["cost"]:
                            change = round(money_inserted - MENU[choice]["cost"], 2)
                            print(f"Here is your change: ${change}")
                        # 7. Make Coffee
                        make_coffee(choice)
                    else:
                        print("Sorry that's not enough money. Money refunded.")

            case _:
                # do nothing
                pass

        _ = input("press ENTER to continue.....")


if __name__ == "__main__":
    coffee_machine()
