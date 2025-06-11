#  Topic –  Function Decorators

 Topics Covered:
- 🔸 Writing a basic @decorator
- 🔸 Measuring function execution time using time module
- 🔸 Use cases in real-world apps — logging, authorization, retries, and timing

## 🎯 Challenge Task:
Build a decorator to calculate and print how long a function takes to execute. ⏱️

```
import time

def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"⏱️ Execution Time: {end - start:.4f} seconds")
    return wrapper

@timer_decorator
def sample_task():
    time.sleep(2)  # Simulate a delay
    print("✅ Task completed.")

sample_task()

```



## ✅ Example: Retail Invoice Generator with Execution Time Logger
```
import time

# Decorator to log execution time
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        print(f"🧾 Generating invoice using '{func.__name__}'...")
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()
        print(f"✅ Invoice generated in {end - start:.2f} seconds.\n")
        return result
    return wrapper

# Sample function that simulates invoice creation
@log_execution_time
def generate_invoice(customer, items):
    print(f"🧍 Customer: {customer}")
    total = 0
    for item, price in items:
        print(f"🛍️ {item}: ₹{price}")
        total += price
        time.sleep(0.3)  # Simulate time taken to process each item
    print(f"💰 Total Amount: ₹{total}")
    return total

# Call the function with sample data
invoice_items = [("Jeans", 1499), ("Shirt", 899), ("Shoes", 2499)]
generate_invoice("Krushna Nayak", invoice_items)
```

Day 15 done
🚀 Key Learning:
Using decorators is like putting power-ups on your functions — whether you're timing operations, logging activity, or enforcing rules.
They keep your core code clean, modular, and extensible.
