class LaptopStore:
    def __init__(self,prod_name,price,quantity):
        self.prod_name = prod_name
        self.price = price
        self.quantity = quantity

    def price_calculation(self):
        return self.price * self.quantity
    
    def product_info(self):
        total_amount = self.price_calculation()
        return f"{self.prod_name} Laptop, total amount:{total_amount}"

apple = LaptopStore("Apple", 1000, 7)
dell = LaptopStore("Dell", 800, 3)

print(apple.price_calculation())
print(dell.price_calculation())

print(apple.product_info())
print(dell.product_info())

