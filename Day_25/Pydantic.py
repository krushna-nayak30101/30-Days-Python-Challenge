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
