# import tkinter as tk

# root = tk.Tk()
# root.geometry("650x850")
# root.resizable(0,0)
# root.title("Parking Lot Manager")

# Domain Layer (knows nothing about persistence)
# class Order:
#     def __init__(self, id, items, status):
#         self.id = id
#         self.items = items
#         self.status = status
#         self._events = []
    
#     def cancel(self):
#         if self.status == "SHIPPED":
#             raise DomainError("Cannot cancel shipped order")
#         self.status = "CANCELLED"
#         self._events.append(OrderCancelled(self.id))
    
#     def add_item(self, product, quantity):
#         self.items.append(OrderItem(product, quantity))

# # Service Layer (business logic)
# class OrderProcessingService:
#     def __init__(self, order_repo, inventory_repo, event_publisher):
#         self._orders = order_repo
#         self._inventory = inventory_repo
#         self._publisher = event_publisher
    
#     def cancel_order(self, order_id):
#         # 1. Retrieve domain object
#         order = self._orders.get(order_id)
        
#         # 2. Execute business logic (pure domain operations)
#         order.cancel()
        
#         # 3. Persist changes (abstract persistence)
#         self._orders.save(order)
        
#         # 4. Handle side effects (also abstracted)
#         for event in order.events:
#             self._publisher.publish(event)

# # Repository Interface (abstraction)
# class OrderRepository:
#     def get(self, order_id) -> Order:
#         raise NotImplementedError
    
#     def save(self, order: Order):
#         raise NotImplementedError
    
#     def find_by_customer(self, customer_id) -> List[Order]:
#         raise NotImplementedError

# # Infrastructure Layer (implementation)
# class SqlOrderRepository(OrderRepository):
#     def __init__(self, session):
#         self._session = session
    
#     def get(self, order_id):
#         # Business logic doesn't see this SQL
#         entity = self._session.query(OrderEntity).get(order_id)
#         return self._to_domain(entity)  # Convert to domain object
    
#     def save(self, order):
#         # Business logic doesn't know if this is INSERT or UPDATE
#         entity = self._to_entity(order)
#         self._session.merge(entity)  # Could be insert or update



# from parkingLot.factory.Vehicle import ElectricCarFactory, ElectricVehicleFactory


# def register_vehicle(factory: ElectricVehicleFactory):
#     vehicle = factory.create_vehicle(
#         regnum="EV-123",
#         make="Tesla",
#         model="Model 3",
#         color="Red"
#     )
#     vehicle.setCharge(80)

#     print(vehicle.getType())
#     print(vehicle.getMake(), vehicle.getModel())
#     print("Charge:", vehicle.getCharge())

# register_vehicle(ElectricCarFactory())


from Architecture.parkingLot.strategy import Vehicle
from Architecture.parkingLot.strategy.ElectricVehicle import CarType, ElectricVehicle, MotorcycleType


car = ElectricVehicle(
    "GR-1234",
    "Tesla",
    "Model 3",
    "Red",
    CarType()
)

bike = ElectricVehicle(
    "GR-5678",
    "Zero",
    "SR/F",
    "Black",
    MotorcycleType()
)

print(car.getType())   # Car
print(bike.getType())  # Motorcycle
print(bike.getMake())  # Motorcycle



car = Vehicle(
    regnum="GT-1234-21",
    make="Toyota",
    model="Corolla",
    color="Red",
    vehicle_type=CarType()
)

truck = Vehicle(
    regnum="AS-4567-22",
    make="Volvo",
    model="FH",
    color="Blue",
    vehicle_type=Vehicle.TruckType()
)

print(car.type())    # Car
print(truck.type()) # Truck
