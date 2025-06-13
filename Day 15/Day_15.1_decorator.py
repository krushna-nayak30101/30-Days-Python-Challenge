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
