from typing import Any, List, Optional, Dict, Tuple
from domain.electric_vehicle import ElectricVehicle
from domain.vehicle import Vehicle

class ParkingLot:
    """
    ParkingLot is responsible ONLY for parking logic.
    It does NOT handle input/output or UI concerns.
    """
    def __init__(self):
        self._capacity: int = 0
        self._ev_capacity: int = 0
        self._level: int = 0
        self._slots: List[Optional[Vehicle]] = []
        self._ev_slots: List[Optional[ElectricVehicle]] = []

    def create_parking_lot(self, capacity:int, evcapacity:int, level:int) -> None:
        self._slots = [None] * capacity
        self._ev_slots = [None] * evcapacity

        self._level = level
        self._capacity = capacity
        self._ev_capacity = evcapacity

    def _get_first_empty_slot(self, slots: List[Optional[object]]) -> Optional[int]:
        for index, slot in enumerate(slots):
            if slot is None:
                return index
        return None

    def _find_slots_by_attr(self, slots: List[Optional[object]], attr: str, value):
        return [
            str(index + 1)
            for index, vehicle in enumerate(slots)
            if vehicle is not None and getattr(vehicle, attr).lower() == value.lower()
        ]

    def _find_regnum_by_attr(self, slots: List[Optional[object]], attr: str, value):
        return [
            vehicle.regnum
            for vehicle in slots
            if vehicle is not None and getattr(vehicle, attr).lower() == value.lower()
        ]


    def park(self, vehicle: Vehicle, is_ev: bool) -> Optional[int]:
        """
		Returns allocated slot number (1-based) or None if full.
		"""
        slots = self._ev_slots if is_ev else self._slots

        if slots.count(None) == 0:
            return None

        index = self._get_first_empty_slot(slots)
        if index is None:
            return None

        slots[index] = vehicle
        return index + 1


    def leave(self, slot_number: int, is_ev: bool) -> bool:
        slots = self._ev_slots if is_ev else self._slots
        index = slot_number - 1

        if index < 0 or index >= len(slots):
            return False

        if slots[index] is None:
            return False
 
        slots[index] = None
        return True
   

    def status(self) -> Dict[str, Any]:
        return {
            "level": self._level,
            "regular": [
                (i+1, v) for i, v in enumerate(self._slots) if v is not None
            ],
            "electric": [
                (i+1, v) for i, v in enumerate(self._ev_slots) if v is not None
            ]
		}

    def charge_status(self) -> List[Dict[str, Any]]:
        return [
            {
                "slot": i + 1,
                "level": self._level,
                "regnum": v.regnum,
                "charge": v.charge
            }
            for i, v in enumerate(self._ev_slots) if v is not None
        ]
            
    def get_slot_from_reg_num(self, regnum: str) -> Tuple[List[int], List[int]]:
        slotnum = self._find_slots_by_attr(self._slots, "regnum", regnum)
        slotnum2 = self._find_slots_by_attr(self._ev_slots, "regnum", regnum)
        return slotnum, slotnum2
  
    def get_slot_by_color(self, slot2_value: str) -> Tuple[List[int], List[int]]:
        slotnum = self._find_slots_by_attr(self._slots, "color", slot2_value)
        slotnum2 = self._find_slots_by_attr(self._ev_slots, "color", slot2_value)
        return slotnum, slotnum2

    def get_regnum_by_color(self, reg1_value: str) -> Tuple[List[int], List[int]]:
        regnums = self._find_regnum_by_attr(self._slots, "color", reg1_value)
        regnums2 = self._find_regnum_by_attr(self._ev_slots, "color", reg1_value)
        return regnums, regnums2


