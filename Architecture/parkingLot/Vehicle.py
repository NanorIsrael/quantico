#Vehicle class for use with Parking Lot Manager
from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    Abstract base class representing a generic vehicle.

    This class defines shared properties and behavior for all vehicles.
    Subclasses must implement the type() method.
    """
    def __init__(self,regnum: str, make: str, model: str, color: str):
        self._color = color
        self._regnum = regnum
        self._make = make
        self._model = model

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



