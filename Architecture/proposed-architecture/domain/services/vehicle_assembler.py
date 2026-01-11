from domain.electric_vehicle import CarType, MotorcycleType, ElectricVehicle
from domain.vehicle import Vehicle, MotorcycleFactory, CarFactory

class VehicleAssembler:
    def __init__(self):
        self._vehicle_factories = {
            "car": CarFactory(),
            "motorcycle": MotorcycleFactory()
        }
        self._ev_strategies = {
            "car": CarType(),
            "motorcycle": MotorcycleType()
        }

    def create(self, vehicle_data: dict, vehicle_kind: str, is_ev: bool):
        if is_ev:
            strategy = self._ev_strategies[vehicle_kind]
            return ElectricVehicle(
                **vehicle_data,
                type_strategy=strategy
            )

        factory = self._vehicle_factories[vehicle_kind]
        return factory.create_vehicle(**vehicle_data)
