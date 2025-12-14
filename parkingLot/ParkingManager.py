import Vehicle
import ElectricVehicle
import sys
# import tkinter as tk

# root = tk.Tk()
# root.geometry("650x850")
# root.resizable(0,0)
# root.title("Parking Lot Manager")

# #input values
# command_value = tk.StringVar()
# num_value = tk.StringVar()
# ev_value = tk.StringVar()
# make_value = tk.StringVar()
# model_value = tk.StringVar()
# color_value = tk.StringVar()
# reg_value = tk.StringVar()
# level_value = tk.StringVar()
# ev_car_value = tk.IntVar()
# ev_car2_value = tk.IntVar()
# slot1_value = tk.StringVar()
# slot2_value = tk.StringVar()
# reg1_value = tk.StringVar()
# slot_value = tk.StringVar()
# ev_motor_value = tk.IntVar()
# level_remove_value = tk.StringVar()
    
# tfield = tk.Text(root, width=70, height=15)
    
#Parking Lot class
class ParkingLot:
    def __init__(self):
        self.capacity = 0
        self.evCapacity = 0
        self.level = 0
        self.slotid= 0
        self.slotEvId = 0
        self.numOfOccupiedSlots = 0
        self.numOfOccupiedEvSlots = 0

    def createParkingLot(self,capacity,evcapacity,level):
        self.slots = [-1] * capacity
        self.evSlots = [-1] * evcapacity
        self.level = level
        self.capacity = capacity
        self.evCapacity = evcapacity
        return self.level

    def getEmptySlot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def getEmptyEvSlot(self):
        for i in range(len(self.evSlots)):
            if self.evSlots[i] == -1:
                return i

    def getEmptyLevel(self):
        if (self.numOfOccupiedEvSlots == 0 and self.numOfOccupiedSlots == 0):
            return self.level

    def park(self,regnum,make,model,color,ev,motor):
        if (self.numOfOccupiedEvSlots < self.evCapacity or self.numOfOccupiedSlots < self.capacity):
            slotid = -1
            if (ev == 1):
                if self.numOfOccupiedEvSlots < self.evCapacity:
                    slotid = self.getEmptyEvSlot()
                    if (motor == 1):
                        self.evSlots[slotid] = ElectricVehicle.ElectricBike(regnum,make,model,color)
                    else:
                        self.evSlots[slotid] = ElectricVehicle.ElectricCar(regnum,make,model,color)
                    self.slotEvId = self.slotEvId+1
                    self.numOfOccupiedEvSlots = self.numOfOccupiedEvSlots + 1
                    slotid = self.slotEvId
            else:
                if self.numOfOccupiedSlots < self.capacity:
                    slotid = self.getEmptySlot()
                    if (motor == 1):
                        self.slots[slotid] = Vehicle.Car(regnum,make,model,color)
                    else:
                        self.slots[slotid] = Vehicle.Motorcycle(regnum,make,model,color)
                    self.slotid = self.slotid+1
                    self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
                    slotid = self.slotid    
            return slotid
        else:
            return -1

    def leave(self,slotid,ev):
        if (ev == 1):
            if self.numOfOccupiedEvSlots > 0 and self.evSlots[slotid-1] != -1:
                self.evSlots[slotid-1] = -1
                self.numOfOccupiedEvSlots = self.numOfOccupiedEvSlots - 1
                return True
            else:
                return False
        else:
            if self.numOfOccupiedSlots > 0 and self.slots[slotid-1] != -1:
                self.slots[slotid-1] = -1
                self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
                return True
            else:
                return False

    def edit(self,slotid,regnum,make,model,color,ev):
        if (ev == 1):
            self.evSlots[slotid] = ElectricVehicle.ElectricCar(regnum,make,model,color)
            return True
        else:
            self.slots[slotid] = Vehicle.Car(regnum,make,model,color)
            return True
            
        return False     

    def status(self):
        output = "Vehicles\nSlot\tFloor\tReg No.\t\tColor \t\tMake \t\tModel\n"
        # tfield.insert(tk.INSERT, output)\
        print(output)
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                output = str(i+1) + "\t" +str(self.level) + "\t" + str(self.slots[i].regnum) + "\t\t" + str(self.slots[i].color) + "\t\t" +str(self.slots[i].make) +"\t\t" +str(self.slots[i].model) +"\n"                    
                # tfield.insert(tk.INSERT, output)
                print(output)
            else:
                continue
            
        output = "\nElectric Vehicles\nSlot\tFloor\tReg No.\t\tColor \t\tMake \t\tModel\n"
        print(output)
        for i in range(len(self.evSlots)):
            if self.evSlots[i] != -1:
                output = str(i+1) + "\t" +str(self.level) + "\t" + str(self.evSlots[i].regnum) + "\t\t" + str(self.evSlots[i].color) + "\t\t" +str(self.evSlots[i].make) +"\t\t" +str(self.evSlots[i].model) +"\n"                    
                print(output)
            else:
                continue

    def chargeStatus(self):
        output = "Electric Vehicle Charge Levels\nSlot\tFloor\tReg No.\t\tCharge %\n"
        print(output)

        
        for i in range(len(self.evSlots)):
            if self.evSlots[i] != -1:
                output = str(i+1) + "\t" +str(self.level) + "\t" + str(self.evSlots[i].regnum) + "\t\t" + str(self.evSlots[i].charge) +"\n"                    
                print(output)
            else:
                continue

    def getRegNumFromColor(self,color):
        regnums = []
        for i in self.slots:

            if i == -1:
                continue
            if i.color == color:
                regnums.append(i.regnum)
        return regnums
            
    def getSlotNumFromRegNum(self,regnum):
        for i in range(len(self.slots)):
            if (self.slots[i] != -1):
                if self.slots[i].regnum == regnum:
                    return i+1
                else:
                    continue
        return -1
            
    def getSlotNumFromColor(self,color): 
        slotnums = []

        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slotnums.append(str(i+1))
        return slotnums

    def getSlotNumFromMake(self,make): 
        slotnums = []

        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].make == make:
                slotnums.append(str(i+1))
        return slotnums

    def getSlotNumFromModel(self,model): 
        slotnums = []

        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].model == model:
                slotnums.append(str(i+1))
        return slotnums


    def getRegNumFromColorEv(self,color):

        regnums = []
        for i in self.evSlots:

            if i == -1:
                continue
            if i.color == color:
                regnums.append(i.regnum)
        return regnums
            
    def getSlotNumFromRegNumEv(self,regnum):

        for i in range(len(self.evSlots)):
            if (self.evSlots[i] != -1):
                if str(self.evSlots[i].regnum) == str(regnum):
                    return i+1
                else:
                    continue
        return -1
            
    def getSlotNumFromColorEv(self,color): 
        slotnums = []

        for i in range(len(self.evSlots)):          
            if self.evSlots[i] == -1:
                continue
            if self.evSlots[i].color == color:
                slotnums.append(str(i+1))
        return slotnums

    def getSlotNumFromMakeEv(self,make): 
        slotnums = []

        for i in range(len(self.evSlots)):          
            if self.evSlots[i] == -1:
                continue
            if self.evSlots[i].make == make:
                slotnums.append(str(i+1))
        return slotnums

    def getSlotNumFromModelEv(self, model): 
        slotnums = []

        for i in range(len(self.evSlots)):          
            if self.evSlots[i] == -1:
                continue
            if self.evSlots[i].model == model:
                slotnums.append(str(i+1))
        return slotnums

    def slotNumByReg(self, slot1_value):
        slot_val = slot1_value
        slotnum = self.getSlotNumFromRegNum(slot_val)
        slotnum2 = self.getSlotNumFromRegNumEv(slot_val)
        output = ""
        if slotnum >= 0:
            output = "Identified slot: " + str(slotnum) + "\n"
        elif slotnum2 >= 0:
            output = "Identified slot (EV): " + str(slotnum2) + "\n"
        else:
            output = "Not found\n"

        print(output)

    def slotNumByColor(self, slot2_value):
        slotnums = self.getSlotNumFromColor(slot2_value)
        slotnums2 = self.getSlotNumFromColorEv(slot2_value)
        output = "Identified slots: " + ', '.join(slotnums) + "\n"
        print(output)
        output = "Identified slots (EV): " + ', '.join(slotnums2) + "\n"
        print(output)

    def regNumByColor(self, reg1_value):
        regnums = self.getRegNumFromColor(reg1_value)
        regnums2 = self.getRegNumFromColorEv(reg1_value)
        output = "Registation Numbers: "+', '.join(regnums) + "\n"        
        print(output)
        output = "Registation Numbers (EV): "+', '.join(regnums2) + "\n"        
        print( output)

    def makeLot(self, num_value, ev_value, level_value):
        res = self.createParkingLot(int(num_value),int(ev_value),int(level_value))
        output = 'Created a parking lot with '+ str(num_value) +' regular slots and '+ str(ev_value) +' ev slots on level: '+ str(level_value)+ "\n"
        # tfield.insert(tk.INSERT, output)
        print(output)

    def parkCar(self, make_value, model_value, color_value, reg_value, ev_car_value, ev_motor_value):  
        res = self.park(reg_value, make_value, model_value, color_value, ev_car_value, ev_motor_value)
        if res == -1:
            print("Sorry, parking lot is full\n")
        else:
            output = 'Allocated slot number: '+str(res)+ "\n"
            print(output)

    def removeCar(self, slot_value, ev_car2_value):
        status = self.leave(int(slot_value),int(ev_car2_value))
        if status:
            output = 'Slot number '+str(slot_value)+' is free\n'
            print( output)
        else:
            print("Unable to remove a car from slot: " + str(slot_value) + "\n")

             
