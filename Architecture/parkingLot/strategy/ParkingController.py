from typing import Any, Dict, List, Tuple
from ParkingLot import ParkingLot

class ParkingController:
    """
        Controller layer:
        - Coordinates between UI and domain
        - Performs no printing or formatting
        - Returns structured data only
    """

    def __init__(self, parking_lot: ParkingLot):
        self._parking_lot = parking_lot

    # ----------------------------
    # Lot management
    # ----------------------------

    def create_lot(self, capacity: int, ev_capacity: int, level: int) -> Dict[str, Any]:
        self._parking_lot.create_parking_lot(capacity, ev_capacity, level)
        return {
            "capacity": capacity,
            "ev_capacity": ev_capacity,
            "level": level
        }

   # ----------------------------
    # Parking operations
    # ----------------------------

    def park_vehicle(self, vehicle, is_ev: bool) -> str:
        slot = self._parking_lot.park(vehicle, is_ev)

        return {
            "success": slot is not None,
            "slot": slot,
            "is_ev": is_ev,
        }

    def remove_vehicle(self, slot: int, is_ev: bool) -> str:    
        return {
            "success": self._parking_lot.leave(slot, is_ev),
            "slot": slot,
        }

    # ----------------------------
    # Queries
    # ----------------------------

    def status(self) -> dict:
        return self._parking_lot.status()

    def charge_status(self) -> list:
        return self._parking_lot.charge_status()
       
    def find_slot_by_reg_num(self, slot_value: str) -> Dict[str, Any]:
        slotnum, slotnum2 = self._parking_lot.get_slot_from_reg_num(slot_value)
        return {
            "slot": slotnum,
            "ev_slot": slotnum2,
        }
    
    def find_slots_by_color(self, color: str) -> Tuple[List[int], List[int]]:
        return self._parking_lot.get_slot_by_color(color)

    def find_regnums_by_color(self, slot_value: str) -> Tuple[List[int], List[int]]:
        return self._parking_lot.get_regnum_by_color(slot_value)
