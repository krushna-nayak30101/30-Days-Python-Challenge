# 📅 Day 3 – Lists, Tuples, Dictionaries, and Sets

## 🗒️ Topics Covered
- Lists: Slicing, Common Methods
- Tuples: Immutability
- Dictionaries: Key-Value Pairs
- Sets: Unique Unordered Elements

## 🎯 Challenge

🔧 Create a Python program that uses a **dictionary** to simulate a basic inventory system.

### 💻 Solution

# Create initial retail inventory (item: quantity)
inventory = {    "Jeans": 5,    "Shirts": 8,    "Kurtis": 7,    "Polo Tees": 5,    "Palazzo": 16}

# Add new item
inventory["Jackets"] = 12

# Update quantity after sales (e.g., sold some items)
inventory["Jeans"] -= 2    # Sold 2 Jeans
inventory["Shirts"] -= 3   # Sold 3 Shirts
inventory["Polo Tees"] -= 4  # Sold 4 Polo Tees

# Remove item (discontinued)
del inventory["Palazzo"]


# Print the final inventory
print("\nFinal Retail Inventory:")
for item in inventory:
    print(f"{item} - {inventory[item]}")
```
📌 Progress

Day 3 completed ✅

#30DaysOfPython #IDC30DaysChallenge
