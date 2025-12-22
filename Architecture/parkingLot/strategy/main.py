from ParkingLot import ParkingLot


def main():
    parkinglot = ParkingLot()

    print("=" * 40)
    print("        Parking Lot Manager")
    print("=" * 40)

    # ---- LOT CREATION ----
    print("\n--- Lot Creation ---")
    num_regular = int(input("Number of Regular Spaces: "))
    num_ev = int(input("Number of EV Spaces: "))
    level = int(input("Floor Level (default 1): ") or 1)

    parkinglot.makeLot(num_regular, num_ev, level)

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

            parkinglot.parkCar(
                make,
                model,
                color,
                reg,
                is_ev,
                is_motor
            )

        elif choice == "2":
            slot = int(input("Slot #: "))
            remove_ev = input("Remove EV? (y/n): ").lower() == "y"
            parkinglot.removeCar(slot, remove_ev)

        elif choice == "3":
            reg = input("Registration #: ")
            parkinglot.slotNumByReg(reg)

        elif choice == "4":
            color = input("Car Color: ")
            parkinglot.slotNumByColor(color)

        elif choice == "5":
            color = input("Car Color: ")
            parkinglot.regNumByColor(color)

        elif choice == "6":
            parkinglot.chargeStatus()

        elif choice == "7":
            parkinglot.status()

        elif choice == "0":
            print("Exiting Parking Lot Manager.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
