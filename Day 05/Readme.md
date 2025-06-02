# 📅 Day 5 – Functions and Lambda Expressions

## 🗒️ Topics Covered  
Defining Functions  
Parameters and Return Values  
Lambda Functions  

### 🎯 Challenge  
🔧 Write a function that computes the sum and average of a list of numbers.
```
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

```
### 📌 Progress  
Day 5 completed ✅  
#30DaysOfPython #IDC30DaysChallenge
