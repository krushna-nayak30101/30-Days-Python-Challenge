# 🎯 Topic: 

-   🔸 Defining models with BaseModel
-   🔸 Nested models for structured data
-   🔸 Auto-validation for fields (type + logic)
-   🔸 Custom error handling with constraints

Challenge -  Build a User Profile model with: 
-  name: non-empty string
-  email: valid email format
-  age: allowed range between 18 and 100
-   ✅ With Pydantic, all of this validation was done in just a few lines of code. Clean, readable, and powerful!

```
from pydantic import BaseModel, EmailStr, Field, ValidationError

class UserProfile(BaseModel):
    name: str
    email: EmailStr
    age: int =  Field(..., ge=18, le=100)  # Must be between 18 and 100

# ✅ Test with valid data
try:
    user = UserProfile(
        name="Krushna Nayak",
        email="krushna@example.com",
        age=18
    )
    print("✅ Valid User Profile:")
    print(user)
except ValidationError as e:
    print("❌ Validation Error:")
    print(e)

# ❌ Test with invalid email and age
try:
    invalid_user = UserProfile(
        name="Asha Verma",
        email="asha[at]gmail.com",  # Invalid email
        age=15  # Below allowed range
    )
except ValidationError as e:
    print("\n❌ Invalid User Profile:")
    print(e)
```

📌 Key Learning:

With Pydantic, data becomes a first-class citizen in your app.
Whether you’re validating user input in a form, parsing JSON in APIs, or designing internal systems — Pydantic ensures your data is clean, structured, and correct before it even reaches your logic.

🔐 Data validation isn't just a backend task — it's a security layer, a UX enhancer, and a sanity check rolled into one.
Onward to more structured code! 💪

hashtag#Pydantic hashtag#DataValidation hashtag#Python hashtag#FastAPI hashtag#CleanCode hashtag#30DaysOfPython hashtag#RetailTech hashtag#PythonTips hashtag#KrushnaLearnsPython hashtag#APIDesign hashtag#BuildInPublic
