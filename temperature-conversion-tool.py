# Project: "Temperature Conversion Tool"
#
# Objective:
# Build a basic temperature conversion tool that converts between Celsius, Fahrenheit, and Kelvin.
#
# Requirements:
# Ask the user which scale they want to convert the temperature to (celsius to fahrenheit, fahrenheit to celsius).
# Ask the user to input a temperature value.
# Use variables to store the temperature (float) and scale (string).
# Ensure proper input validation to check for valid temperature values and scales.
# Based on the input, check the current temperature scale and convert it to the requested scale.
# Use conditional statements to handle different conversions (Celsius to Fahrenheit, Fahrenheit to Kelvin, etc.).
# Allow the user to perform multiple conversions until they choose to exit the program.
# After each conversion, display the result and ask if the user wants to perform another conversion.
# Check which conversion the user wants and whether the input values are valid (e.g., the temperature isn't below absolute zero for Kelvin).
#
# Example Flow:
# The user inputs a temperature in Celsius, and the system converts it to Fahrenheit.
# The user can then convert another temperature, say from Kelvin to Celsius.
# The program loops until the user decides to exit.

def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9 / 5) + 32

    return fahrenheit

def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5 / 9

    return celsius

def check_for_float_number(string):
    try:
        float(string)
        return True
    except TypeError:
        return False

available_conversions = ['celsius', 'fahrenheit']
user_confirmation = ""
stop = False

while not stop:
    print("Temperature values available to convert from:")

    for temperature in available_conversions:
        print(temperature)

    chosen_temp_scale = input("What do you want to convert from? ").lower()
    user_temp_value = input("What value do you want to convert (decimal format)? ")

    if chosen_temp_scale not in available_conversions:
        print("Value to convert from needs to be either 'celsius' or 'fahrenheit'")
        continue

    if not check_for_float_number(user_temp_value):
        print("Temp value needs to be a valid decimal number")
        continue

    if chosen_temp_scale == 'celsius':
        print(f"Celsius: {float(user_temp_value)} to Fahrenheit: {celsius_to_fahrenheit(float(user_temp_value))}")
    else:
        print(f"Fahrenheit: {float(user_temp_value)} to Celsius: {fahrenheit_to_celsius(float(user_temp_value))}")

    user_confirmation = input("Would you like to convert another value? ").lower()

    stop = True if user_confirmation == "no" else False





