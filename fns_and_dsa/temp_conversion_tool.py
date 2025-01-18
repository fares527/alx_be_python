

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
   
    celsius = (fahrenheit -32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    

    fahrenheit = (celsius * FAHRENHEIT_TO_CELSIUS_FACTOR) +32
    return fahrenheit


def main():

    while True:
        try:
            temperature_value = float(input("Enter a temperature value: "))
            unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

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
                f"{temperature_value:.2f} degrees {unit} is equivalent to {converted_temperature:.2f} degrees {unit_label}."   )
            break

        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()