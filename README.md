# quantico
collection of quantico labs sessions


                    <<abstract>>
              +--------------------------+
              |  ElectricVehicleFactory  |
              +--------------------------+
              | + create_vehicle(...)    |
              +--------------------------+
                       ▲
          -------------------------------
          |                             |
+-------------------------+   +-------------------------+
|  ElectricCarFactory     |   |  ElectricBikeFactory    |
+-------------------------+   +-------------------------+
| + create_vehicle(...)   |   | + create_vehicle(...)   |
+-------------------------+   +-------------------------+
          |                             |
          ▼                             ▼
+--------------------+       +--------------------+
|   ElectricCar      |       |   ElectricBike     |
+--------------------+       +--------------------+
| + getType():String |       | + getType():String




        +----------------------+
        |   ElectricVehicle    |
        +----------------------+
        | - type_strategy      |
        +----------------------+
        | + getType()          |
        +----------------------+
                  |
                  v
      <<interface>> VehicleTypeStrategy
                  ▲
          +---------------+   +-------------------+
          |    CarType    |   |  MotorcycleType   |
          +---------------+   +-------------------+





                +----------------------+
                |   ElectricVehicle    |
                +----------------------+
                | - regnum: String     |
                | - make: String       |
                | - model: String      |
                | - color: String      |
                | - charge: int        |
                +----------------------+
                | + getMake(): String  |
                | + getModel(): String |
                | + getColor(): String |
                | + getRegNum(): String|
                | + setCharge(int): void |
                | + getCharge(): int   |
                +----------------------+
                     ▲            ▲
                     |            |
        +------------------+  +------------------+
        |   ElectricCar    |  |  ElectricBike    |
        +------------------+  +------------------+
        |                  |  |                  |
        +------------------+  +------------------+
        | + getType(): String| | + getType(): String|
        +------------------+  +------------------+






ParkingLot
--------------------------------
- capacity: int
- evCapacity: int
- level: int
- slotid: int
- slotEvId: int
- numOfOccupiedSlots: int
- numOfOccupiedEvSlots: int
- slots: List<Vehicle>
- evSlots: List<ElectricVehicle>


+ createParkingLot(capacity: int, evCapacity: int, level: int): int
+ park(regnum, make, model, color, ev, motor): int
+ leave(slotId: int, ev: int): boolean
+ edit(slotId, regnum, make, model, color, ev): boolean
+ status(): void
+ chargeStatus(): void

+ getSlotNumFromRegNum(regnum): int
+ getSlotNumFromColor(color): List<String>
+ getRegNumFromColor(color): List<String>
