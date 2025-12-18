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
