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
