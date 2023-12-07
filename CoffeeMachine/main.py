MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_resources():
    """Returns True if there are insufficient resources"""
    if MENU[answer]["ingredients"]["water"] > resources["water"]:
        print("Insufficient water.")
        return True
    if MENU[answer]["ingredients"]["milk"] > resources["milk"]:
        print("Insufficient milk.")
        return True
    if MENU[answer]["ingredients"]["coffee"] > resources["coffee"]:
        print("Insufficient coffee.")
        return True
    else:
        print(f"Please insert ${MENU[answer]['cost']}")
        return False


def take_money():
    """Return the total cost of the drink if sufficient money is inserted"""
    quarters = int(input("How many quarters would you like to insert? "))
    dimes = int(input("How many dimes would you like to insert? "))
    nickles = int(input("How many nickles would you like to insert? "))
    pennies = int(input("How many pennies would you like to insert? "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    print(f"You've inserted ${total}")
    if total > MENU[answer]['cost']:
        change = total - MENU[answer]['cost']
        print(f"Here is ${round(change, 2)} in change.")
        return MENU[answer]['cost']
    elif total == MENU[answer]['cost']:
        print("Thank you.")
        return MENU[answer]['cost']
    else:
        print("Sorry that is not enough money. Money refunded.")
        return 0


def make_coffee(drink, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")


servicing = True
insufficient = False

while servicing:
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    if answer == "report":
        print(resources)
    elif answer == "off":
        servicing = False
        print("Goodbye.")
    elif answer == "espresso":
        insufficient = check_resources()
        if not insufficient:
            sale = take_money()
            resources["money"] += sale
            if sale == 0:
                insufficient = True
            make_coffee(answer, MENU[answer]["ingredients"])
            print(resources)
    elif answer == "latte":
        insufficient = check_resources()
        if not insufficient:
            sale = take_money()
            resources["money"] += sale
            if sale == 0:
                break
            make_coffee(answer, MENU[answer]["ingredients"])
            print(resources)
    elif answer == "cappuccino":
        insufficient = check_resources()
        if not insufficient:
            sale = take_money()
            resources["money"] += sale
            if sale == 0:
                insufficient = True
                break
            make_coffee(answer, MENU[answer]["ingredients"])
            print(resources)
    else:
        print("invalid answer. Try again.")
