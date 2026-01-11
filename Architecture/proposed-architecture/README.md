# Fixed Anti-Patterns
### Vehicle, Electric Vehicle, ParkingLot Classes
* Java-style getters (getMake, getColor, etc.)
	- Attributes are accessed directly
 	- @property is used for control

* Repeating __init__ in subclasses
	- This adds no new behavior
	- If Vehicle.__init__ changes, all subclasses must be updated
	- Replaced with super().__init__(regnum, make, model, color)



* getType() method returning a string
	- Fragile (string-based logic is error-prone)
	- Use a class attribute

* Overusing inheritance for simple classification
	- No subclass adds unique behavior
	- This is a classic over-inheritance smell.

* Manual boilerplate class definition

* Electric Vehicle Class
	- Charge Has No Validation
	- No range checks (e.g. 0–100%)
	- Allows invalid state

* ParkingLot Class
	- Mixing UI logic with domain logic
	- ParkingLot should return data
UI layer should render data
Using magic values (-1) to represent empty slots
-1 has no semantic meaning
You must constantly compare against it
Use None

* Flags instead of types (ev == 1, motor == 1)
	- Boolean flags make code hard to read
	- Logic explodes as features grow
	- Use polymorphism (Vehicle vs ElectricVehicle)

* Manual counters for occupied slots
	- Error-prone
	- Can get out of sync
	- Derive state from data

* Duplicated logic (EV vs non-EV)
	- Abstract common behavior
	- Pass slot list as a parameterior

* Inconsistent indexing (slotid vs index)
	- Easy to introduce off-by-one bugs
	- Internally: 0-based
	- Externally: convert to 1-based only for display

* Naming not pythonic
	- Use snake_case


* ParkingLot Manager (View)
	- ParkingLot is acting as:
		* Domain model
		* Controller
		* View handler
		* UI renderer


## RUN
$ python main.py