# def main():

#     parkinglot = ParkingLot()
    
#     #input boxes and GUI
#     label_head= tk.Label(root, text = 'Parking Lot Manager', font = 'Arial 14 bold')
#     label_head.grid(row=0, column=0, padx = 10, columnspan = 4)

#     label_head= tk.Label(root, text = 'Lot Creation', font = 'Arial 12 bold')
#     label_head.grid(row=1, column=0, padx = 10, columnspan = 4)

#     lbl_num = tk.Label(root, text = 'Number of Regular Spaces', font = 'Arial 12')
#     lbl_num.grid(row=2, column=0, padx = 5)

#     num_entry = tk.Entry(root, textvariable = num_value,  width = 6, font='Arial 12')
#     num_entry.grid(row = 2, column=1,  padx = 4, pady = 2)

#     lbl_ev = tk.Label(root, text = 'Number of EV Spaces', font = 'Arial 12')
#     lbl_ev.grid(row=2, column=2, padx = 5)

#     num_entry = tk.Entry(root, textvariable = ev_value,  width = 6, font='Arial 12')
#     num_entry.grid(row = 2, column=3,  padx = 4, pady = 4)

#     lbl_level = tk.Label(root, text = 'Floor Level', font = 'Arial 12')
#     lbl_level.grid(row=3, column=0, padx = 5)
    
