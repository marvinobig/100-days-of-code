print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? (S, M or L): ").upper()
pepperoni = input("Do you want pepperoni on your pizza? (Y or N): ").upper()
extra_cheese = input("Do you want extra cheese? (Y or N): ").upper()

if size == 'S':
    total = 15

    if pepperoni == 'Y':
        total += 2
    if extra_cheese == 'Y':
        total += 1

    print(f"Your final bill is: ${total}.")
elif size == 'M':
    total = 20

    if pepperoni == 'Y':
        total += 3
    if extra_cheese == 'Y':
        total += 1

    print(f"Your final bill is: ${total}.")
else:
    total = 25

    if pepperoni == 'Y':
        total += 3
    if extra_cheese == 'Y':
        total += 1

    print(f"Your final bill is: ${total}.")