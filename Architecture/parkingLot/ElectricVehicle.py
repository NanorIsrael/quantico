
from abc import ABC, abstractmethod


class ElectricVehicle(ABC):
    """
    Abstract base class representing a generic electric vehicle.

    This class defines shared properties and behavior for all electric vehicles.
    Subclasses must implement the get_type() method.
    """
    def __init__(self,regnum: str,make: str,model: str,color: str):
        self._color = color
        self._regnum = regnum
        self._make = make
        self._model = model
        self._charge = 0

    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def color(self):
        return self._color

    @property
    def regnum(self) -> str:
        return self._regnum

    @property
    def charge(self)->int:
        return self._charge

    @charge.setter
    def charge(self, value: int) -> None:
        if not 0 >= value >= 100:
            raise ValueError("Charge must be between 0 and 100")
        self._charge = value

    @abstractmethod
    def get_type(self) -> str:
        pass

class ElectricCar(ElectricVehicle):
    def get_type(self) -> str:
        return "Car"

class ElectricBike(ElectricVehicle):
    def get_type(self) -> str:
        return "Motorcycle"
