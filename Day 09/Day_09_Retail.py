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
