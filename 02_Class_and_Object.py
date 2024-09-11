class LaptopStore:
    def price_calculation(self, x, y):
        return x * y

#instance of the class
product1 = LaptopStore()

# Assign attributes:
product1.name = "Laptop"
product1.price = 1000
product1.quantity = 8

# Calling methods from instances of a class:
print(LaptopStore.price_calculation(product1.name, product1.price,product1.quantity))

#instance of the class
product2 = LaptopStore()

# Assign attributes:
product2.name = "Joystick"
product2.price = 50
product2.quantity = 3

# Calling methods from instances of a class: 
print(product2.price_calculation(product2.price, product2.quantity))