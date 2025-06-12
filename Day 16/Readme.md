# 🎯 Topic: 
 - Difference between return and yield
 - Creating custom iterators using __iter__() and __next__()
 - The magic of lazy evaluation — compute values only when needed

 Challennge - Build a generator that yields even numbers up to a limit.

 🧵 What I did:

 ```
def even_numbers(limit):
    num = 0
    while num <= limit:
        if num % 2 == 0:
            yield num  # Lazy evaluation in action
        num += 1

# Consuming the generator
for n in even_numbers(10):
    print(n, end=" ")
```
### Fibonacci Generator 
```
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
```


Day 16 Done 

- If you're building log processors, file readers, or infinite data streams — this concept is a game-changer. 🔄
