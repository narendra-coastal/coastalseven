# example for abstraction
from abc import ABC, abstractmethod

# Abstract class
class ATM(ABC):

    @abstractmethod
    def withdraw(self):
        pass

# Child class
class BankATM(ATM):

    def withdraw(self):
        print("Money withdrawn successfully")

# Object creation
obj = BankATM()
obj.withdraw()