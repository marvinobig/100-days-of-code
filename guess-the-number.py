from random import randint

print("Welcome to the number guessing game!!")

number_to_guess = randint(1, 100)
number_of_guesses = 0
userGuess = 0

difficulty = input("Do you want to play on easy or hard mode? (easy/hard) ").strip().lower()

if difficulty in ["hard", "h"]:
    number_of_guesses = 5
else:
    number_of_guesses = 10

print("I'm thinking of a number between 1 and 100")

while number_of_guesses > 0:
    print(f"You have {number_of_guesses} attempts remaining to guess the number")

    try:
        userGuess = int(input("Make a guess: "))
    except ValueError:
        print("Make a guess using a valid whole number")
        continue

    if userGuess < number_to_guess:
        print("Too low!")
        number_of_guesses -= 1
        continue
    elif userGuess > number_to_guess:
        print("Too high!")
        number_of_guesses -= 1
        continue
    elif userGuess == number_to_guess:
        break

if userGuess == number_to_guess:
    print("You guessed correctly. You win!!")
else:
    print("You've run out of guesses, you lose")