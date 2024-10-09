from coffee_machine_class import CoffeeMachine

machine = CoffeeMachine()

while True:
    try:
        user_choice = input("What would you like? (espresso/latte/cappuccino) ").strip().lower()

        if user_choice == 'off':
            break
        elif user_choice == 'report':
            machine.print_report()
            continue

        if user_choice not in machine.MENU:
            print("The only available items on the menu include espresso, latte and cappuccino")
            continue

        machine.add_choice(user_choice)
        balance = machine.add_coins()

        if balance < machine.MENU[machine.coffee_choice]['cost']:
            print(f"You only have ${balance:.2f} which isn't enough to buy the {machine.coffee_choice} which costs ${machine.MENU[machine.coffee_choice]['cost']:.2f}. Money refunded.")
            balance = 0
            continue

        machine.check_resources()
        machine.make_coffee()
    except Exception as err:
        print(str(err))
        continue
