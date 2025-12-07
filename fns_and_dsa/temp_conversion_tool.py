FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temperature = float(input("Enter the temperature: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"Converted temperature: {result:.2f} Celsius")

    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"Converted temperature: {result:.2f} Fahrenheit")

    else:
        print("Invalid temperature unit.")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
