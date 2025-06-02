# 🎯 Topic: Working with Modules in Python – built-in & custom


### ✅ Importing Built-in Modules
### ✅ Using popular ones like math and random
### ✅ Creating and using custom modules
### ✅ Understanding the role of modular programming in real-world projects 

### Solution
```
import random
import string

# Step 1: Choose the first character (must be uppercase)
first_char = random.choice(string.ascii_uppercase)

# Step 2: Generate the remaining 7 characters randomly
remaining_chars = random.choices(
    string.ascii_letters + string.digits + string.punctuation,
    k=7
)

# Step 3: Combine and create the password
password = first_char + ''.join(remaining_chars)

# Step 4: Output
print("Password (starts with capital):", password)


```

### 
🧠 Why It Matters:
Modules = less repetition, more structure.
They help split logic across files and build scalable, professional-grade apps.
And let’s be real — importing a math function > writing it from scratch!

✅ 6 days done, and momentum is building!
If you’ve ever been intimidated by Python, join this journey — one module at a time. 🌱
