# method overloading
#same class and same functions or method names
#different parameters
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

obj = Calculator()

print(obj.add(2, 3))
print(obj.add(2, 3, 4))

#method over riding
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()