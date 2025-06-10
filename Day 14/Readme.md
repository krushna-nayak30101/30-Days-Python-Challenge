# ✅ Topic – Recursive Functions in Python 🔁

  Topics Covered:
-   What is recursion and how it works
-   Importance of base cases
-   Understanding the call stack
-   Recursive vs. iterative thinking

## 🎯 Challenge Task:
Write a recursive function to calculate the factorial of a number.

```

def factorial(n):
    if n == 0 or n == 1:            # Base case
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(n))  # Output: 120

n= int(input ("Enter a number: "))
print(f"factorial of {n} is {factorial (n)} ")
```

### 📘 Key Learning:
Recursion isn’t just a coding trick — it teaches you to think in layers.
It breaks down problems into self-similar subproblems, a powerful way to solve complex logic cleanly and elegantly.
Day 14 Done
