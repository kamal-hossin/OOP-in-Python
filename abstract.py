from abc import ABC, abstractmethod


# Abstract Class
class Vehicle(ABC):

    def __init__(self, name):
        self.name = name

    # Abstract Method
    @abstractmethod
    def start_engine(self):
        pass


# Child Class 1
class Car(Vehicle):

    def start_engine(self):
        print(f"{self.name} car engine started 🚗")


# Child Class 2
class Bike(Vehicle):

    def start_engine(self):
        print(f"{self.name} bike engine started 🏍️")


# Object Create
car1 = Car("Toyota")
bike1 = Bike("Yamaha")

car1.start_engine()
bike1.start_engine()