from Vehicle import Vehicle, CarType as VCarType, MotorcycleType as VMotorcycleType
from ElectricVehicle import ElectricVehicle, CarType, MotorcycleType


class ParkingLot:
    def __init__(self):
        self._capacity = 0
        self._ev_capacity = 0
        self._level = 0
        self._slot_id = 0
        self._slot_ev_id = 0
        self._num_of_occupied_slots = 0
        self._num_of_occupied_ev_slots = 0

    def create_parking_lot(self, capacity:int, evcapacity:int, level:int) -> int:
        self.slots = [-1] * capacity
        self.ev_slots = [-1] * evcapacity
        self._level = level
        self._capacity = capacity
        self._ev_capacity = evcapacity
        return self._level

    def get_empty_slot(self) -> int:
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def get_empty_ev_slot(self) -> int:
        for i in range(len(self.ev_slots)):
            if self.ev_slots[i] == -1:
                return i

    def get_empty_level(self) -> int:
        if (self._num_of_occupied_ev_slots == 0 and self._num_of_occupied_slots == 0):
            return self._level

    def park(self, regnum: str, make: str, model: str, color: str, ev: int, motor: int) -> int:
        if (self._num_of_occupied_ev_slots < self._ev_capacity or self._num_of_occupied_slots < self._capacity):
            slotid = -1
            if (ev == 1):
                if self._num_of_occupied_ev_slots < self._ev_capacity:
                    slotid = self.get_empty_ev_slot()
                    if (motor == 1):
                        self.ev_slots[slotid] = ElectricVehicle(regnum, make, model, color, MotorcycleType())
                    else:
                        self.ev_slots[slotid] = ElectricVehicle(regnum, make, model, color, CarType())
                    self.slot_ev_id = self.slot_ev_id + 1
                    self._num_of_occupied_ev_slots = self._num_of_occupied_ev_slots + 1
                    slotid = self.slot_ev_id
            else:
                if self._num_of_occupied_slots < self._capacity:
                    slotid = self.get_empty_slot()
                    if (motor == 1):
                        self.slots[slotid] = Vehicle(regnum, make, model, color, vehicle_type=VCarType())
                    else:
                        self.slots[slotid] = Vehicle(regnum, make, model, color, vehicle_type=VMotorcycleType())
                    self._slot_id = self._slot_id + 1
                    self._num_of_occupied_slots = self._num_of_occupied_slots + 1
                    slotid = self._slot_id    
            return slotid
        else:
            return -1

    def leave(self, slotid: int, ev: int) -> int:
        if (ev == 1):
            if self._num_of_occupied_ev_slots > 0 and self.ev_slots[slotid - 1] != -1:
                self.ev_slots[slotid - 1] = -1
                self._num_of_occupied_ev_slots = self._num_of_occupied_ev_slots - 1
                return True
            else:
                return False
        else:
            if self._num_of_occupied_slots > 0 and self.slots[slotid - 1] != -1:
                self.slots[slotid - 1] = -1
                self._num_of_occupied_slots = self._num_of_occupied_slots - 1
                return True
            else:
                return False

    def edit(self, slotid: int, regnum: str, make: str, model: str, color: str, ev: int) -> int:
        if (ev == 1):
            self.ev_slots[slotid] = ElectricVehicle(regnum, make, model, color, CarType())
            return True
        else:
            self.slots[slotid] = Vehicle(regnum, make, model, color, VCarType())
            return True
   

    def status(self) -> int:
        output = "Vehicles\nSlot\tFloor\tReg No.\t\tColor \t\tMake \t\tModel\n"
        # tfield.insert(tk.INSERT, output)\
        print(output)
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                output = str(i+1) + "\t" +str(self._level) + "\t" + str(self.slots[i].regnum) + "\t\t" + str(self.slots[i].color) + "\t\t" +str(self.slots[i].make) +"\t\t" +str(self.slots[i].model) +"\n"                    
                # tfield.insert(tk.INSERT, output)
                print(output)
            else:
                continue
            
        output = "\nElectric Vehicles\nSlot\tFloor\tReg No.\t\tColor \t\tMake \t\tModel\n"
        print(output)
        for i in range(len(self.ev_slots)):
            if self.ev_slots[i] != -1:
                output = str(i+1) + "\t" +str(self._level) + "\t" + str(self.ev_slots[i].regnum) + "\t\t" + str(self.ev_slots[i].color) + "\t\t" +str(self.ev_slots[i].make) +"\t\t" +str(self.ev_slots[i].model) +"\n"                    
                print(output)
            else:
                continue

    def charge_status(self) -> int:
        output = "Electric Vehicle Charge Levels\nSlot\tFloor\tReg No.\t\tCharge %\n"
        print(output)
        for i in range(len(self.ev_slots)):
            if self.ev_slots[i] != -1:
                output = str(i+1) + "\t" +str(self._level) + "\t" + str(self.ev_slots[i].regnum) + "\t\t" + str(self.ev_slots[i].charge) +"\n"                    
                print(output)
            else:
                continue

    def get_reg_num_from_color(self, color: str) -> int:
        regnums = []
        for i in self.slots:

            if i == -1:
                continue
            if i.color == color:
                regnums.append(i.regnum)
        return regnums
            
    def get_slot_num_from_reg_num(self, regnum: str) -> int:
        for i in range(len(self.slots)):
            if (self.slots[i] != -1):
                if self.slots[i].regnum == regnum:
                    return i+1
                else:
                    continue
        return -1
            
    def get_slot_num_from_color(self, color: str) -> int:
        slotnums = []

        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slotnums.append(str(i+1))
        return slotnums

    def get_slot_num_from_make(self, make: str) -> int: 
        slotnums = []

        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].make == make:
                slotnums.append(str(i+1))
        return slotnums

    def get_slot_num_from_model(self, model: str) -> int: 
        slotnums = []

        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].model == model:
                slotnums.append(str(i+1))
        return slotnums


    def get_reg_num_from_color_ev(self, color: str) -> int:

        regnums = []
        for i in self.ev_slots:

            if i == -1:
                continue
            if i.color == color:
                regnums.append(i.regnum)
        return regnums
            
    def get_slot_num_from_reg_num_ev(self, regnum: str) -> int:

        for i in range(len(self.ev_slots)):
            if (self.ev_slots[i] != -1):
                if str(self.ev_slots[i].regnum) == str(regnum):
                    return i+1
                else:
                    continue
        return -1
            
    def get_slot_num_from_color_ev(self, color: str) -> int: 
        slotnums = []

        for i in range(len(self.ev_slots)):          
            if self.ev_slots[i] == -1:
                continue
            if self.ev_slots[i].color == color:
                slotnums.append(str(i+1))
        return slotnums

    def get_slot_num_from_make_ev(self, make: str) -> int:
        slotnums = []

        for i in range(len(self.ev_slots)):          
            if self.ev_slots[i] == -1:
                continue
            if self.ev_slots[i].make == make:
                slotnums.append(str(i+1))
        return slotnums

    def get_slot_num_from_model_ev(self, model: str) -> int: 
        slotnums = []

        for i in range(len(self.ev_slots)):          
            if self.ev_slots[i] == -1:
                continue
            if self.ev_slots[i].model == model:
                slotnums.append(str(i+1))
        return slotnums

    def slot_num_by_reg(self, slot1_value: str) -> int:
        slot_val = slot1_value
        slotnum = self.get_slot_num_from_reg_num(slot_val)
        slotnum2 = self.get_slot_num_from_reg_num_ev(slot_val)
        output = ""
        if slotnum >= 0:
            output = "Identified slot: " + str(slotnum) + "\n"
        elif slotnum2 >= 0:
            output = "Identified slot (EV): " + str(slotnum2) + "\n"
        else:
            output = "Not found\n"

        print(output)

    def slot_num_by_color(self, slot2_value: str) -> int:
        slotnums = self.get_slot_num_from_color(slot2_value)
        slotnums2 = self.get_slot_num_from_color_ev(slot2_value)
        output = "Identified slots: " + ', '.join(slotnums) + "\n"
        print(output)
        output = "Identified slots (EV): " + ', '.join(slotnums2) + "\n"
        print(output)

    def reg_num_by_color(self, reg1_value: str) -> None:
        regnums = self.get_reg_num_from_color(reg1_value)
        regnums2 = self.get_reg_num_from_color_ev(reg1_value)
        output = "Registation Numbers: "+', '.join(regnums) + "\n"        
        print(output)
        output = "Registation Numbers (EV): "+', '.join(regnums2) + "\n"        
        print( output)

    def make_lot(self, num_value: int, ev_value: int, level_value: int) -> None:
        res = self.create_parking_lot(int(num_value), int(ev_value), int(level_value))
        output = 'Created a parking lot with '+ str(num_value) +' regular slots and '+ str(ev_value) +' ev slots on level: '+ str(level_value)+ "\n"
        # tfield.insert(tk.INSERT, output)
        print(output)

    def park_car(self, make_value: str, model_value: str, color_value: str, reg_value: str, ev_car_value: str, ev_motor_value: str) -> None:  
        res = self.park(reg_value, make_value, model_value, color_value, ev_car_value, ev_motor_value)
        if res == -1:
            print("Sorry, parking lot is full\n")
        else:
            output = 'Allocated slot number: '+str(res)+ "\n"
            print(output)

    def remove_car(self, slot_value: int, ev_car2_value: int) -> None:
        status = self.leave(int(slot_value),int(ev_car2_value))
        if status:
            output = 'Slot number '+str(slot_value)+' is free\n'
            print( output)
        else:
            print("Unable to remove a car from slot: " + str(slot_value) + "\n")

