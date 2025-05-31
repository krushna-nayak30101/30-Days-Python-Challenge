# 📅 Day 4 – if, elif, else, for and while loops , break and continue

## 🗒️ Topics Covered
✅ if, elif, else – for making logical decisions
✅ for and while loops – for repeating tasks
✅ break and continue – to control loop behavior

## 🎯 Challenge

 🔢 Write a Python program to check if a number entered by the user is **prime**.

### 💻 Solution

```python
# Check if a user-entered number is prime.
n = int(input("Enter a number: "))
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break  # No need to check further

if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

```

📌 Progress

Day 4 completed ✅

#30DaysOfPython #IDC30DaysChallenge
