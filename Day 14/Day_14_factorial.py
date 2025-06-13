
def factorial(n):
    if n == 0 or n == 1:            # Base case
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(n))  # Output: 120

n= int(input ("Enter a number: "))
print(f"factorial of {n} is {factorial (n)} ")
