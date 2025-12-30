from ElectricVehicle import ElectricVehicle, CarType, MotorcycleType
from Vehicle import Vehicle
from ParkingController import ParkingController
from ParkingLot import ParkingLot


def main():
    # parkinglot = ParkingLot()
    parkinglot_controller = ParkingController(ParkingLot())

    print("=" * 40)
    print("        Parking Lot Manager")
    print("=" * 40)

    # ---- LOT CREATION ----
    print("\n--- Lot Creation ---")
    num_regular = int(input("Number of Regular Spaces: "))
    num_ev = int(input("Number of EV Spaces: "))
    level = int(input("Floor Level (default 1): ") or 1)

    result = parkinglot_controller.create_lot(num_regular, num_ev, level)
    output = f"Created a parking lot with {result['capacity']} regular slots and {result['ev_capacity']} EV slots on level {result['level']}"
    print(output)

    while True:
        print("\n--- Car Management ---")
        print("1. Park Car")
        print("2. Remove Car")
        print("3. Get Slot ID by Registration #")
        print("4. Get Slot ID by Color")
        print("5. Get Registration # by Color")
        print("6. EV Charge Status")
        print("7. Current Lot Status")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            make = input("Car Make: ")
            model = input("Car Model: ")
            color = input("Car Color: ")
            reg = input("Registration #: ")

            is_ev = input("Electric? (y/n): ").lower() == "y"
            is_motor = input("Motorcycle? (y/n): ").lower() == "y"

            vehicle_type = CarType() if not is_motor else MotorcycleType()
            vehicle_cls = ElectricVehicle if is_ev else Vehicle
            vehicle = vehicle_cls(reg, make, model, color, vehicle_type)

            result = parkinglot_controller.park_vehicle(vehicle, is_ev)
            print(
                f"Allocated slot number {result['slot']}"
                if result["success"]
                else print("Parking lot is full")
            )
            
        elif choice == "2":
            slot = int(input("Slot #: "))
            remove_ev = input("Remove EV? (y/n): ").lower() == "y"
            result = parkinglot_controller.remove_vehicle(slot, remove_ev)
            
            print(
                f"Slot number {slot} is free"
                if result["success"]
                else "Invalid slot or already empty"
            )
            

        elif choice == "3":
            reg = input("Registration #: ")
            result = parkinglot_controller.find_slot_by_reg_num(reg)
            if result['slot']:
                print(f"Identified slot: " + str(result['slot'][0]) + "\n")
            elif result['ev_slot']:
                print(f"Identified slot (EV): " + str(result['ev_slot'][0]) + "\n") 
            else:
                print("Not found\n")

        elif choice == "4":
            color = input("Car Color: ")
            slotnums, slotnums2 = parkinglot_controller.find_slots_by_color(color)
            output = "Identified slots: " + ', '.join(list(map(lambda num : str(num), slotnums))) + "\n"
            print(output)
            output = "Identified slots (EV): " + ', '.join(list(map(lambda num : str(num), slotnums2))) + "\n"
            print(output)

        elif choice == "5":
            color = input("Car Color: ")
            regnums, regnums2 = parkinglot_controller.find_regnums_by_color(color)
            output = "Registation Numbers: "+', '.join(regnums) + "\n"        
            print(output)
            output = "Registation Numbers (EV): "+', '.join(regnums2) + "\n"        
            print( output)

        elif choice == "6":
            title = "Electric Vehicle Charge Levels\nSlot\tFloor\tReg No.\t\tCharge %\n"
            print(title)
            for v in parkinglot_controller.charge_status():
                print(f"{v['slot']}\t{v['level']}\t{v['regnum']}\t\t{v['charge']}")

        elif choice == "7":
            data = parkinglot_controller.status()
            output = "Vehicles\nSlot\tFloor\tReg No.\t\tColor \t\tMake \t\tModel\n"
            print(output)
            for slot, v in data["regular"]:
                print(str(slot) + "\t" + str(data['level']) + "\t" + v.regnum + "\t\t" + v.color + "\t\t" + v.make +"\t\t" + v.model +"\n")
            output2 = "\nElectric Vehicles\nSlot\tFloor\tReg No.\t\tColor \t\tMake \t\tModel\n"
            print(output2)
            for slot, v in data["electric"]:
                print(str(slot) + "\t" + str(data['level']) + "\t" + v.regnum + "\t\t" + v.color + "\t\t" + v.make +"\t\t" + v.model +"\n")

        elif choice == "0":
            print("Exiting Parking Lot Manager.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
