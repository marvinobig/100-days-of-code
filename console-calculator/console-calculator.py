# Console Calculator
# Program asks the user to type the first number.
# Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
# Program asks the user to type the second number.
# Program works out the result based on the chosen mathematical operator.
# Program asks if the user wants to continue working with the previous result.
# If yes, program loops to use the previous result as the first number and then repeats the calculation process.
# If no, program asks the user for the fist number again and wipes all memory of previous calculations.
from art import logo

def add(n1, n2):
    """
    :param n1:
    :param n2:
    :return: result of addition operation
    """
    return n1 + n2

def subtract(n1, n2):
    """
    :param n1:
    :param n2:
    :return: result of subtraction operation
    """
    return n1 - n2

def multiply(n1, n2):
    """
    :param n1:
    :param n2:
    :return: result of multiplication operation
    """
    return n1 * n2

def divide(n1, n2):
    """
    :param n1:
    :param n2:
    :return: result of division operation
    """
    return n1 / n2


operators = {
    "+" : add ,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

total = 0
stop = False

print(logo)

while not stop:
    try:
        first_number = float(total if total != 0 else input("What is your first number? "))
    except ValueError:
        print("First value needs to be a number")
        continue

    try:
        second_number = float(input("What is your second number? "))
    except ValueError:
        print("Second value needs to be a number")
        continue

    calculator_operator = input("What operation do you want to perform? (+, -, *, /) ").strip()
    if calculator_operator in operators:
        if calculator_operator == "/" and second_number == 0:
            print("Division by zero is not possible")
            continue

        total = operators[calculator_operator](first_number, second_number)

        print(f"Current total: {total}")

        calculation_confirmation = input("Do you want to continue with previous total? (yes/no) ")
        if calculation_confirmation in ["no", "n"]:
            total = 0
        else:
            continue

        app_confirmation = input("Do you want to perform another calculation? (yes/no) ")
        stop = app_confirmation in ["no", "n"]
    else:
        print("The program requires a valid mathematical operator")
        continue