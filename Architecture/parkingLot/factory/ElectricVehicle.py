from abc import ABC, abstractmethod

class ElectricVehicle(ABC):
    def __init__(self, regnum, make, model, color):
        self.regnum = regnum
        self.make = make
        self.model = model
        self.color = color
        self.charge = 0

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

    @abstractmethod
    def getType(self):
        pass

class ElectricCar(ElectricVehicle):
    def getType(self):
        return "Car"


class ElectricBike(ElectricVehicle):
    def getType(self):
        return "Motorcycle"




from abc import abstractmethod

class ElectricVehicleFactory(ABC):

    @abstractmethod
    def create_vehicle(self, regnum, make, model, color) -> ElectricVehicle:
        pass

class ElectricCarFactory(ElectricVehicleFactory):
    def create_vehicle(self, regnum, make, model, color):
        return ElectricCar(regnum, make, model, color)

class ElectricBikeFactory(ElectricVehicleFactory):
    def create_vehicle(self, regnum, make, model, color):
        return ElectricBike(regnum, make, model, color)
