# 🎯 Topic: 
## try / except blocks
## Specific exceptions: ValueError, ZeroDivisionError, FileNotFoundError
## finally clause for guaranteed cleanup

## Challennge - Read numbers from a file and handle errors gracefully.

### 🧵 What I did:

## Challennge - Read numbers from a file and handle errors gracefully.

```
try:
    num = int(input("Enter a number: "))   # May raise ValueError if input is not a number
    result = 10 / num                      # May raise ZeroDivisionError if num is 0
    with open("log.txt", "r") as file:     # May raise FileNotFoundError if file doesn't exist
        print(file.read())                 # Reads and prints file content

except ValueError:
    print("Invalid number!")               # Handles non-integer input (e.g., 'abc')

except ZeroDivisionError:
    print("Division by zero is not allowed!")  # Handles dividing 10 by 0

except FileNotFoundError:
    print("Log file not found!")           # Handles case where 'log.txt' is missing

finally:
    print("This block always runs (cleanup or exit message).")

```
## Retail file error handelling method 

```
file_path = r"D:\kk\New folder\Python\30 days Pyhton Challenge\Day wise\Day_10\Daily_sales.txt"

try:
    file = open(file_path, "r")
    total_sales = 0
    day = 1

    for line in file:
        try:
            sales = float(line.strip())
            print(f"✅ Day {day}: ₹{sales}")
            total_sales += sales
        except ValueError:
            print(f"⚠️ Day {day}: Invalid entry '{line.strip()}' — Skipped.")
        day += 1

    print(f"\n🧾 Total Sales: ₹{total_sales:.2f}")

except FileNotFoundError:
    print(f"\n❌ Error: Could not find the file at '{file_path}'.")

except Exception as e:
    print(f"\n⚠️ Unexpected error occurred: {e}")

finally:
    if 'file' in locals():
        file.close()
        print("📁 File closed after reading sales data.")

````
