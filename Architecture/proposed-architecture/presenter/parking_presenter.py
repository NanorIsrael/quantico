import enum
from domain.vehicle import Vehicle
from domain.electric_vehicle import ElectricVehicle, MotorcycleType, CarType

class VehicleType(enum.Enum):
    CAR = "car"
    MOTOCYCLE = "motorcycle"


class ParkingPresenter:
    def __init__(self, controller, view):
        self.controller = controller
        self.view = view

    # ---------------- Commands ----------------

    def create_lot(self, capacity: str, ev_capacity: str, level: str):
        try:
            result = self.controller.create_lot(
                int(capacity),
                int(ev_capacity),
                int(level)
            )
        except ValueError:
            self.view.render_error("Invalid numeric input")
            return

        self.view.render(
            f"Created parking lot with {result['capacity']} regular slots "
            f"and {result['ev_capacity']} ev slots on level {result['level']}"
        )

    def park_vehicle(
        self,
        make: str,
        model: str,
        color: str,
        reg: str,
        is_ev: bool,
        is_motor: bool
    ):
        data = {
            "vehicle": {
                "make": make,
                "model": model,
                "color": color,
                "regnum": reg
            },
            "is_ev": is_ev,
            "vehicle_kind": (
                VehicleType.MOTOCYCLE.value
                if is_motor else VehicleType.CAR.value
            )
        }

        result = self.controller.park_vehicle(data)

        if result["success"]:
            self.view.render(f"Allocated slot number {result['slot']}")
        else:
            self.view.render_error("Sorry, parking lot is full")

    def remove_vehicle(self, slot:str, is_ev:bool):
        try:
            slot = int(slot)
        except ValueError:
            self.view.render_error("Slot must be a number")
            return

        result = self.controller.remove_vehicle(slot, is_ev)

        if result["success"]:
            self.view.render(f"Slot number {slot} is free")
        else:
            self.view.render_error("Invalid slot or already empty")

    # ---------------- Queries ----------------

    def status(self):
        data = self.controller.status()

        lines = [
            "Vehicles",
            "Slot\tFloor\tReg No.\t\tColor\tMake\tModel"
        ]

        for slot, v in data["regular"]:
            lines.append(
                f"{slot}\t{data['level']}\t{v.regnum}\t\t{v.color}\t{v.make}\t{v.model}"
            )

        lines.append("")
        lines.append("Electric Vehicles")
        lines.append("Slot\tFloor\tReg No.\t\tColor\tMake\tModel")

        for slot, v in data["electric"]:
            lines.append(
                f"{slot}\t{data['level']}\t{v.regnum}\t\t{v.color}\t{v.make}\t{v.model}"
            )

        self.view.render_lines(lines)

    def charge_status(self):
        data = self.controller.charge_status()

        lines = [
            "Electric Vehicle Charge Levels",
            "Slot\tFloor\tReg No.\t\tCharge %"
        ]

        for v in data:
            lines.append(
                f"{v['slot']}\t{v['level']}\t{v['regnum']}\t\t{v['charge']}"
            )

        self.view.render_lines(lines)

    def find_slot_by_reg_num(self, regnum: str):
        try:
            if not regnum:
                raise ValueError()
        except ValueError:
            self.view.render_error("Registration number is required")
            return
        data = self.controller.find_slot_by_reg_num(regnum)

        if data.get("slot"):
            self.view.render(f"Identified slot: {data['slot'][0]}")
        elif data.get("ev_slot"):
            self.view.render(f"Identified slot (EV): {data['ev_slot'][0]}")
        else:
            self.view.render("Not found")

    def find_slots_by_color(self, color: str):
        try:
            if not color:
                raise ValueError()
        except ValueError:
            self.view.render_error("Color is required")
            return
        slots, ev_slots = self.controller.find_slots_by_color(color)
        lines = [
            "Identified slots: " + ", ".join(slots),
            "Identified slots (EV): " + ", ".join(ev_slots)
        ]

        self.view.render_lines(lines)

    def find_regnums_by_color(self, color: str):
        try:
            if not color:
                raise ValueError()
        except ValueError:
            self.view.render_error("Color is required")
            return
        regs, ev_regs = self.controller.find_regnums_by_color(color)

        lines = [
            "Registration Numbers: " + ", ".join(regs),
            "Registration Numbers (EV): " + ", ".join(ev_regs)
        ]

        self.view.render_lines(lines)