#     level_entry = tk.Entry(root, textvariable = level_value,  width = 6, font='Arial 12')
#     level_entry.grid(row = 3, column=1,  padx = 4, pady = 4)
#     level_entry.insert(tk.INSERT, "1")

#     parkMakeBtn = tk.Button(root, command = parkinglot.makeLot, text = "Create Parking Lot", font="Arial 12", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 )
#     parkMakeBtn.grid(row=4, column=0,  padx = 4, pady = 4)

#     label_car= tk.Label(root, text = 'Car Management', font = 'Arial 12 bold')
#     label_car.grid(row=5, column=0, padx = 10, columnspan = 4)

#     lbl_make = tk.Label(root, text = 'Make', font = 'Arial 12')
#     lbl_make.grid(row=6, column=0, padx = 5)

#     make_entry = tk.Entry(root, textvariable = make_value,  width = 12, font='Arial 12')
#     make_entry.grid(row=6, column=1,  padx = 4, pady = 4)

#     lbl_model = tk.Label(root, text = 'Model', font = 'Arial 12')
#     lbl_model.grid(row=6, column=2, padx = 5)

#     model_entry = tk.Entry(root, textvariable = model_value,  width = 12, font='Arial 12')
#     model_entry.grid(row=6, column=3,  padx = 4, pady = 4)
    
