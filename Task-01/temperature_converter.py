print("=== Temperature Conversion Program ===")

print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

choice = int(input("Enter your choice (1/2/3): "))
temp = float(input("Enter the temperature value: "))

if choice == 1:
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    print("\nTemperature in Fahrenheit:", round(fahrenheit, 2))
    print("Temperature in Kelvin:", round(kelvin, 2))

elif choice == 2:
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    print("\nTemperature in Celsius:", round(celsius, 2))
    print("Temperature in Kelvin:", round(kelvin, 2))

elif choice == 3:
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print("\nTemperature in Celsius:", round(celsius, 2))
    print("Temperature in Fahrenheit:", round(fahrenheit, 2))

else:
    print("Invalid choice. Please run the program again.")
