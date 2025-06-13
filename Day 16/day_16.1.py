# Fibonacci Generator 

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Example: Generate first 10 Fibonacci numbers
for num in fibonacci(10):
    print(num, end=" ")
