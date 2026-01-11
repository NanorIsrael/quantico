from abc import ABC, abstractmethod

class VehicleTypeStrategy(ABC):
    @abstractmethod
    def type(self) -> str:
        pass

class CarType(VehicleTypeStrategy):
    def type(self) -> str:
        return "Car"


class MotorcycleType(VehicleTypeStrategy):
    def type(self) -> str:
        return "Motorcycle"

class ElectricVehicle:
    def __init__(
        self,
        regnum: str,
        make: str,
        model: str,
        color: str,
        type_strategy: VehicleTypeStrategy
    ):
        self._regnum = regnum
        self._make = make
        self._model = model
        self._color = color
        self._charge = 0
        self._type_strategy = type_strategy

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

    @property
    def charge(self) -> str:
        return self._charge

    @charge.setter
    def charge(self, charge):
        self.charge = charge

    @property
    def type_strategy(self):
        return self._type_strategy.type()

    @type_strategy.setter
    def type_strategy(self, strategy: VehicleTypeStrategy):
        self._type_strategy = strategy
