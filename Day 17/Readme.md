# 🎯 Topic: 
-  🔹 What is a with statement and why it's used
-  🔹 How Python handles resources safely (like files or network connections)
-  🔹 Writing a custom context manager using __enter__() and __exit__()

 Challennge - Build a custom context manager that logs when a block of code starts and ends

 🧵 What I did:
```
class RetailFileManager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_path, self.mode)
            return self.file
        except FileNotFoundError:
            print(f"❌ File not found at: {self.file_path}")
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print("✅ File closed successfully.")
        if exc_type:
            print(f"⚠️ Error occurred: {exc_value}")
        return True  # Prevents exception propagation

# Sample inventory file path (Update this to your actual file location)
file_path = r"D:\kk\New folder\Python\30 days Pyhton Challenge\Day wise\Day_17\retail_inventory.txt"

# Using the custom context manager to read inventory
with RetailFileManager(file_path, "r") as file:
    if file:
        print("🛍️ Retail Inventory Stock:\n")
        for line in file:
            item, stock = line.strip().split(":")
            print(f"📦 {item} — Stock: {stock}")

```

  Day 17 Done 

🔑 𝗞𝗲𝘆 𝗟𝗲𝗮𝗿𝗻𝗶𝗻𝗴:

Python gives you the power to manage resources elegantly and safely.
 Whether it’s opening a file or creating a custom logger, with statements make sure nothing is left hanging.
 

