## Python Challenege ## --  
### Daily Python Dose: Learn Something New Every Day
### From Zero to Pythonic: 30-Day Challenge Begins

# Path to your file
file_path = r"D:\kk\New folder\Python\30 days Pyhton Challenge\Day wise\Day_7\Python_challenge.txt"

# Read the file
with open(file_path, "r") as file:
    text = file.read()

# Convert to lowercase and split into words
words = text.lower().split()

# Count word frequencies
word_count = {}
for word in words:
    word = word.strip(".,!?\"'()[]{}")  # Basic punctuation cleanup
    word_count[word] = word_count.get(word, 0) + 1

# Print results (unsorted)
print("📊 Word Frequencies:\n")
for word, count in word_count.items():
    print(f"{word}: {count}")
