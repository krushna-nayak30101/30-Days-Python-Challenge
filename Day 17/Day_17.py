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
