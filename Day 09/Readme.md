# 🎯 Topic: Diving into Inheritance & Polymorphism! 🐍✨
##  Challenge : Extend Car into an ElectricCar subclass with battery capacity

### 🧵 What I built:

## Challennge - Extend Car into an ElectricCar subclass with battery capacity 

```
# Define a class named Car, which will serve as a blueprint for car objects
class Car:
    def __init__(self, make, model, year):
        self.make, self.model, self.year = make, model, year
#  display car information
    def display(self):
        print(f"{self.year} {self.make} {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display(self):
        super().display()
        print(f"🔋 Battery: {self.battery_capacity} kWh")

# Tata Harrier (regular car example)
harrier = Car("Tata", "Harrier", 2024)
harrier.display()

# Suppose Tata launches an Electric version (ElectricCar example)
harrier_ev = ElectricCar("Tata", "Harrier EV", 2025, 85)
harrier_ev.display()

```
##  retail industry example (e.g., Product → DigitalProduct) 

```
class Product:
    def __init__(self, name, price, stock):
        self.name, self.price, self.stock = name, price, stock

    def update_stock(self, qty_sold):
        self.stock -= qty_sold

    def display_info(self):
        print(f"📦 {self.name} | ₹{self.price} | Stock: {self.stock}")

class DiscountedProduct(Product):
    def __init__(self, name, price, stock, discount):
        super().__init__(name, price, stock)
        self.discount = discount

    def display_info(self):
        discounted = self.price * (1 - self.discount / 100)
        print(f"📦 {self.name} | ₹{self.price} ➡ ₹{discounted:.2f} (-{self.discount}%) | Stock: {self.stock}")

# Test examples
Product("Jeans", 1499, 25).display_info()
dp = DiscountedProduct("Shirt", 999, 30, 20)
dp.update_stock(5)
dp.display_info()

```

🧠 Key Concepts Highlighted:
super() is used to call the parent class constructor and method.

display_info() is overridden in the ElectricCar class to show additional info.

Demonstrates real-world use of inheritance in modeling different types of vehicles.

Inheritance via super().__init__()

Method overriding (display_info)

New method to calculate discounted price

Real-world use case for retail inventory + promotions

- ✅ 9 days done, and momentum is building!
- If you’ve ever been intimidated by Python, join this journey — one module at a time. 🌱
