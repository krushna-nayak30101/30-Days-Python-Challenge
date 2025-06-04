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
