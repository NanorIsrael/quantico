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
