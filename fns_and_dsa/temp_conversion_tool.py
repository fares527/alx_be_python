FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    celsius = (fahrenheit - 32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 
    return fahrenheit

def main():
    while True:
        try:
            temperature_value = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

            if unit == "C":
                converted_temperature = convert_to_fahrenheit(temperature_value)
                unit_label = "Fahrenheit"
            elif unit == "F":
                converted_temperature = convert_to_celsius(temperature_value)
                unit_label = "Celsius"
            else:
                print("Invalid unit. Please enter 'C' or 'F'.")
                continue

            print(
                f"{temperature_value:.1f} {unit} is {converted_temperature:.1f} {unit_label}."
            )
            break

        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()