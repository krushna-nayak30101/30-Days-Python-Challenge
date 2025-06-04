# 🎯 Topic: Object-Oriented Programming (OOP) Unlocked 
##  Challenge : Create a Car class with attributes and a display method.

### 🧵 What I built:
- ✅ A Product class — the DNA for each retail item
- ✅ Attributes like name, price, stock
- ✅ A constructor to initialize each product
- ✅ A display_info() method to showcase product details
- ✅ An update_stock() method to reflect real-time sales

 ## Create a Car class with attributes and a display method

 ```
## python challenge -- Create a Car class with attributes and a display method

class Car:
    def __init__(self, brand, model,variant): # int initialize 
        self.brand = brand      # brand name 
        self.model = model      # model name 
        self.variant = variant  # variant type
    def show_info(self):
        print(f"{self.brand} {self.model} {self.variant}")

# Creating an object
car1 = Car("Toyota", "Fortuner", "Legender")
car1.show_info()  # Output: Toyota Fortuner Legender

```
```
### Python challenge -- Challenge: Design a retail product class with display and update methods 
class Product:
    def __init__(self, name, price, stock):
        self.name = name        # Product name
        self.price = price      # Price per unit
        self.stock = stock      # Available stock

    def update_stock(self, qty_sold):
        self.stock -= qty_sold  # Reduce stock after sale

    def display_info(self):
        print(f"📦 {self.name} | ₹{self.price} | Stock: {self.stock}")

item1 = Product("Jeans", 1499, 25)
item1.update_stock(3)
item1.display_info()
```

- ✅ 8 days done, and momentum is building!
- If you’ve ever been intimidated by Python, join this journey — one module at a time. 🌱
