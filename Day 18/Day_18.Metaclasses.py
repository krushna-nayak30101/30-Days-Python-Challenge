class StrictMeta(type):
    def __new__(cls, name, bases, class_dict):
        print(f"\n🔧 Creating class '{name}' with StrictMeta...")
        for key in class_dict:
            print(f"🔍 Checking attribute: {key}")
            if not key.startswith("__") and not key.isupper():
                raise TypeError(f"❌ Attribute '{key}' must be uppercase.")
        print(f"✅ All attributes in '{name}' meet the naming convention.\n")
        return super().__new__(cls, name, bases, class_dict)

# ✅ Valid class
class RetailSettings(metaclass=StrictMeta):
    MAX_ITEMS = 100
    STORE_ID = "MUMBAI001"
    LOCATION = "Mumbai"

# ❌ Invalid class — caught safely
try:
    class InvalidRetailSettings(metaclass=StrictMeta):
        store_name = "PuneMart"   # Not uppercase – triggers error
        MAX_ITEMS = 50
except TypeError as e:
    print(e)
