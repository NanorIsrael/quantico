from typing import Any, Dict, List, Tuple
from domain.parking_lot import ParkingLot
from domain.services.vehicle_assembler import VehicleAssembler

class ParkingManager:
    """
        Controller layer:
        - Coordinates between UI and domain
        - Performs no printing or formatting
        - Returns structured data only
    """

    def __init__(self, parking_lot: ParkingLot, vehicle_assembler: VehicleAssembler):
        self._parking_lot = parking_lot
        self._vehicle_assembler = vehicle_assembler
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

    def park_vehicle(self, data: dict) -> Dict[str, Any]:
        vehicle = self._vehicle_assembler.create(data["vehicle"], data["vehicle_kind"], data['is_ev'])
        slot = self._parking_lot.park(vehicle, data['is_ev'])

        return {
            "success": slot is not None,
            "slot": slot
        }

    def remove_vehicle(self, slot: int, is_ev: bool) -> str:
        result = self._parking_lot.leave(slot, is_ev)
        return {
            "success": result,
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
