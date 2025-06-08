import re
# check is only for [@gmail.com]
def is_valid_gmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email) is not None

# Example usage:
emails = [
    "krishna.nayak@gmail.com",     # ✅ valid
    "krishna_nayak123@gmail.com",     # ✅ valid
    "ravi123@gmail.com",           # ✅ valid
     "ravi_123@gmail.com",          # ✅ valid
    "sonali_singh@outlook.com",    # ❌ invalid
    "meera.k@gmails.com",          # ❌ invalid
    "amit@@gmail.com",             # ❌ invalid
    "lata@gmaill.com"              # ❌ invalid
]

for email in emails:
    result = "Valid ✅" if is_valid_gmail(email) else "Invalid ❌"
    print(f"{email} --> {result}")
