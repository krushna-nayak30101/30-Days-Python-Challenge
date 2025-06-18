# 🎯 Topic: 
- 🔹 How to parse command-line arguments using argparse
- 🔹 Structuring user-friendly CLI tools
- 🔹 Handling options, flags, and help messages

Challennge -   Build a Temperature Converter CLI tool 🌡️

**Temperature Converter CLI Tool (Python)**
```
import argparse

# Create the ArgumentParser object with a description
parser = argparse.ArgumentParser(description="🌡️ Convert temperatures between Celsius and Fahrenheit.")

# Define CLI arguments
parser.add_argument("--temp", type=float, required=True, help="Temperature value to convert.")
parser.add_argument("--to", choices=["c", "f"], required=True, help="Convert to 'c' for Celsius or 'f' for Fahrenheit.")

# Parse the arguments
args = parser.parse_args()

# Define the conversion function
def convert_temperature(temp, to_unit):
    if to_unit == "c":
        return (temp - 32) * 5 / 9
    else:
        return (temp * 9 / 5) + 32

# Perform and print the conversion
converted = convert_temperature(args.temp, args.to)

# Show result
if args.to == "c":
    print(f"{args.temp}°F is {converted:.2f}°C")
else:
    print(f"{args.temp}°C is {converted:.2f}°F")
```
**Python Script (with input() instead of argparse)**
```
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
```

📌 Key Learning:
 Building CLI tools makes your scripts interactive, sharable, and automation-ready — from file processors to retail price checkers and internal utilities.

 🧰 CLI tools can power:
Internal data converters
Automation scripts for stock updates
Mini tools for customer service teams
