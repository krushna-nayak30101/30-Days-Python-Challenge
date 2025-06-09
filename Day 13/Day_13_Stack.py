# Initialize an empty stack
stack = []

# 🔼 Push items to the stack
stack.append("Shirt")
stack.append("Jeans")
stack.append("Jacket")
stack.append("Socks")
stack.append("Cap")

print("🧺 Current Stack:", stack)

# 👀 Peek the top item
print("👀 Top Item (peek):", stack[-1])  # Shows "Cap" without removing

# ⬇️ Pop the top item
removed_item = stack.pop()
print("❌ Removed (pop):", removed_item)

# 🔁 Stack after popping
print("📦 Stack Now:", stack)

# Push more items
stack.append("Shoes")
stack.append("Sweater")

print("➕ After More Pushes:", stack)

# Peek again
print("🔍 New Top Item (peek):", stack[-1])
