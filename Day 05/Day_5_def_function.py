def compute_sum_avg(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

# Taking input from user
user_input = input("Enter numbers separated by commas: ")

# Convert input string to a list of floats
number_list = list(map(float, user_input.split(',')))

# Call the function
total, average = compute_sum_avg(number_list)

# Display result
print(f"Sum = {total}")
print(f"Average = {average}")
