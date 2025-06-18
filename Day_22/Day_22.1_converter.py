def convert_temperature(temp, to_unit):
    if to_unit == "c":
        return (temp - 32) * 5 / 9
    elif to_unit == "f":
        return (temp * 9 / 5) + 32
    else:
        return None

# Ask the user for input
try:
    temp = float(input("Enter the temperature value: "))
    to_unit = input("Convert to (c for Celsius, f for Fahrenheit): ").lower()

    converted = convert_temperature(temp, to_unit)

    if converted is not None:
        if to_unit == "c":
            print(f"{temp}°F is {converted:.2f}°C")
        else:
            print(f"{temp}°C is {converted:.2f}°F")
    else:
        print("❌ Invalid conversion unit. Please enter 'c' or 'f'.")

except ValueError:
    print("❌ Please enter a valid number for the temperature.")
