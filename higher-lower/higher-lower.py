from random import randint
from game_data import data

score = 0
stop = False

def seperator(amount, seperator_char = '-'):
    print(seperator_char * amount)

while not stop:
    comparison_dict = {
        'a' : data[randint(0, len(data) - 1)],
        'b' : data[randint(0, len(data) - 1)]
    }

    seperator(100)
    print(f"Compare A: {comparison_dict['a']['name']}, a {comparison_dict['a']['description']}, from {comparison_dict['a']['country']}.")
    print(f"Against B: {comparison_dict['b']['name']}, a {comparison_dict['b']['description']}, from {comparison_dict['b']['country']}.")
    seperator(100)

    user_choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
    seperator(100)

    if user_choice not in comparison_dict:
        print("Enter 'A' or 'B' when prompted")
        continue

    for key, value in comparison_dict.items():
        if user_choice == key:
            continue

        if comparison_dict[user_choice]['follower_count'] > value['follower_count']:
            score += 1
            print(f"Your right! Current score: {score}.")
        elif comparison_dict[user_choice]['follower_count'] < value['follower_count']:
            stop = True
            print(f"Sorry, that's wrong. Final score: {score}")