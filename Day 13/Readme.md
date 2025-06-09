# 🎯 Topic: 

- 🔸 Stack operations: push(), pop(), peek()
- 🔸 Queue basics and implementation using lists

###  Implement a stack with push, pop, and peek methods in Python 🐍

```
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

```

Day 13 Done

It’s a perfect example of LIFO (Last-In, First-Out) in real-world applications! 💼

💡 Quick Tip:
 Use stacks when you need undo functionality, backtracking, or temporary storage in a sequence.


