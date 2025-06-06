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
