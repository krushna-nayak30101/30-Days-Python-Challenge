def even_numbers(limit):
    num = 0
    while num <= limit:
        if num % 2 == 0:
            yield num  # Lazy evaluation in action
        num += 1

# Consuming the generator
for n in even_numbers(10):
    print(n, end=" ")
