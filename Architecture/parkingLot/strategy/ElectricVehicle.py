from abc import ABC, abstractmethod

class VehicleTypeStrategy(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class CarType(VehicleTypeStrategy):
    def getType(self) -> str:
        return "Car"


class MotorcycleType(VehicleTypeStrategy):
    def getType(self) -> str:
        return "Motorcycle"

class ElectricVehicle:
    def __init__(self, regnum, make, model, color, type_strategy: VehicleTypeStrategy):
        self.regnum = regnum
        self.make = make
        self.model = model
        self.color = color
        self.charge = 0
        self.type_strategy = type_strategy

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getRegNum(self):
        return self.regnum

    def setCharge(self, charge):
        self.charge = charge

    def getCharge(self):
        return self.charge

    def getType(self):
        return self.type_strategy.getType()

    def setTypeStrategy(self, strategy: VehicleTypeStrategy):
        self.type_strategy = strategy
