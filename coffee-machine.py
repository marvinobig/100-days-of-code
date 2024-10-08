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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

available_coins = 0
profit = 0

def add_coins(coin_bank):
    while True:
        try:
            coins = float(input("Insert coins: (0.25, 0.10, 0.05, 0.01) "))

            if coins not in [0.25, 0.10, 0.05, 0.01]:
                raise Exception("Accepted coins include 0.25, 0.10, 0.05 and 0.01")

            number_of_coin = int(input(f"How many ${coins} do you want to add? "))

            if number_of_coin > 0:
                coin_bank += (coins * number_of_coin)
            else:
                continue

            coin_confirmation = input("Do you want to add more coins? (yes/no) ")

            if coin_confirmation in ['no', 'n']:
                break
        except ValueError:
            print("The machine does not take anything but coins")
            continue
        except Exception as coin_err:
            print(str(coin_err))
            continue

    return coin_bank

def print_report(available_resources, coins):
    for ingredient, value in available_resources.items():
        print(f"{ingredient.title()}: {value}g") if ingredient == 'coffee' else print(f"{ingredient.title()}: {value}ml")
    print(f"Money: ${coins:.2f}")

def check_resources(choice, menu, available_resources):
    for ingredient in MENU[user_choice]['ingredients'].keys():
        if available_resources[ingredient] < menu[choice]['ingredients'][ingredient]:
            raise Exception(f"Sorry there is not enough {ingredient}.")


while True:
    try:
        user_choice = input("What would you like? (espresso/latte/cappuccino) ").strip().lower()

        if user_choice == 'off':
            break
        elif user_choice == 'report':
            print_report(resources, available_coins)
            continue

        if user_choice not in MENU:
            print("The only available items on the menu include espresso, latte and cappuccino")
            continue

        available_coins = add_coins(available_coins)

        if available_coins < MENU[user_choice]['cost']:
            print(f"You only have ${available_coins:.2f} which isn't enough to buy the {user_choice} which costs ${MENU[user_choice]['cost']:.2f}. Money refunded.")
            available_coins = 0
            continue

        check_resources(user_choice, MENU, resources)

        change = available_coins - MENU[user_choice]['cost']

        for key in MENU[user_choice]['ingredients'].keys():
            resources[key] = resources[key] - MENU[user_choice]['ingredients'][key]

        available_coins = 0

        print(f"Here is your {user_choice} and ${change:.2f} in change. Enjoy!") if change > 0.0 else print(f"Here is your {user_choice}. Enjoy!")
    except Exception as err:
        print(str(err))
        continue
