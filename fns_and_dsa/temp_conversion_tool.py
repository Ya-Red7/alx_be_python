FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
temp = int(input("Enter the temperature to convert:"))
if type(temp) is not int:
    print("Invalid temperature. Please enter a numeric value.")
else:
    cf = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    if cf=='F':
        print(f"{temp}F is {convert_to_celsius(temp)}C")
    elif cf=='C':
        print(f"{temp}C is {convert_to_fahrenheit(temp)}F")