#     lbl_color = tk.Label(root, text = 'Color', font = 'Arial 12')
#     lbl_color.grid(row=7, column=0, padx = 5)

#     color_entry = tk.Entry(root, textvariable = color_value,  width = 12, font='Arial 12')
#     color_entry.grid(row=7, column=1,  padx = 4, pady = 4)

#     lbl_reg = tk.Label(root, text = 'Registration #', font = 'Arial 12')
#     lbl_reg.grid(row=7, column=2, padx = 5)
    
#     reg_entry = tk.Entry(root, textvariable = reg_value,  width = 12, font='Arial 12')
#     reg_entry.grid(row=7, column=3,  padx = 4, pady = 4)

#     evToggle = tk.Checkbutton(root, text='Electric',variable=ev_car_value, onvalue=1, offvalue=0, font='Arial 12')
#     evToggle.grid(column=0, row=8,  padx = 4, pady = 4)

#     motorToggle = tk.Checkbutton(root, text='Motorcycle',variable=ev_motor_value, onvalue=1, offvalue=0, font='Arial 12')
#     motorToggle.grid(column=1, row=8,  padx = 4, pady = 4)

#     parkBtn = tk.Button(root, command = parkinglot.parkCar, text = "Park Car", font="Arial 11", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 )
#     parkBtn.grid(column=0, row=9,  padx = 4, pady = 4)

#     lbl_slot = tk.Label(root, text = 'Slot #', font = 'Arial 12')
#     lbl_slot.grid(row=10, column=0, padx = 5)

#     slot_entry = tk.Entry(root, textvariable = slot_value,  width = 12, font='Arial 12')
#     slot_entry.grid(row=10, column=1,  padx = 4, pady = 4)

#     evToggle = tk.Checkbutton(root, text='Remove EV?',variable=ev_car2_value, onvalue=1, offvalue=0, font='Arial 12')
#     evToggle.grid(column=2, row=10,  padx = 4, pady = 4)

#     removeBtn = tk.Button(root, command = parkinglot.removeCar, text = "Remove Car", font="Arial 11", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 )
#     removeBtn.grid(column=0, row=11,  padx = 4, pady = 4)

#     spacer1 = tk.Label(root, text="")
#     spacer1.grid(row=12, column=0)

#     slotRegBtn = tk.Button(root, command = parkinglot.slotNumByReg, text = "Get Slot ID by Registration #", font="Arial 11", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 )
#     slotRegBtn.grid(column=0, row=13,  padx = 4, pady = 4)

#     slot1_entry = tk.Entry(root, textvariable = slot1_value,  width = 12, font='Arial 12')
#     slot1_entry.grid(row=13, column=1,  padx = 4, pady = 4)

#     slotColorBtn = tk.Button(root, command = parkinglot.slotNumByColor, text = "Get Slot ID by Color", font="Arial 11", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 )
#     slotColorBtn.grid(column=2, row=13,  padx = 4, pady = 4)

#     slot2_entry = tk.Entry(root, textvariable = slot2_value,  width = 12, font='Arial 12')
#     slot2_entry.grid(row=13, column=3,  padx = 4, pady = 4)
    
#     regColorBtn = tk.Button(root, command = parkinglot.regNumByColor, text = "Get Registration # by Color", font="Arial 11", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 )
#     regColorBtn.grid(column=0, row=14,  padx = 4, pady = 4)

#     reg1_entry = tk.Entry(root, textvariable = reg1_value,  width = 12, font='Arial 12')
#     reg1_entry.grid(row=14, column=1,  padx = 4, pady = 4)

#     chargeStatusBtn = tk.Button(root, command = parkinglot.chargeStatus, text = "EV Charge Status", font="Arial 11", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 )
#     chargeStatusBtn.grid(column=2, row=14,  padx = 4, pady = 4)

#     statusBtn = tk.Button(root, command = parkinglot.status, text = "Current Lot Status", font="Arial 11", bg='PaleGreen1', fg='black', activebackground="PaleGreen3", padx=5, pady=5 )
#     statusBtn.grid(column=0, row=15,  padx = 4, pady = 4)

#     tfield.grid(column=0, row=16, padx = 10, pady = 10, columnspan = 4)
    
#     root.mainloop()
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
