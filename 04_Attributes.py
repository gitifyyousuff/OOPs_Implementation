class LaptopStore:
    all = []
    def __init__(self, prod_name: str, price: float, quantity=0):
        self.prod_name = prod_name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        LaptopStore.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def __repr__(self):
        return f"Laptop('{self.prod_name}', {self.price}, {self.quantity})"

item1 = LaptopStore("Dell", 100, 1)
item2 = LaptopStore("Samsung", 1000, 3)
item3 = LaptopStore("Apple", 10, 5)
item4 = LaptopStore("HP", 50, 5)
item5 = LaptopStore("Lenovo", 75, 5)

print(LaptopStore.all)
print(repr(item3))
