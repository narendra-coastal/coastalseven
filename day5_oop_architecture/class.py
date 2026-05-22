class Narendra:
    d = 12
    print("this is class")

    def display(self):
        a = 10
        b = 15
        print(a, b)

# creating object
obj = Narendra()

# calling method
obj.display()

# accessing class variable
print(obj.d)


class Mobile:

    def __init__(self, brand, battery, ram, camera, price):
        self.brand = brand
        self.battery = battery
        self.ram = ram
        self.camera = camera
        self.price = price

    def display(self):

        print("Brand:", self.brand)
        print("Battery:", self.battery)
        print("RAM:", self.ram)
        print("Camera:", self.camera)
        print("Price:", self.price)


# Object creation
obj = Mobile("Apple", "5000mAh", "8GB", "50MP", "75000")

# Method call
obj.display()