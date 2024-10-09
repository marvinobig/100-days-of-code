class CoffeeMachine:
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
    balance = 0
    profit = 0
    coffee_choice = ""
    change = 0

    def add_coins(self):
        while True:
            try:
                coins = float(input("Insert coins: (0.25, 0.10, 0.05, 0.01) "))

                if coins not in [0.25, 0.10, 0.05, 0.01]:
                    raise Exception("Accepted coins include 0.25, 0.10, 0.05 and 0.01")

                number_of_coin = int(input(f"How many ${coins} do you want to add? "))

                if number_of_coin > 0:
                    self.balance += (coins * number_of_coin)
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

        return self.balance

    def print_report(self):
        for ingredient, value in self.resources.items():
            print(f"{ingredient.title()}: {value}g") if ingredient == 'coffee' else print(
                f"{ingredient.title()}: {value}ml")
        print(f"Money: ${self.balance:.2f}")

    def check_resources(self):
        for ingredient in self.MENU[self.coffee_choice]['ingredients'].keys():
            if self.resources[ingredient] < self.MENU[self.coffee_choice]['ingredients'][ingredient]:
                raise Exception(f"Sorry there is not enough {ingredient}.")

    def add_choice(self, user_coffee_choice):
        self.coffee_choice = user_coffee_choice

    def make_coffee(self):
        self.change = self.balance - self.MENU[self.coffee_choice]['cost']

        for resource in self.MENU[self.coffee_choice]['ingredients'].keys():
            self.resources[resource] = self.resources[resource] - self.MENU[self.coffee_choice]['ingredients'][resource]

        self.balance = 0

        print(
            f"Here is your {self.coffee_choice} and ${self.change:.2f} in change. Enjoy!") if self.change > 0.0 else print(
            f"Here is your {self.coffee_choice}. Enjoy!")