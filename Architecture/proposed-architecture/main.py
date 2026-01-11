import tkinter as tk
from domain.parking_lot import ParkingLot
from domain.services.vehicle_assembler import VehicleAssembler
from controller.parking_manager import ParkingManager
from presenter.parking_presenter import ParkingPresenter
from view.parking_view import ParkingView


def main():

    root = tk.Tk()
    root.geometry("650x850")
    root.resizable(False, False)
    root.title("Parking Lot Manager")

    # ----- Domain / Controller -----
    parking_lot = ParkingLot()
    vehicle_assembler = VehicleAssembler()
    parking_manager = ParkingManager(parking_lot, vehicle_assembler)

    # ----- View (no presenter yet) -----
    view = ParkingView(root, presenter=None)

    # ----- Presenter (inject view) -----
    presenter = ParkingPresenter(
        controller=parking_manager,
        view=view
    )

    # ----- Complete the circle -----
    view.presenter = presenter

    root.mainloop()



if __name__ == '__main__':
    main()
