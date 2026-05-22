# Parent class
class Animal:
    def eat(self):
        print("This animal eats food")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Using the classes
d = Dog()
d.eat()   # Inherited method
d.bark()  # Own method


class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

c = Car()


# single inheritance 

class Father:
    def bike(self):
        print("Father has a bike")

class Son(Father):
    def laptop(self):
        print("Son has a laptop")

s = Son()

s.bike()
s.laptop()

# multilevel inheritance

# Multilevel Inheritance

class Father:
    def bike(self):
        print("Father has a bike")


class Son(Father):
    def laptop(self):
        print("Son has a laptop")


class GrandChild(Son):
    def mobile(self):
        print("GrandChild has a mobile")


# Object creation
s = GrandChild()

# Calling methods
s.bike()
s.laptop()
s.mobile()