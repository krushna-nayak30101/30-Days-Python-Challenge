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
