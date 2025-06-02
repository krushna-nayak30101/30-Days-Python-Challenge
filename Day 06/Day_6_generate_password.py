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
