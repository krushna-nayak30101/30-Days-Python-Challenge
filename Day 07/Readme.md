# 🎯 Topic: Reading Files & Word Frequency Counter

## Today’s challenge was all about working with files and real-world text data. 

Here’s what I tackled today:
### ✅ Read a .txt file using Python
### ✅ Split the content into words
### ✅ Normalized the text (lowercased and removed punctuation)
### ✅ Used a dictionary to count how many times each word appears

 ## 🔍 Counting word frequency in a text file using Python.
```
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
```

- ✅ 7 days done, and momentum is building!
- If you’ve ever been intimidated by Python, join this journey — one module at a time. 🌱
