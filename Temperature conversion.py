temperature = int(input("input a temperature: "))
print('''
(1) for celsius to fahrenheit
(2) for fahrenheit to celsius
(3) for kelvin to fahrenheit
(4) for fahrenheit to kelvin
(5) for celsius to kelvin
(6) for kelvin to celsius
''')
temperature_conversion = input("Please input a number: ")
if temperature_conversion == "1":
    celsius_to_fahrenheit = 9/5*(temperature) + 32
    print(f"The temperature in fahrenheit is: {celsius_to_fahrenheit} degrees")
elif temperature_conversion == "2":
    fahrenheit_to_celsius = 5/9 * (temperature - 32)
    print(f"The temperature in celsius is: {fahrenheit_to_celsius} degrees")
elif temperature_conversion == "3":
    kelvin_to_fahrenheit = 9/5*(temperature-273) + 32
    print(f"The temperature in fahrenheit is: {kelvin_to_fahrenheit} degrees")
elif temperature_conversion == "4":
    fahrenheit_to_kelvin = 5/9*(temperature-32) + 273
    print(f"The temperature in kelvin is: {fahrenheit_to_kelvin} degrees")
elif temperature_conversion == "5":
    celsius_to_kelvin = temperature + 273
    print(f"The temperature in kelvin is: {celsius_to_kelvin} degrees")
elif temperature_conversion == "6":
    kelvin_to_celsius = temperature - 273
    print(f"The temperature in celsius is: {kelvin_to_celsius} degrees")
else:
    print("Please a number for temperature")


