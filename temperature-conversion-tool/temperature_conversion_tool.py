from conversion_class import TemperatureConversion

# Project: "Temperature Conversion Tool"
#
# Objective:
# Build a basic temperature conversion tool that converts between Celsius, Fahrenheit and vice versa.
#
# Requirements:
# Ask the user which scale they want to convert the temperature to (Celsius to Fahrenheit, Fahrenheit to Celsius).
# Ask the user to input a temperature value.
# Use variables to store the temperature (float) and scale (string).
# Ensure proper input validation to check for valid temperature values and scales.
# Based on the input, check the current temperature scale and convert it to the requested scale.
# Use conditional statements to handle different conversions (Celsius to Fahrenheit, etc.).
# Allow the user to perform multiple conversions until they choose to exit the program.
# After each conversion, display the result and ask if the user wants to perform another conversion.

tool = TemperatureConversion()

while True:
    print("Temperature values available to convert from:")

    for temperature in tool.available_conversions:
        print(temperature.title())

    chosen_temp_scale = input("What do you want to convert from? ").strip().lower()
    user_temp_value = input("What value do you want to convert (decimal format)? ").strip()

    if chosen_temp_scale not in tool.available_conversions:
        print("Value to convert from needs to be either 'celsius' or 'fahrenheit'")
        continue

    if not tool.check_for_float_number(user_temp_value):
        print("Temp value needs to be a valid decimal number")
        continue

    if chosen_temp_scale == 'celsius':
        print(f"Celsius: {float(user_temp_value)} to Fahrenheit: {tool.celsius_to_fahrenheit(float(user_temp_value))}")
    else:
        print(f"Fahrenheit: {float(user_temp_value)} to Celsius: {tool.fahrenheit_to_celsius(float(user_temp_value))}")

    user_confirmation = input("Would you like to convert another value [yes/no]? ").strip().lower()

    if user_confirmation in ["no", "n"]:
        break
