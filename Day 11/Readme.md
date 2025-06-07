# 🎯 Topic: 
- ✅ How to use Python’s built-in datetime module
-  ✅ Create and manipulate dates and times
-  ✅ Format them into readable or custom styles
-  ✅ Calculate differences between two dates using timedelta

 ###  Calculate the number of days remaining until the end of the year —

 🧵 What I did:

```
from datetime import datetime

# Input two dates in YYYY-MM-DD format
date_str1 = input("Enter the first date (YYYY-MM-DD): ")
date_str2 = input("Enter the second date (YYYY-MM-DD): ")

# Convert string input to datetime objects
date1 = datetime.strptime(date_str1, "%Y-%m-%d")
date2 = datetime.strptime(date_str2, "%Y-%m-%d")

# Calculate the difference
delta = abs((date2 - date1).days)

print(f"The number of days between {date_str1} and {date_str2} is {delta} days.")

```
Day11 Done 
