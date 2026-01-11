import tkinter as tk
from typing import Union, List
from .parking_view_interface import ParkingViewInterface

class ParkingView(ParkingViewInterface):
    def __init__(self, root: tk.TK, presenter):
        self.root = root
        self.presenter = presenter

        self._init_state()
        self._build_layout()

    # ------------------------------------------------------------------
    # State / Variables
    # ------------------------------------------------------------------
    def _init_state(self):
        self.num_value = tk.StringVar()
        self.ev_value = tk.StringVar()
        self.level_value = tk.StringVar(value="1")

        self.make_value = tk.StringVar()
        self.model_value = tk.StringVar()
        self.color_value = tk.StringVar()
        self.reg_value = tk.StringVar()

        self.is_ev_value = tk.IntVar()
        self.is_motor_value = tk.IntVar()

        self.slot_value = tk.StringVar()
        self.remove_is_ev_value = tk.IntVar()

        self.query_reg_value = tk.StringVar()
        self.query_reg_value_color = tk.StringVar()
        self.query_color_value = tk.StringVar()

    # ------------------------------------------------------------------
    # Layout
    # ------------------------------------------------------------------
    def _build_layout(self):
        self._build_header()
        self._build_lot_creation()
        self._build_car_management()
        self._build_queries()
        self._build_output()

    def _build_header(self):
        tk.Label(
            self.root,
            text="Parking Lot Manager",
            font="Arial 14 bold"
        ).grid(row=0, column=0, columnspan=4, pady=5)

    def _build_lot_creation(self):
        tk.Label(self.root, text="Lot Creation", font="Arial 12 bold") \
            .grid(row=1, column=0, columnspan=4, pady=5)

        self._labeled_entry("Number of Regular Spaces", self.num_value, 2, 0, 5, 0, 6)
        self._labeled_entry("Number of EV Spaces", self.ev_value, 2, 2, 5, 0, 6)
        self._labeled_entry("Floor Level", self.level_value, 3, 0, 5, 0, 6)

        tk.Button(
            self.root,
            text="Create Parking Lot",
            command=self.on_create_lot,
            font="Arial 11",
            bg="lightblue"
        ).grid(row=4, column=0, pady=5)

    def _build_car_management(self):
        tk.Label(self.root, text="Car Management", font="Arial 12 bold") \
            .grid(row=5, column=0, columnspan=4, pady=5)

        self._labeled_entry("Make", self.make_value, 6, 0)
        self._labeled_entry("Model", self.model_value, 6, 2)
        self._labeled_entry("Color", self.color_value, 7, 0)
        self._labeled_entry("Registration #", self.reg_value, 7, 2)

        tk.Checkbutton(
            self.root, text="Electric", variable=self.is_ev_value, font="Arial 12"
        ).grid(row=8, column=0)

        tk.Checkbutton(
            self.root, text="Motorcycle", variable=self.is_motor_value, font="Arial 12"
        ).grid(row=8, column=1)

        tk.Button(
            self.root,
            text="Park Vehicle",
            command=self.on_park_vehicle,
            bg="lightblue",
            font="Arial 11",
        ).grid(row=9, column=0, pady=5)

        self._labeled_entry("Slot #", self.slot_value, 10, 0)

        tk.Checkbutton(
            self.root,
            text="Remove EV?",
            variable=self.remove_is_ev_value,
            font="Arial 12"
        ).grid(row=10, column=2)

        tk.Button(
            self.root,
            text="Remove Vehicle",
            command=self.on_remove_vehicle,
            bg="lightblue",
            font="Arial 11",
        ).grid(row=11, column=0, pady=5)

    def _build_queries(self):
        tk.Label(self.root, text="").grid(row=12, column=0)

        tk.Button(
            self.root,
            text="Get Slot by Registration",
            command=self.on_get_slot_by_reg,
            font="Arial 11",
            bg="lightblue"
        ).grid(row=13, column=0)
        
        tk.Entry(
            self.root,
            textvariable=self.query_reg_value,
            font="Arial 12",
            width = 12
        ).grid(row=13, column=1)

        tk.Button(
            self.root,
            text="Get Slots by Color",
            command=self.on_get_slots_by_color,
            font="Arial 11",
            bg="lightblue"
        ).grid(row=13, column=2)

        tk.Entry(
            self.root,
            textvariable=self.query_color_value,
            font="Arial 12",
            width = 12
        ).grid(row=13, column=3)

        tk.Button(
            self.root,
            text="Get Registration by Color",
            command=self.on_get_registration_by_color,
            font="Arial 11",
            bg="lightblue"
        ).grid(row=14, column=0, pady=5)

        tk.Entry(
            self.root,
            textvariable=self.query_reg_value_color,
            font="Arial 12",
            width = 12
        ).grid(row=14, column=1, pady=5)

        tk.Button(
            self.root,
            text="EV Charge Status",
            command=self.on_get_ev_charge_status,
            font="Arial 11",
            bg="lightblue"
        ).grid(row=14, column=2)

        tk.Button(
            self.root,
            text="Current Lot Status",
            command=self.on_get_lot_status,
            bg="PaleGreen1",
            font="Arial 11"
        ).grid(row=15, column=0)

    def _build_output(self):
        self.output = tk.Text(self.root, width=70, height=15)
        self.output.grid(row=16, column=0, columnspan=4, pady=10)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _labeled_entry(self, label, variable, row, column, padx=0, pady=0, w=12):
        tk.Label(self.root, text=label, font='Arial 12').grid(row=row, column=column, padx=padx, pady=pady)
        tk.Entry(self.root, textvariable=variable, width=w, font='Arial 12') \
            .grid(row=row, column=column + 1)

    
    def render(self, message: str) -> None:
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)

    def render_lines(self, lines) -> None:
        for line in lines:
            self.render(line)

    def render_error(self, message: str) -> None:
        self.output.insert(tk.END, f"ERROR: {message}\n")
        self.output.see(tk.END)

    # ------------------------------------------------------------------
    # Event Handlers
    # ------------------------------------------------------------------
    def on_create_lot(self):
        self.presenter.create_lot(
            self.num_value.get(),
            self.ev_value.get(),
            self.level_value.get()
        )

    def on_park_vehicle(self):
        self.presenter.park_vehicle(
            self.make_value.get(),
            self.model_value.get(),
            self.color_value.get(),
            self.reg_value.get(),
            bool(self.is_ev_value.get()),
            bool(self.is_motor_value.get())
        )
    

    def on_remove_vehicle(self):
        self.presenter.remove_vehicle(
            self.slot_value.get(),
            bool(self.remove_is_ev_value.get())
        )


    def on_get_slot_by_reg(self):
        self.presenter.find_slot_by_reg_num(
            self.query_reg_value.get()
        )


    def on_get_slots_by_color(self):
        self.presenter.find_slots_by_color(
            self.query_color_value.get()
        )


    def on_get_registration_by_color(self):
        self.presenter.find_regnums_by_color(
            self.query_reg_value_color.get() 
        )


    def on_get_ev_charge_status(self):
        self.presenter.charge_status()

    def on_get_lot_status(self):
        self.presenter.status()