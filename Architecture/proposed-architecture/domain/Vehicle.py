from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, regnum: str, make: str, model: str, color: str):
        self._regnum = regnum
        self._make = make
        self._model = model
        self._color = color

    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def color(self) -> str:
        return self._color

    @property
    def regnum(self) -> str:
        return self._regnum

    @abstractmethod
    def type(self) -> str:
        pass


class Car(Vehicle):
    def type(self) -> str:
        return "Car"


class Truck(Vehicle):
    def type(self) -> str:
        return "Truck"


class Motorcycle(Vehicle):
    def type(self) -> str:
        return "Motorcycle"


class Bus(Vehicle):
    def type(self) -> str:
        return "Bus"

from abc import ABC, abstractmethod

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(
        self, regnum: str, make: str, model: str, color: str
    ) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self, regnum: str, make: str, model: str, color: str) -> Vehicle:
        return Car(regnum, make, model, color)


class TruckFactory(VehicleFactory):
    def create_vehicle(self, regnum: str, make: str, model: str, color: str) -> Vehicle:
        return Truck(regnum, make, model, color)


class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self, regnum: str, make: str, model: str, color: str) -> Vehicle:
        return Motorcycle(regnum, make, model, color)


class BusFactory(VehicleFactory):
    def create_vehicle(self, regnum: str, make: str, model: str, color: str) -> Vehicle:
        return Bus(regnum, make, model, color)
