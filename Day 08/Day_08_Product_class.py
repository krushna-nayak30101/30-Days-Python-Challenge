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
