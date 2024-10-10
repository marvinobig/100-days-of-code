class TemperatureConversion:
    available_conversions = ['celsius', 'fahrenheit']

    def celsius_to_fahrenheit(self, temp):
        fahrenheit = (temp * 9 / 5) + 32

        return fahrenheit

    def fahrenheit_to_celsius(self, temp):
        celsius = (temp - 32) * 5 / 9

        return celsius

    def check_for_float_number(self, temp):
        try:
            float(temp)
            return True
        except ValueError:
            return False
