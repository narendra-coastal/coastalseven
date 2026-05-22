# method overloading
#same class and same functions or method names
#different parameters
class A:
    def sum(self, a , b):
        return a+b
    def sum(self, a, b, c=1):
        return a+b+c
    obj=A()
    print(obj.sum(1,2,5))