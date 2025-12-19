from abc import ABC, abstractmethod

class VehicleTypeStrategy(ABC):
    @abstractmethod
    def type(self) -> str:
        pass

class CarType(VehicleTypeStrategy):
    def type(self) -> str:
        return "Car"


class TruckType(VehicleTypeStrategy):
    def type(self) -> str:
        return "Truck"


class MotorcycleType(VehicleTypeStrategy):
    def type(self) -> str:
        return "Motorcycle"


class BusType(VehicleTypeStrategy):
    def type(self) -> str:
        return "Bus"

class Vehicle:
    def __init__(
        self,
        regnum: str,
        make: str,
        model: str,
        color: str,
        vehicle_type: VehicleTypeStrategy
    ):
        self._regnum = regnum
        self._make = make
        self._model = model
        self._color = color
        self._vehicle_type = vehicle_type

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
    def regNum(self) -> str:
        return self._regnum

    def type(self) -> str:
        return self._vehicle_type.type()
