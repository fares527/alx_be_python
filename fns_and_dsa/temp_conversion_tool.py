FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    from_fahrenheite_to_celsius =  FAHRENHEIT_TO_CELSIUS_FACTOR * (temp - 32) 



def convert_to_fahrenheit(celsius):
    from_celsius_to_fahrenheite = (CELSIUS_TO_FAHRENHEIT_FACTOR * temp) + 32



temp = input("Enter the temperature to convert: ")
degree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if degree == "celsius":
    print(convert_to_fahrenheit)

elif degree == "fahrenheite":
    print(convert_to_celsius)

else:
    print("wrong input")