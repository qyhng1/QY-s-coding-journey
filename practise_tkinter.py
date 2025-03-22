import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from customtkinter import *
from random import choice
import mysql.connector
import csv
import pandas as pd
import numpy as np
import re




# list of material cost, would like it to be updated weekly or monthly preferably it's auto
materialCost = {
    "SUS304-0.3":           48.00,
    "SUS304-0.5":	        60.00,
    "SUS304-0.8":	        86.00,
    "SUS304-1.0":	        102.00,
    "SUS304-1.2":	        122.00,
    "SUS304-1.5":	        150.00,
    "SUS304-1.6":	        187.00,
    "SUS304-2.0":	        198.00,
    "SUS304-2.3":	        225.00,
    "SUS304-2.5":	        255.00,
    "SUS304-3.0":	        312.00,
    "SUS304-3.5":	        343.00,
    "SUS304-4.0":	        520.00,
    "SUS304-5.0":	        670.00,
    "SUS304-6.0":	        700.00,
    "SUS304-8.0":	        740.00,
    "SUS304-10.0":	        920.00,
    "SUS304-12.0":	        1100.00,
    "SUS316-0.5":	        92.00,
    "SUS316-1.0":	        179.00,
    "SUS316-1.2":	        214.00,
    "SUS316-1.5":	        267.00,
    "SUS316-2.0":      	    354.00,
    "SUS316-2.5":	        442.00,
    "SUS316-3.0":	        531.00,
    "SUS316-4.0":	        761.00,
    "SUS316-5.0":	        950.00,
    "ALU5052-0.5":	        32.00,
    "ALU5052-1.0":	        41.00,
    "ALU5052-1.5":	        75.00,
    "ALU5052-2.0":	        105.00,
    "ALU5052-2.5":	        120.00,
    "ALU5052-3.0":	        140.00,
    "ALU5052-4.0":	        168.00,
    "ALU5052-5.0":	        236.00,
    "ALU5052-6.0":	        250.00,
    "ALU6061-8.0":	        515.00,
    "ALU6061-10.0":	        726.00,
    "ALU6061-12.0":	        860.00,
    "ALU6061-15.0":	        1095.00,
    "AL5083-2.0":	        146.00,
    "AL5083-3.0": 	        185.00,
    "AL5083-4.0":      	    205.00,
    "AL5083-5.0": 	        260.00,
    "AL5083-6.0":           310.00,
    "AL6061-1.27":	        360.00,
    "AL6061-2.0": 	        125.00,
    "MS-1.5":	            80.00,
    "MS-2.0":	            100.00,
    "MS-3.0":	            150.00,
    "MS-4.0":          	    160.00,
    "MS-5.0":	            170.00,
    "MS-6.0":	            180.00,
    "MS-9.0":	            210.00,
    "MS-10.0":         	    240.00,
    "MS-12.0":	            280.00,
    "MS-15.0":        	    350.00,
    "MS-16.0":	            360.00,
    "MS-20.0":	            500.00,
    "MS-25.0":	            730.00,
    "EG-0.5":               50.00,
    "EG-0.8":               50.00,
    "EG-1.0":	            60.00,
    "EG-1.2":	            70.00,
    "EG-1.5":	            80.00,
    "EG-2.0":	            100.00,
    "EG-2.5":          	    130.00,
    "EG-3.0":	            150.00,
    "Plastic":              50.00,
}

treatmentCost = {
    "None":                 1.00,
    "Powder coat":          93025.00,
    "Clear Anodise":        0.06,
    "Black Anodise":        0.12,
    "Hard Clear Anodise":   0.15,
    "Hard Black Anodise":   0.20,
    "Colour Anodise":       0.20,
    "EN":                   0.13,
    "Flash Chrome":         0.15,
    "Hard Chrome":          0.20,
    "Black Oxide":          1.5,
    "Zinc plating":         0.11,
    "EP":                   0.10,
}

thickness = [
            "0.2",
            "0.3",
            "0.4",
            "0.5",
            "0.6",
            "0.7",
            "0.8",
            "0.9",
            "1.0",
            "1.2",
            "1.5",
            "1.6",
            "2.0",
            "2.3",
            "2.5",
            "3.0",
            "3.5",
            "4.0",
            "4.5",
            "5.0",
            "6.0",
            "8.0",
            "9.0",
            "10.0",
            "12.0",
            "15.0",
            "16.0",
            "20.0",
            "25.0"
        ]

difficulty = [
            "Easy",
            "Normal",
            "Hard"
        ]

ans = [
            "Yes",
            "No"
        ]

materialList = [
    "SUS",
    "ALU",
    "STEEL"
]

materialList_machining = {
    "SUS": 0.00013,
    "ALU": 0.000025,
    "STEEL": 0.00013,
    "DERLIN": 0.000016
}

materialType = [
    "Square tube",
    "Pipe"
]

sizePipe = [
    "Ø10",
    "Ø20",
    "Ø25",
    "Ø30",
    "Ø50"
]

sizesTube = [
    "10x10",
    "12x12",
    "20x20",
    "25x25",
    "50x50"
]

class App(CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (size[0] / 2)
        y = (screen_height / 2) - (size[1] / 2)

        self.geometry(f'{size[0]}x{size[1]}+{int(x)}+{int(y)}')
        self.minsize(size[0],size[1])

        # calling MainMenu Frame
        self.frame = MainMenu(self)





        self.mainloop()

class MainMenu(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        CTkButton(self, text='Quotation Calculator', font=('Algerian', 30), command=self.open_QuotationCalculator).pack(expand=True, fill='both', padx=5, pady=5)
        CTkButton(self, text='Create Sales Order', font=('Algerian', 30), command=self.open_SalesOrderCreate).pack(expand=True, fill='both', padx=5, pady=5)
        CTkButton(self, text='Workshop Scheduling', font=('Algerian', 30), command=self.open_WorkshopScheduling).pack(expand=True, fill='both', padx=5, pady=5)
        CTkButton(self, text='Logistic', font=('Algerian', 30), command=self.open_Logistic).pack(expand=True, fill='both', padx=5, pady=5)
        CTkButton(self, text='SSH Database', font=('Algerian', 30), command=self.open_SSHDatabase).pack(expand=True, fill='both', padx=5, pady=5)
        self.pack(expand=True, fill='both')

        self.quotation_calculator_window = None
        self.sales_order_create_window = None
        self.workshop_scheduling_window = None
        self.logistic_window = None
        self.ssh_database_window = None

    # Method to open only 1 window at any time and taking focus when Menu button are pressed
    def open_QuotationCalculator(self):
        if self.quotation_calculator_window is None or not self.quotation_calculator_window.winfo_exists():
            self.quotation_calculator_window = QuotationCalculator(self,'Quotation Calculator', (800, 1000))

        else:
            self.quotation_calculator_window.focus()
            self.quotation_calculator_window.deiconify()

    def open_SalesOrderCreate(self):
        if self.sales_order_create_window is None or not self.sales_order_create_window.winfo_exists():
            self.sales_order_create_window = SalesOrderCreate(self,'Sales Order Create', (800, 1000))

        else:
            self.sales_order_create_window.focus()
            self.sales_order_create_window.deiconify()


    def open_WorkshopScheduling(self):
        if self.workshop_scheduling_window is None or not self.workshop_scheduling_window.winfo_exists():
            self.workshop_scheduling_window = WorkshopScheduling(self,'Workshop Scheduling', (800, 1000))

        else:
            self.workshop_scheduling_window.focus()
            self.workshop_scheduling_window.deiconify()

    def open_Logistic(self):
        if self.logistic_window is None or not self.logistic_window.winfo_exists():
            self.logistic_window = Logistic(self,'Logistic', (800, 1000))

        else:
            self.logistic_window.focus()
            self.logistic_window.deiconify()

    def open_SSHDatabase(self):
        if self.ssh_database_window is None or not self.ssh_database_window.winfo_exists():
            self.ssh_database_window = SSHDatabase(self,'SSH Database', (1200, 1000))


        else:
            self.ssh_database_window.focus()
            self.ssh_database_window.deiconify()



# Actual window of each individual function
class QuotationCalculator(CTkToplevel):
    def __init__(self, parent, title, size):
        super().__init__(parent)

        self.title(title)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (size[0] / 2)
        y = (screen_height / 2) - (size[1] / 2)

        self.geometry(f'{size[0]}x{size[1]}+{int(x)}+{int(y)}')
        self.focus()


        QuotationCalculator_widgets(self)

class QuotationCalculator_widgets(CTkTabview):
    def __init__(self, parent):
        super().__init__(parent)

        self.AddSheetMetalTab()
        self.AddMachiningTab()
        self.AddStructureTab()



    # method to add tab onto Tabview
    def AddSheetMetalTab(self):
        # create tabs (sheet metal, machining, structure)
        self.add("Sheet Metal calculator")
        unit_factor = 1

        # mini calculator function for Sheet Metal tab
        def do_math(e, event):
            eqn = e.get()
            cond = str(e).split('.!')

            if not re.search(r'[a-zA-Z]', eqn):
                ans = str(eval(eqn))
                # print(cond) # To check if I am able to use this as a condition

                if cond[-1] == "ctkentry":
                    length_entry.delete(0, END)
                    length_entry.insert(0, ans)

                elif cond[-1] == "ctkentry2":
                    width_entry.delete(0, END)
                    width_entry.insert(0, ans)

                elif cond[-1] == "PY_VAR3":
                    number_of_bend_entry.delete(0, END)
                    number_of_bend_entry.insert(0, ans)

                elif cond[-1] == "PY_VAR4":
                    number_of_thru_holes_entry.delete(0, END)
                    number_of_thru_holes_entry.insert(0, ans)

                elif cond[-1] == "PY_VAR5":
                    number_of_special_holes_entry.delete(0, END)
                    number_of_special_holes_entry.insert(0, ans)

                elif cond[-1] == "PY_VAR6":
                    number_of_weldings_entry.delete(0, END)
                    number_of_weldings_entry.insert(0, ans)


            else:
                messagebox.showwarning(title="Warning!", message="This entry box accepts numbers only.")
                if cond[-1] == "ctkentry":
                    length_entry.delete(0, END)
                    length_entry.focus()

                elif cond[-1] == "ctkentry2":
                    width_entry.delete(0, END)
                    width_entry.focus()

                elif cond[-1] == "PY_VAR3":
                    number_of_bend_entry.delete(0, END)
                    number_of_bend_entry.focus()

                elif cond[-1] == "PY_VAR4":
                    number_of_thru_holes_entry.delete(0, END)
                    number_of_thru_holes_entry.focus()

                elif cond[-1] == "PY_VAR5":
                    number_of_special_holes_entry.delete(0, END)
                    number_of_special_holes_entry.focus()

                elif cond[-1] == "PY_VAR6":
                    number_of_weldings_entry.delete(0, END)
                    number_of_weldings_entry.focus()


        # actual calculator function
        def quote_sheet_metal():

            def get_unfold_size():
                global unfold_size, percentage_of_material_used

                unfold_size = 0
                percentage_of_material_used = 0

                unfold_size = (float(length_entry_var.get()) * unit_factor) * (float(width_entry_var.get()) * unit_factor)
                # Check unfold size for both inches and mm
                # print(unfold_size)
                percentage_of_material_used = unfold_size / 2880000

                # statement to check if calculation is correct
                # print(percentage_of_material_used)

                return unfold_size, percentage_of_material_used

            def get_material_cost():
                global material_cost_sus304, material_cost_sus316, material_cost_alu5052, material_cost_alu6061, material_cost_eg, material_cost_ms

                material_cost_sus304 = 0
                material_cost_sus316 = 0
                material_cost_alu5052 = 0
                material_cost_alu6061 = 0
                material_cost_eg = 0
                material_cost_ms = 0

                for cost in materialCost:
                    if cost == "SUS304" + "-" + str(thickness_entry_var.get()):
                        material_cost_sus304 = materialCost.get(cost)


                    if cost == "SUS316" + "-" + str(thickness_entry_var.get()):
                        material_cost_sus316 = materialCost.get(cost)


                    if cost == "ALU5052" + "-" + str(thickness_entry_var.get()):
                        material_cost_alu5052 = materialCost.get(cost)


                    if cost == "ALU6061" + "-" + str(thickness_entry_var.get()):
                        material_cost_alu6061 = materialCost.get(cost)


                    if cost == "EG" + "-" + str(thickness_entry_var.get()):
                        material_cost_eg = materialCost.get(cost)


                    if cost == "MS" + "-" + str(thickness_entry_var.get()):
                        material_cost_ms = materialCost.get(cost)

                # statement to check if calculation is correct
                # print(material_cost_sus304, material_cost_sus316, material_cost_alu5052, material_cost_alu6061, material_cost_eg, material_cost_ms)

                return material_cost_sus304, material_cost_sus316, material_cost_alu5052, material_cost_alu6061, material_cost_eg, material_cost_ms

            def calculate_raw_material_cost():
                global raw_cost_sus304, raw_cost_sus316, raw_cost_alu5052, raw_cost_alu6061, raw_cost_eg, raw_cost_ms

                raw_cost_sus304 = percentage_of_material_used * (material_cost_sus304 * 1.1)
                raw_cost_sus316 = percentage_of_material_used * (material_cost_sus316 * 1.1)
                raw_cost_alu5052 = percentage_of_material_used * (material_cost_alu5052 * 1.1)
                raw_cost_alu6061 = percentage_of_material_used * (material_cost_alu6061 * 1.1)
                raw_cost_eg = percentage_of_material_used * (material_cost_eg * 1.1)
                raw_cost_ms = percentage_of_material_used * (material_cost_ms * 1.1)


                # statement to check if calculation is correct
                # print(raw_cost_sus304, raw_cost_sus316, raw_cost_alu5052, raw_cost_alu6061, raw_cost_eg, raw_cost_ms)

                return raw_cost_sus304, raw_cost_sus316, raw_cost_alu5052, raw_cost_alu6061, raw_cost_eg, raw_cost_ms

            def bending_calculation():
                global cost_of_bend

                cost_of_bend = 0
                # bending work calculation
                if not length_entry_var.get() == "0" or width_entry_var.get() == "0" or length_entry_var.get() == "" or width_entry_var.get() == "":
                    if float(length_entry_var.get()) == float(width_entry_var.get()):
                        bend_length = (float(length_entry_var.get()) * unit_factor)
                    elif float(length_entry_var.get()) < float(width_entry_var.get()):
                        bend_length = (float(width_entry_var.get()) * unit_factor)
                    elif float(length_entry_var.get()) > float(width_entry_var.get()):
                        bend_length = (float(length_entry_var.get()) * unit_factor)

                    if float(bend_length) <= 300:
                        cost_of_bend = float(number_of_bend_entry_var.get()) * 3
                    elif float(bend_length) > 300 and float(bend_length) <= 500:
                        cost_of_bend = float(number_of_bend_entry_var.get()) * 4
                    elif float(bend_length) > 500 and int(bend_length) <= 990:
                        cost_of_bend = float(number_of_bend_entry_var.get()) * 5
                    else:
                        cost_of_bend = float(number_of_bend_entry_var.get()) * 10

                return cost_of_bend

            def welding_calculation():
                global cost_of_weld
                # welding work calculation
                if float(length_entry_var.get()) == float(width_entry_var.get()):
                    weld_length = (float(length_entry_var.get()) * unit_factor)
                elif float(length_entry_var.get()) < float(width_entry_var.get()):
                    weld_length = (float(width_entry_var.get()) * unit_factor)
                elif float(length_entry_var.get()) > float(width_entry_var.get()):
                    weld_length = (float(length_entry_var.get()) * unit_factor)

                if float(weld_length) <= 300:
                    cost_of_weld = float(number_of_welding_entry_var.get()) * 3
                elif float(weld_length) > 300 and float(weld_length) <= 500:
                    cost_of_weld = float(number_of_welding_entry_var.get()) * 4
                elif float(weld_length) > 500 and int(weld_length) <= 990:
                    cost_of_weld = float(number_of_welding_entry_var.get()) * 5
                else:
                    cost_of_weld = float(number_of_welding_entry_var.get()) * 10

                return cost_of_weld

            def holes_calculation():
                global cost_of_tholes, cost_of_sholes

                cost_of_sholes = 0
                cost_of_tholes = 0
                # thru holes calculation
                if number_of_thru_hole_entry_var.get() != "0":
                    if float(thickness_entry_var.get()) <= 3:
                        cost_of_tholes = float(number_of_thru_hole_entry_var.get()) * 0.5
                    elif float(thickness_entry_var.get()) > 3 and float(thickness_entry_var.get()) <= 6:
                        cost_of_tholes = float(number_of_thru_hole_entry_var.get()) * 1
                    elif float(thickness_entry_var.get()) > 6 and float(thickness_entry_var.get()) <= 12:
                        cost_of_tholes = float(number_of_thru_hole_entry_var.get()) * 2
                    elif float(thickness_entry_var.get()) > 12 and float(thickness_entry_var.get()) <= 16:
                        cost_of_tholes = float(number_of_thru_hole_entry_var.get()) * 3

                # else:
                #     cost_of_tholes = 0

                # special holes calculation
                if number_of_special_hole_entry_var.get() != "0":
                    if float(thickness_entry_var.get()) <= 3:
                        cost_of_sholes = float(number_of_special_hole_entry_var.get()) * 1
                    elif float(thickness_entry_var.get()) > 3 and float(thickness_entry_var.get()) <= 6:
                        cost_of_sholes = float(number_of_special_hole_entry_var.get()) * 2
                    elif float(thickness_entry_var.get()) > 6 and float(thickness_entry_var.get()) <= 12:
                        cost_of_sholes = float(number_of_special_hole_entry_var.get()) * 3
                    elif float(thickness_entry_var.get()) > 12 and float(thickness_entry_var.get()) <= 16:
                        cost_of_sholes = float(number_of_special_hole_entry_var.get()) * 4
                # else:
                #     cost_of_sholes = 0

                return cost_of_tholes, cost_of_sholes

            def treatment_calculation():
                global treatment_cost
                for tcost in treatmentCost:
                    if tcost == treatment_entry_var.get():
                        if treatment_entry_var.get() == "Powder coat":
                            treatment_cost = float(unfold_size) / 93025 * 2 * 2

                        elif treatment_entry_var.get() == "None":
                            treatment_cost = 0

                        else:
                            tfactor = treatmentCost.get(tcost)
                            treatment_cost = float(unfold_size) / 645.1650 * float(tfactor)

                return treatment_cost

            def labour_cost_calculation():
                global labour_cost, cost_mill
                # part difficulty assessment
                if difficulty_entry_var.get() == "Easy":
                    labour_cost = (1 * (10 / 60)) * 20

                elif difficulty_entry_var.get() == "Normal":
                    labour_cost = (1 * (30 / 60)) * 20

                elif difficulty_entry_var.get() == "Hard":
                    labour_cost = (1 * (60 / 60)) * 20

                if switch_var2.get() == "Yes" and difficulty_entry_var.get() == "Easy":
                    cost_mill = 10

                elif switch_var2.get() == "Yes" and difficulty_entry_var.get() == "Normal":
                    cost_mill = 20

                elif switch_var2.get() == "Yes" and difficulty_entry_var.get() == "Hard":
                    cost_mill = 30

                else:
                    cost_mill = 0

                return labour_cost, cost_mill

            def final_calculation_sheet_metal():

                get_unfold_size()
                get_material_cost()
                calculate_raw_material_cost()
                bending_calculation()
                welding_calculation()
                holes_calculation()
                treatment_calculation()
                labour_cost_calculation()


                # final quote calculation (cost of unfold material + bending cost + cost of different types of holes + labour cost + cost of treatment)
                # displaying results on the display frame
                if material_cost_sus304 != 0:
                    ptq_sus304 = ((float(raw_cost_sus304) + float(labour_cost)) * float(markup_entry_var.get())
                                  + float(cost_of_bend) + float(cost_of_weld) + float(cost_mill)
                                  + float(cost_of_tholes) + float(cost_of_sholes) + float(treatment_cost))  # * qty_factor

                    display_price_sus304_var = StringVar(value=f'{ptq_sus304:.2f}')

                    self.display_price_sus304.grid_forget()
                    self.price_sus304.grid_forget()
                    self.display_price_sus304 = CTkLabel(display_frame, text=f'Price to quote for SUS 304-{thickness_entry_var.get()} = $', font=('Arial', 20))
                    self.price_sus304 = CTkEntry(display_frame, textvariable=display_price_sus304_var, font=('Arial', 20), fg_color='green', width=400, border_width=0)
                    self.display_price_sus304.grid(row=0, column=0, sticky='e')
                    self.price_sus304.grid(row=0, column=1)
                else:
                    ptq_sus304 = 0
                    self.display_price_sus304.grid_forget()
                    self.price_sus304.grid_forget()
                    self.display_price_sus304 = CTkLabel(display_frame, text="SUS 304 is not available for this thickness", font=('Arial', 20))
                    self.display_price_sus304.grid(row=0, column=0, sticky='e')

                if material_cost_sus316 != 0:
                    ptq_sus316 = ((float(raw_cost_sus316) + float(labour_cost)) * float(markup_entry_var.get())
                                  + float(cost_of_bend) + float(cost_of_weld) + float(cost_mill)
                                  + float(cost_of_tholes) + float(cost_of_sholes) + float(treatment_cost))  # * qty_factor

                    display_price_sus316_var = StringVar(value=f'{ptq_sus316:.2f}')

                    self.display_price_sus316.grid_forget()
                    self.price_sus316.grid_forget()
                    self.display_price_sus316 = CTkLabel(display_frame, text=f'Price to quote for SUS 316-{thickness_entry_var.get()} = $', font=('Arial', 20))
                    self.price_sus316 = CTkEntry(display_frame, textvariable=display_price_sus316_var, font=('Arial', 20), fg_color='green', width=400, border_width=0)
                    self.display_price_sus316.grid(row=1, column=0, sticky='e')
                    self.price_sus316.grid(row=1, column=1)
                else:
                    ptq_sus316 = 0
                    self.display_price_sus316.grid_forget()
                    self.price_sus316.grid_forget()
                    self.display_price_sus316 = CTkLabel(display_frame, text="SUS 316 is not available for this thickness", font=('Arial', 20))
                    self.display_price_sus316.grid(row=1, column=0, sticky='w')

                if material_cost_alu5052 != 0:
                    ptq_alu5052 = ((float(raw_cost_alu5052) + float(labour_cost)) * float(markup_entry_var.get())
                                  + float(cost_of_bend) + float(cost_of_weld) + float(cost_mill)
                                  + float(cost_of_tholes) + float(cost_of_sholes) + float(treatment_cost))  # * qty_factor

                    display_price_alu5052_var = StringVar(value=f'{ptq_alu5052:.2f}')

                    self.display_price_alu5052.grid_forget()
                    self.price_alu5052.grid_forget()
                    self.display_price_alu5052 = CTkLabel(display_frame, text=f'Price to quote for Alu 5052-{thickness_entry_var.get()} = $', font=('Arial', 20))
                    self.price_alu5052 = CTkEntry(display_frame, textvariable=display_price_alu5052_var, font=('Arial', 20), fg_color='green', width=400, border_width=0)
                    self.display_price_alu5052.grid(row=2, column=0, sticky='e')
                    self.price_alu5052.grid(row=2, column=1)
                else:
                    ptq_alu5052 = 0
                    self.display_price_alu5052.grid_forget()
                    self.price_alu5052.grid_forget()
                    self.display_price_alu5052 = CTkLabel(display_frame, text="Alu 5052 is not available for this thickness", font=('Arial', 20))
                    self.display_price_alu5052.grid(row=2, column=0, sticky='w')

                if material_cost_alu6061 != 0:
                    ptq_alu6061 = ((float(raw_cost_alu6061) + float(labour_cost)) * float(markup_entry_var.get())
                                  + float(cost_of_bend) + float(cost_of_weld) + float(cost_mill)
                                  + float(cost_of_tholes) + float(cost_of_sholes) + float(treatment_cost))  # * qty_factor

                    display_price_alu6061_var = StringVar(value=f'{ptq_alu6061:.2f}')

                    self.display_price_alu6061.grid_forget()
                    self.price_alu6061.grid_forget()
                    self.display_price_alu6061 = CTkLabel(display_frame, text=f'Price to quote for Alu 6061-{thickness_entry_var.get()} = $', font=('Arial', 20))
                    self.price_alu6061 = CTkEntry(display_frame, textvariable=display_price_alu6061_var, font=('Arial', 20), fg_color='green', width=400, border_width=0)
                    self.display_price_alu6061.grid(row=3, column=0, sticky='e')
                    self.price_alu6061.grid(row=3, column=1)
                else:
                    ptq_alu6061 = 0
                    self.display_price_alu6061.grid_forget()
                    self.price_alu6061.grid_forget()
                    self.display_price_alu6061 = CTkLabel(display_frame, text="Alu 6061 is not available for this thickness", font=('Arial', 20))
                    self.display_price_alu6061.grid(row=3, column=0, sticky='w')

                if material_cost_ms != 0:
                    ptq_ms = ((float(raw_cost_ms) + float(labour_cost)) * float(markup_entry_var.get())
                                  + float(cost_of_bend) + float(cost_of_weld) + float(cost_mill)
                                  + float(cost_of_tholes) + float(cost_of_sholes) + float(treatment_cost))  # * qty_factor

                    display_price_ms_var = StringVar(value=f'{ptq_ms:.2f}')

                    self.display_price_ms.grid_forget()
                    self.price_ms.grid_forget()
                    self.display_price_ms = CTkLabel(display_frame, text=f'Price to quote for Mild steel-{thickness_entry_var.get()} = $', font=('Arial', 20))
                    self.price_ms = CTkEntry(display_frame, textvariable=display_price_ms_var, font=('Arial', 20), fg_color='green', width=400, border_width=0)
                    self.display_price_ms.grid(row=4, column=0, sticky='e')
                    self.price_ms.grid(row=4, column=1)
                else:
                    ptq_ms = 0
                    self.display_price_ms.grid_forget()
                    self.price_ms.grid_forget()
                    self.display_price_ms = CTkLabel(display_frame, text="Mild steel is not available for this thickness", font=('Arial', 20))
                    self.display_price_ms.grid(row=4, column=0, sticky='w')

                if material_cost_eg != 0:
                    ptq_eg = ((float(raw_cost_eg) + float(labour_cost)) * float(markup_entry_var.get())
                                  + float(cost_of_bend) + float(cost_of_weld) + float(cost_mill)
                                  + float(cost_of_tholes) + float(cost_of_sholes) + float(treatment_cost))  # * qty_factor

                    display_price_eg_var = StringVar(value=f'{ptq_eg:.2f}')

                    self.display_price_eg.grid_forget()
                    self.price_eg.grid_forget()
                    self.display_price_eg = CTkLabel(display_frame, text=f'Price to quote for EG-{thickness_entry_var.get()} = $', font=('Arial', 20))
                    self.price_eg = CTkEntry(display_frame, textvariable=display_price_eg_var, font=('Arial', 20), fg_color='green', width=400, border_width=0)
                    self.display_price_eg.grid(row=5, column=0, sticky='e')
                    self.price_eg.grid(row=5, column=1)
                else:
                    ptq_eg = 0
                    self.display_price_eg.grid_forget()
                    self.price_eg.grid_forget()
                    self.display_price_eg = CTkLabel(display_frame, text="EG is not available for this thickness", font=('Arial', 20))
                    self.display_price_eg.grid(row=5, column=0, sticky='w')

            def price_register_widgets():

                part_name_var = StringVar()
                price_entry_var = StringVar()
                self.part_name_label = CTkLabel(register_frame, text='Part name/no.:', font=('Arial', 15)).grid(row=0, column=0, sticky='e', pady=5)
                self.part_name_entry = CTkEntry(register_frame, textvariable=part_name_var, font=('Arial', 15), width=250).grid(row=0, column=1, sticky='w')
                self.price_label = CTkLabel(register_frame, text='Price $:', font=('Arial', 15)).grid(row=0, column=2, sticky='e')
                self.price_entry = CTkEntry(register_frame, textvariable=price_entry_var, font=('Arial', 15)).grid(row=0, column=3, sticky='w')
                self.register_price_button = CTkButton(register_frame, text='Register price', font=('Arial', 15)).grid(row=0, column=4, sticky='ew', padx=10)
                self.customer_name_label = CTkLabel(register_frame, text='Customer: ', font=('Arial', 15)).grid(row=1, column=0, sticky='e')
                self.customer_name_ = CTkComboBox(register_frame, font=('Arial', 15), width=250).grid(row=1, column=1, sticky='w', pady=5)
                self.add_new_customer_button = CTkButton(register_frame, text='Add New Customer', font=('Arial', 15)).grid(row=1, column=2, sticky='w', columnspan=2)

            if length_entry_var.get() == "0" or width_entry_var.get() == "0" or length_entry_var.get() == "" or width_entry_var.get() == "":
                messagebox.showwarning(title="Warning!", message="Length or Width entry cannot be 0 or left blank")
                self.focus()
            else:
                final_calculation_sheet_metal()
                price_register_widgets()

        # for layout
        def radiobutton_event_sheet_metal():
            global unit_factor
            if radio_var.get() == 1:
                self.length_sheet_metal.grid_forget()
                self.width_sheet_metal.grid_forget()
                self.length_sheet_metal = CTkLabel(label_frame, text='Length(mm):', font=('Arial', 24))
                self.length_sheet_metal.grid(row=0, column=0, sticky='e', pady=10)
                self.width_sheet_metal = CTkLabel(label_frame, text='Width(mm):', font=('Arial', 24))
                self.width_sheet_metal.grid(row=1, column=0, sticky='e', pady=10)
                unit_factor = 1

            else:
                self.length_sheet_metal.grid_forget()
                self.width_sheet_metal.grid_forget()
                self.length_sheet_metal = CTkLabel(label_frame, text='Length(inches):', font=('Arial', 24))
                self.length_sheet_metal.grid(row=0, column=0, sticky='e', pady=10)
                self.width_sheet_metal = CTkLabel(label_frame, text='Width(inches):', font=('Arial', 24))
                self.width_sheet_metal.grid(row=1, column=0, sticky='e', pady=10)
                unit_factor = 25.4

        def switch_event():

            if switch_var.get() == "off":
                switch_var2.set(value="No")


            else:
                switch_var2.set(value="Yes")

        # add frames onto sheet metal tabs for layout
        top_frame = CTkFrame(self.tab("Sheet Metal calculator"))

        # Coloured Background
        label_frame = CTkFrame(top_frame, fg_color='pink')
        input_frame = CTkFrame(top_frame, fg_color='orange')
        unit_frame = CTkFrame(top_frame, fg_color='yellow')
        display_frame = CTkFrame(self.tab("Sheet Metal calculator"), fg_color='green')
        register_frame = CTkFrame(self.tab("Sheet Metal calculator"), fg_color='light blue')

        # Grey Background
        # label_frame = CTkFrame(top_frame)
        # input_frame = CTkFrame(top_frame)
        # unit_frame = CTkFrame(top_frame)
        # display_frame = CTkFrame(self.tab("Sheet Metal calculator"))
        # register_frame = CTkFrame(self.tab("Sheet Metal calculator"))
        register_frame.columnconfigure((0,1,2,3,4), weight=1)
        register_frame.rowconfigure((0,1), weight=1)



        # widgets for sheet metal calculator
        self.length_sheet_metal = CTkLabel(label_frame, text='Length(mm):', font=('Arial', 24))
        self.length_sheet_metal.grid(row=0, column=0, sticky='e', pady=10)
        self.width_sheet_metal = CTkLabel(label_frame, text='Width(mm):', font=('Arial', 24))
        self.width_sheet_metal.grid(row=1, column=0, sticky='e', pady=10)
        self.material_thickness = CTkLabel(label_frame, text='Thickness:', font=('Arial', 24)).grid(row=2, column=0, sticky='e', pady=13)
        self.number_of_bend = CTkLabel(label_frame, text='Number of bends:', font=('Arial', 24)).grid(row=3, column=0, sticky='e', pady=13)
        self.number_of_thru_holes = CTkLabel(label_frame, text='Number of thru holes:', font=('Arial', 24)).grid(row=4, column=0, sticky='e', pady=13)
        self.number_of_special_holes = CTkLabel(label_frame, text='Number of special holes:', font=('Arial', 24)).grid(row=5, column=0, sticky='e', pady=13)
        self.number_of_weldings = CTkLabel(label_frame, text='Number of welds:', font=('Arial', 24)).grid(row=6, column=0, sticky='e', pady=13)
        self.machining = CTkLabel(label_frame, text='Machining:', font=('Arial', 24)).grid(row=7, column=0, sticky='e', pady=13)
        self.part_difficulty = CTkLabel(label_frame, text='Part difficulty:', font=('Arial', 24)).grid(row=8, column=0, sticky='e', pady=13, padx=(140, 0))
        self.treatment = CTkLabel(label_frame, text='Treatment:', font=('Arial', 24)).grid(row=9, column=0, sticky='e', pady=13)
        self.markup = CTkLabel(label_frame, text='Mark-up:', font=('Arial', 24)).grid(row=10, column=0, sticky='e', pady=13)

        # defining tkinter variables for calculation purpose
        length_entry_var = StringVar(value=0)
        width_entry_var = StringVar(value=0)
        thickness_entry_var = DoubleVar()
        number_of_bend_entry_var = StringVar(value=0)
        number_of_thru_hole_entry_var = StringVar(value=0)
        number_of_special_hole_entry_var = StringVar(value=0)
        number_of_welding_entry_var = StringVar(value=0)
        switch_var = StringVar(value="off")
        switch_var2 = StringVar(value="No")
        treatment_entry_var = StringVar()
        difficulty_entry_var = StringVar()
        markup_entry_var = StringVar(value='3')

        length_entry = CTkEntry(input_frame, textvariable=length_entry_var, font=('Arial', 24), width=260)
        length_entry.bind("<Return>", lambda event, entry=length_entry: do_math(entry, event))
        length_entry.grid(row=0, column=1, sticky='w', pady=10)

        width_entry = CTkEntry(input_frame, textvariable=width_entry_var, font=('Arial', 24), width=260)
        width_entry.bind("<Return>", lambda event, entry=width_entry: do_math(entry, event))
        width_entry.grid(row=1, column=1, sticky='w', pady=6)

        thickness_entry = CTkComboBox(input_frame, values=thickness, state='readonly', variable=thickness_entry_var, font=('Arial', 24), width=260)
        thickness_entry.set(thickness[8])
        thickness_entry.grid(row=2, column=1, sticky='w', pady=8)

        number_of_bend_entry = CTkEntry(input_frame, textvariable=number_of_bend_entry_var, font=('Arial', 24), width=260)
        number_of_bend_entry.bind("<Return>", lambda event, entry=number_of_bend_entry_var: do_math(entry, event))
        number_of_bend_entry.grid(row=3, column=1, sticky='w', pady=12)

        number_of_thru_holes_entry = CTkEntry(input_frame, textvariable=number_of_thru_hole_entry_var, font=('Arial', 24), width=260)
        number_of_thru_holes_entry.bind("<Return>", lambda event, entry=number_of_thru_hole_entry_var: do_math(entry, event))
        number_of_thru_holes_entry.grid(row=4, column=1, sticky='w', pady=10)

        number_of_special_holes_entry = CTkEntry(input_frame, textvariable=number_of_special_hole_entry_var, font=('Arial', 24), width=260)
        number_of_special_holes_entry.bind("<Return>", lambda event, entry=number_of_special_hole_entry_var: do_math(entry, event))
        number_of_special_holes_entry.grid(row=5, column=1, sticky='w', pady=10)

        number_of_weldings_entry = CTkEntry(input_frame, textvariable=number_of_welding_entry_var, font=('Arial', 24), width=260)
        number_of_weldings_entry.bind("<Return>", lambda event, entry=number_of_welding_entry_var: do_math(entry, event))
        number_of_weldings_entry.grid(row=6, column=1, sticky='w', pady=10)

        machining_response_entry = CTkSwitch(input_frame, text="Yes", command=switch_event, textvariable=switch_var2, variable=switch_var, onvalue="on", offvalue="off").grid(row=7, column=1, sticky='w', pady=12)


        difficulty_entry = CTkComboBox(input_frame, values=difficulty, state='readonly', font=('Arial', 24), variable=difficulty_entry_var, width=260)
        difficulty_entry.set(difficulty[0])
        difficulty_entry.grid(row=8, column=1, sticky='w', pady=15)

        treatment_entry = CTkComboBox(input_frame, values=list(treatmentCost.keys()), state='readonly', font=('Arial', 24), variable=treatment_entry_var, width=260)
        treatment_entry.set(list(treatmentCost.keys())[0])
        treatment_entry.grid(row=9, column=1, sticky='w', pady=10)

        mark_up_entry = CTkEntry(input_frame, textvariable=markup_entry_var, font=('Arial', 24), width=260).grid(row=10, column=1, sticky='w', pady=10)
        quote = CTkButton(input_frame, text='Quote', command=quote_sheet_metal, font=('Arial', 24), width=260).grid(row=11, column=1, sticky='w', pady=10)

        radio_var = IntVar(value=1)
        unit_label = CTkLabel(unit_frame, text='Unit selection').pack(expand=True, fill='both')
        unit_selection = CTkRadioButton(unit_frame, text='mm', command=radiobutton_event_sheet_metal, variable=radio_var, value=1).pack(expand=True, fill='both', pady=5)
        unit_selection = CTkRadioButton(unit_frame, text='inches', command=radiobutton_event_sheet_metal, variable=radio_var, value=2).pack(expand=True, fill='both', pady=5)


        self.display_price_sus304 = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.display_price_sus304.grid(row=0, column=0, sticky='w')
        self.price_sus304  = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.price_sus304.grid(row=0, column=1, sticky='w')

        self.display_price_sus316 = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.display_price_sus316.grid(row=1, column=0, sticky='w')
        self.price_sus316 = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.price_sus316.grid(row=1, column=1, sticky='w')


        self.display_price_alu5052 = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.display_price_alu5052.grid(row=2, column=0, sticky='w')
        self.price_alu5052 = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.price_alu5052.grid(row=2, column=1, sticky='w')


        self.display_price_alu6061 = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.display_price_alu6061.grid(row=3, column=0, sticky='w')
        self.price_alu6061 = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.price_alu6061.grid(row=3, column=1, sticky='w')


        self.display_price_ms = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.display_price_ms.grid(row=4, column=0, sticky='w')
        self.price_ms = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.price_ms.grid(row=4, column=1, sticky='w')


        self.display_price_eg = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.display_price_eg.grid(row=5, column=0, sticky='w')
        self.price_eg = CTkLabel(display_frame, text='', font=('Arial', 20))
        self.price_eg.grid(row=5, column=1, sticky='w')


        # packing the frames
        top_frame.pack(expand=True, fill='both')
        label_frame.pack(side='left', expand=True, fill='both')
        input_frame.pack(side='left', expand=True, fill='both')
        unit_frame.place(relx=1, rely=0, anchor='ne')
        display_frame.pack(expand=True, fill='both')
        register_frame.pack(fill='both', pady=5)

        self.pack(expand=True, fill='both')

    def AddMachiningTab(self):
        self.add("Machining calculator")


        # mini calculator function for Machining tab
        def do_math(e, event):
            eqn = e.get()
            cond = str(e).split('.!')

            if not re.search(r'[a-zA-Z]', eqn):
                ans = str(eval(eqn))
                # print(cond) # To check if I am able to use this as a condition

                if cond[-1] == "ctkentry":
                    length_entry.delete(0, END)
                    length_entry.insert(0, ans)

                elif cond[-1] == "ctkentry2":
                    width_entry.delete(0, END)
                    width_entry.insert(0, ans)

                elif cond[-1] == "ctkentry3":
                    height_entry.delete(0, END)
                    height_entry.insert(0, ans)


            else:
                messagebox.showwarning(title="Warning!", message="This entry box accepts numbers only.")
                if cond[-1] == "ctkentry":
                    length_entry.delete(0, END)
                    length_entry.focus()

                elif cond[-1] == "ctkentry2":
                    width_entry.delete(0, END)
                    width_entry.focus()

                elif cond[-1] == "ctkentry3":
                    height_entry.delete(0, END)
                    height_entry.focus()


        # actual calculator function
        def quote_machining():

            def get_volume():
                global volume, cost_of_raw_material

                volume = 0

                volume = (float(length_entry_var.get()) * unit_factor) * (float(width_entry_var.get()) * unit_factor) * (float(height_entry_var.get()) * unit_factor)
                print(f'volume = {volume}')

                # getting material cost per 1mm square
                if material_entry_var.get() == "SUS":
                    cost_of_raw_material = volume * materialList_machining.get("SUS")
                    print(f'cost of material = {cost_of_raw_material}')

                elif material_entry_var.get() == "ALU":
                    cost_of_raw_material = volume * materialList_machining.get("ALU")
                    print(f'cost of material = {cost_of_raw_material}')

                elif material_entry_var.get() == "STEEL":
                    cost_of_raw_material = volume * materialList_machining.get("STEEL")
                    print(f'cost of material = {cost_of_raw_material}')

                elif material_entry_var.get() == "DERLIN":
                    cost_of_raw_material = volume * materialList_machining.get("DERLIN")
                    print(f'cost of material = {cost_of_raw_material}')


                return volume, cost_of_raw_material


            def treatment_calculation():
                global treatment_cost

                unfold_size = (float(length_entry_var.get()) * unit_factor) * (float(width_entry_var.get()) * unit_factor)
                print(f'unfold size = {unfold_size}')
                for tcost in treatmentCost:
                    if tcost == treatment_entry_var.get():
                        if treatment_entry_var.get() == "Powder coat":
                            treatment_cost = unfold_size / 93025 * 2 * 2

                        elif treatment_entry_var.get() == "None":
                            treatment_cost = 0

                        else:
                            tfactor = treatmentCost.get(tcost)
                            treatment_cost = unfold_size / 645.1650 * float(tfactor)
                print(f'treatment cost = {treatment_cost}')
                return treatment_cost

            def labour_cost_calculation():
                global total_labour_cost
                # programming time x programming cost per hour
                programming_cost = float(programming_time_entry_var.get()) * (45/60)
                print(f'programming cost = ${programming_cost}')

                # Simulated runtime x labour cost per hour
                labour_cost = float(simulated_runtime_entry_var.get()) * (16/60)
                print(f'labour cost = ${labour_cost}')

                total_labour_cost = programming_cost + labour_cost

                return total_labour_cost

            def final_calculation_machining():

                get_volume()
                treatment_calculation()
                labour_cost_calculation()

                # final quote calculation for machining (cost of raw material x markup + treatment cost + total labour cost)
                ptq_machining = (cost_of_raw_material * float(markup_entry_var.get())) + treatment_cost + total_labour_cost

                price_to_quote_machining_var = StringVar(value=f'{ptq_machining:.2f}')

                self.price_to_quote_machining_label = CTkLabel(display_frame, text='Price to quote: $', font=('Arial', 24))
                self.price_to_quote_machining_label.grid(row=0, column=0, sticky='e')

                self.price_to_quote_machining = CTkEntry(display_frame, textvariable=price_to_quote_machining_var, font=('Arial', 24), fg_color='green')
                self.price_to_quote_machining.grid(row=0, column=1, sticky='w')

            def price_register_widgets():

                part_name_var = StringVar()
                price_entry_var = StringVar()

                self.part_name_label = CTkLabel(register_frame, text='Part name/no.:', font=('Arial', 15)).grid(row=0, column=0, sticky='e')
                self.part_name_entry = CTkEntry(register_frame, textvariable=part_name_var, font=('Arial', 15), width=250).grid(row=0, column=1, sticky='w')
                self.price_label = CTkLabel(register_frame, text='Price $:', font=('Arial', 15)).grid(row=0, column=2, sticky='e')
                self.price_entry = CTkEntry(register_frame, textvariable=price_entry_var, font=('Arial', 15)).grid(row=0, column=3, sticky='w')
                self.register_price_button = CTkButton(register_frame, text='Register price', font=('Arial', 15)).grid(row=0, column=4, sticky='w')
                self.customer_name_label = CTkLabel(register_frame, text='Customer: ', font=('Arial', 15)).grid(row=1, column=0, sticky='e', pady=5)
                self.customer_name_ = CTkComboBox(register_frame, font=('Arial', 15), width=250).grid(row=1, column=1, columnspan=2, sticky='w')
                self.add_new_customer_button = CTkButton(register_frame, text='Add New Customer', font=('Arial', 15)).grid(row=1, column=2, sticky='w', columnspan=2)

            if length_entry_var.get() == "0" or width_entry_var.get() == "0" or height_entry_var.get() == "0" or length_entry_var.get() == "" or width_entry_var.get() == "" or height_entry_var.get() == "":
                messagebox.showwarning(title="Warning!", message="Length, Width or Height entry cannot be 0 or left blank")
                self.focus()
            else:
                final_calculation_machining()
                price_register_widgets()
        # for layout
        def radiobutton_event_machining():
            global unit_factor
            if radio_var.get() == 1:
                self.length_machining.grid_forget()
                self.width_machining.grid_forget()
                self.height_machining.grid_forget()
                self.length_machining = CTkLabel(label_frame, text='Length(mm):', font=('Arial', 24))
                self.length_machining.grid(row=0, column=0, sticky='e', pady=10)
                self.width_machining = CTkLabel(label_frame, text='Width(mm):', font=('Arial', 24))
                self.width_machining.grid(row=1, column=0, sticky='e', pady=10)
                self.height_machining = CTkLabel(label_frame, text='Height(mm):', font=('Arial', 24))
                self.height_machining.grid(row=2, column=0, sticky='e', pady=10)
                unit_factor = 1

            else:
                self.length_machining.grid_forget()
                self.width_machining.grid_forget()
                self.height_machining.grid_forget()
                self.length_machining = CTkLabel(label_frame, text='Length(inches):', font=('Arial', 24))
                self.length_machining.grid(row=0, column=0, sticky='e', pady=10)
                self.width_machining = CTkLabel(label_frame, text='Width(inches):', font=('Arial', 24))
                self.width_machining.grid(row=1, column=0, sticky='e', pady=10)
                self.height_machining = CTkLabel(label_frame, text='Height(inches):', font=('Arial', 24))
                self.height_machining.grid(row=2, column=0, sticky='e', pady=10)
                unit_factor = 25.4

        # add frames onto machining tabs for layout
        top_frame = CTkFrame(self.tab("Machining calculator"))
        label_frame = CTkFrame(top_frame, fg_color='pink')
        input_frame = CTkFrame(top_frame, fg_color='orange')
        unit_frame = CTkFrame(top_frame, fg_color='yellow')
        display_frame = CTkFrame(self.tab("Machining calculator"), fg_color='green')
        register_frame = CTkFrame(self.tab("Machining calculator"), fg_color='light blue')
        register_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        register_frame.rowconfigure((0, 1), weight=1)

        # widgets for machining calculator
        self.length_machining = CTkLabel(label_frame, text='Length(mm):', font=('Arial', 24))
        self.length_machining.grid(row=0, column=0, sticky='e', pady=10)
        self.width_machining = CTkLabel(label_frame, text='Width(mm):', font=('Arial', 24))
        self.width_machining.grid(row=1, column=0, sticky='e', pady=10)
        self.height_machining = CTkLabel(label_frame, text='Height(mm):', font=('Arial', 24))
        self.height_machining.grid(row=2, column=0, sticky='e', pady=10)

        self.material = CTkLabel(label_frame, text='Material:', font=('Arial', 24)).grid(row=3, column=0, sticky='e', pady=13, padx=(140, 0))
        self.programming_time = CTkLabel(label_frame, text='Programming time(mins):', font=('Arial', 24)).grid(row=4, column=0, sticky='e', pady=13)
        self.simulated_runtime = CTkLabel(label_frame, text='Simulated runtime(mins):', font=('Arial', 24)).grid(row=5, column=0, sticky='e', pady=13)
        self.treatment = CTkLabel(label_frame, text='Treatment:', font=('Arial', 24)).grid(row=6, column=0, sticky='e', pady=13)
        self.markup = CTkLabel(label_frame, text='Mark-up:', font=('Arial', 24)).grid(row=7, column=0, sticky='e', pady=13)

        # defining tkinter variables for calculation purpose
        length_entry_var = StringVar(value=0)
        width_entry_var = StringVar(value=0)
        height_entry_var = StringVar(value=0)
        material_entry_var = StringVar()
        programming_time_entry_var = StringVar(value=30)
        simulated_runtime_entry_var = StringVar(value=60)
        treatment_entry_var = StringVar()

        markup_entry_var = StringVar(value='1.1')

        length_entry = CTkEntry(input_frame, textvariable=length_entry_var, font=('Arial', 24), width=260)
        length_entry.bind("<Return>", lambda event, entry=length_entry: do_math(entry, event))
        length_entry.grid(row=0, column=1, sticky='w', pady=10)

        width_entry = CTkEntry(input_frame, textvariable=width_entry_var, font=('Arial', 24), width=260)
        width_entry.bind("<Return>", lambda event, entry=width_entry: do_math(entry, event))
        width_entry.grid(row=1, column=1, sticky='w', pady=6)

        height_entry = CTkEntry(input_frame, textvariable=height_entry_var, font=('Arial', 24), width=260)
        height_entry.bind("<Return>", lambda event, entry=height_entry: do_math(entry, event))
        height_entry.grid(row=2, column=1, sticky='w', pady=6)


        self.material_entry = CTkComboBox(input_frame, values=materialList_machining.keys(), state='readonly', font=('Arial', 24), variable=material_entry_var, width=260)
        self.material_entry.set(list(materialList_machining.keys())[1])
        self.material_entry.grid(row=3, column=1, sticky='w', pady=10)

        self.programming_time_entry = CTkEntry(input_frame, textvariable=programming_time_entry_var, font=('Arial', 24), width=260).grid(row=4, column=1, sticky='w', pady=11)
        self.simulated_runtime_entry = CTkEntry(input_frame, textvariable=simulated_runtime_entry_var, font=('Arial', 24), width=260).grid(row=5, column=1, sticky='w', pady=10)

        self.treatment_entry = CTkComboBox(input_frame, values=list(treatmentCost.keys()), state='readonly', font=('Arial', 24), variable=treatment_entry_var, width=260)
        self.treatment_entry.set(list(treatmentCost.keys())[0])
        self.treatment_entry.grid(row=6, column=1, sticky='w', pady=10)

        self.mark_up_entry = CTkEntry(input_frame, textvariable=markup_entry_var, font=('Arial', 24), width=260).grid(row=7, column=1, sticky='w', pady=10)
        self.quote = CTkButton(input_frame, text='Quote', command=quote_machining, font=('Arial', 24), width=260).grid(row=8, column=1, sticky='w', pady=10)

        radio_var = IntVar(value=1)
        self.unit_label = CTkLabel(unit_frame, text='Unit selection').pack(expand=True, fill='both')
        self.unit_selection = CTkRadioButton(unit_frame, text='mm', command=radiobutton_event_machining, variable=radio_var, value=1).pack(expand=True, fill='both', pady=5)
        self.unit_selection = CTkRadioButton(unit_frame, text='inches', command=radiobutton_event_machining, variable=radio_var, value=2).pack(expand=True, fill='both', pady=5)



        # packing the frames
        top_frame.pack(expand=True, fill='both')
        label_frame.pack(side='left', expand=True, fill='both')
        input_frame.pack(side='left', expand=True, fill='both')
        unit_frame.place(relx=1, rely=0, anchor='ne')
        display_frame.pack(expand=True, fill='both')
        register_frame.pack(fill='x', pady=5)

        self.pack(expand=True, fill='both')

    def AddStructureTab(self):
        self.add("Structure calculator")
        unit_factor = 1

        # mini calculator function for Structure tab
        def do_math(e, event):
            eqn = e.get()
            cond = str(e).split('.!')

            if not re.search(r'[a-zA-Z]', eqn):
                ans = str(eval(eqn))
                print(cond) # To check if I am able to use this as a condition

                if cond[-1] == "ctkentry":
                    length_entry.delete(0, END)
                    length_entry.insert(0, ans)

                elif cond[-1] == "ctkentry2":
                    width_entry.delete(0, END)
                    width_entry.insert(0, ans)

                elif cond[-1] == "ctkentry3":
                    height_entry.delete(0, END)
                    height_entry.insert(0, ans)


            else:
                messagebox.showwarning(title="Warning!", message="This entry box accepts numbers only.")
                if cond[-1] == "ctkentry":
                    length_entry.delete(0, END)
                    length_entry.focus()

                elif cond[-1] == "ctkentry2":
                    width_entry.delete(0, END)
                    width_entry.focus()

                elif cond[-1] == "ctkentry3":
                    height_entry.delete(0, END)
                    height_entry.focus()


        # actual calculator function
        def quote_structure():

            def get_volume():
                global volume

                volume = 0

                volume = (float(length_entry_var.get()) * unit_factor) * (float(width_entry_var.get()) * unit_factor) * (float(height_entry_var.get()) * unit_factor)

                return volume

            def treatment_calculation():
                global treatment_cost
                for tcost in treatmentCost:
                    if tcost == treatment_entry_var.get():
                        if treatment_entry_var.get() == "Powder coat":
                            treatment_cost = float(unfold_size) / 93025 * 2 * 2

                        elif treatment_entry_var.get() == "None":
                            treatment_cost = 0

                        else:
                            tfactor = treatmentCost.get(tcost)
                            treatment_cost = float(unfold_size) / 645.1650 * float(tfactor)

                return treatment_cost

            def labour_cost_calculation():
                global labour_cost
                # part difficulty assessment
                if difficulty_entry_var.get() == "Easy":
                    labour_cost = (1 * (10 / 60)) * 20

                elif difficulty_entry_var.get() == "Normal":
                    labour_cost = (1 * (30 / 60)) * 20

                elif difficulty_entry_var.get() == "Hard":
                    labour_cost = (1 * (60 / 60)) * 20

                return labour_cost

            def final_calculation_structure():

                get_volume()
                treatment_calculation()
                labour_cost_calculation()

                # final quote calculation (cost of unfold material + bending cost + cost of different types of holes + labour cost + cost of treatment)

            def price_register_widgets():

                part_name_var = StringVar()
                price_entry_var = StringVar()

                self.part_name_label = CTkLabel(register_frame, text='Part name/no.:', font=('Arial', 15)).grid(row=0, column=0, sticky='e')
                self.part_name_entry = CTkEntry(register_frame, textvariable=part_name_var, font=('Arial', 15), width=250).grid(row=0, column=1, sticky='w')
                self.price_label = CTkLabel(register_frame, text='Price $:', font=('Arial', 15)).grid(row=0, column=2, sticky='e')
                self.price_entry = CTkEntry(register_frame, textvariable=price_entry_var, font=('Arial', 15)).grid(row=0, column=3, sticky='w')
                self.register_price_button = CTkButton(register_frame, text='Register price', font=('Arial', 15)).grid(row=0, column=4, sticky='w')
                self.customer_name_label = CTkLabel(register_frame, text='Customer: ', font=('Arial', 15)).grid(row=1, column=0, sticky='e', pady=10)
                self.customer_name_ = CTkComboBox(register_frame, font=('Arial', 15), width=250).grid(row=1, column=1, columnspan=2, sticky='w')
                self.add_new_customer_button = CTkButton(register_frame, text='Add New Customer', font=('Arial', 15)).grid(row=1, column=2, sticky='w', columnspan=2)

            if length_entry_var.get() == "0" or width_entry_var.get() == "0" or height_entry_var.get() == "0" or length_entry_var.get() == "" or width_entry_var.get() == "" or height_entry_var.get() == "":
                messagebox.showwarning(title="Warning!", message="Length, Width or Height entry cannot be 0 or left blank")
                self.focus()
            else:
                final_calculation_structure()
                price_register_widgets()

        # for layout
        def radiobutton_event_structure():
            if radio_var.get() == 1:
                self.length_structure.grid_forget()
                self.width_structure.grid_forget()
                self.height_structure.grid_forget()
                self.length_structure = CTkLabel(label_frame, text='Length(mm):', font=('Arial', 24))
                self.length_structure.grid(row=0, column=0, sticky='e', pady=10)
                self.width_structure = CTkLabel(label_frame, text='Width(mm):', font=('Arial', 24))
                self.width_structure.grid(row=1, column=0, sticky='e', pady=10)
                self.height_structure = CTkLabel(label_frame, text='Height(mm):', font=('Arial', 24))
                self.height_structure.grid(row=2, column=0, sticky='e', pady=10)
                unit_factor = 1

            else:
                self.length_structure.grid_forget()
                self.width_structure.grid_forget()
                self.height_structure.grid_forget()
                self.length_structure = CTkLabel(label_frame, text='Length(inches):', font=('Arial', 24))
                self.length_structure.grid(row=0, column=0, sticky='e', pady=10)
                self.width_structure = CTkLabel(label_frame, text='Width(inches):', font=('Arial', 24))
                self.width_structure.grid(row=1, column=0, sticky='e', pady=10)
                self.height_structure = CTkLabel(label_frame, text='Height(inches):', font=('Arial', 24))
                self.height_structure.grid(row=2, column=0, sticky='e', pady=10)
                unit_factor = 25.4

        def material_type_seclection(selected):

            if selected == "Square tube":
                self.material_size_entry.configure(values=sizesTube)
                self.material_size_entry.set(sizesTube[3])

            elif selected == "Pipe":
                self.material_size_entry.configure(values=sizePipe)
                self.material_size_entry.set(sizePipe[2])


        # add frames onto structure tabs for layout
        top_frame = CTkFrame(self.tab("Structure calculator"))
        label_frame = CTkFrame(top_frame, fg_color='pink')
        input_frame = CTkFrame(top_frame, fg_color='orange')
        unit_frame = CTkFrame(top_frame, fg_color='yellow')
        display_frame = CTkFrame(self.tab("Structure calculator"), fg_color='green')
        register_frame = CTkFrame(self.tab("Structure calculator"), fg_color='light blue')
        register_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        register_frame.rowconfigure((0, 1), weight=1)


        # widgets for structure calculator
        self.length_structure = CTkLabel(label_frame, text='Length(mm):', font=('Arial', 24))
        self.length_structure.grid(row=0, column=0, sticky='e', pady=10)
        self.width_structure = CTkLabel(label_frame, text='Width(mm):', font=('Arial', 24))
        self.width_structure.grid(row=1, column=0, sticky='e', pady=10)
        self.height_structure = CTkLabel(label_frame, text='Height(mm):', font=('Arial', 24))
        self.height_structure.grid(row=2, column=0, sticky='e', pady=10)
        self.material = CTkLabel(label_frame, text='Material:', font=('Arial', 24)).grid(row=3, column=0, sticky='e', pady=13)
        self.material_type = CTkLabel(label_frame, text='Material type:', font=('Arial', 24)).grid(row=4, column=0, sticky='e', pady=13)
        self.material_size = CTkLabel(label_frame, text='Material size:', font=('Arial', 24)).grid(row=5, column=0, sticky='e', pady=13)
        self.difficulty = CTkLabel(label_frame, text='Part difficulty:', font=('Arial', 24)).grid(row=6, column=0, sticky='e', pady=13, padx=(140, 0))
        self.treatment = CTkLabel(label_frame, text='Treatment:', font=('Arial', 24)).grid(row=7, column=0, sticky='e', pady=13)
        self.markup = CTkLabel(label_frame, text='Mark-up:', font=('Arial', 24)).grid(row=8, column=0, sticky='e', pady=13)

        # defining tkinter variables for calculation purpose
        length_entry_var = StringVar(value=0)
        width_entry_var = StringVar(value=0)
        height_entry_var = StringVar(value=0)
        material_entry_var = StringVar()
        material_type_entry_var = StringVar()
        material_size_entry_var = StringVar()
        difficulty_entry_var = StringVar()
        treatment_entry_var = StringVar()
        markup_entry_var = StringVar(value='3')

        length_entry = CTkEntry(input_frame, textvariable=length_entry_var, font=('Arial', 24), width=260)
        length_entry.bind("<Return>", lambda event, entry=length_entry: do_math(entry, event))
        length_entry.grid(row=0, column=1, sticky='w', pady=10)

        width_entry = CTkEntry(input_frame, textvariable=width_entry_var, font=('Arial', 24), width=260)
        width_entry.bind("<Return>", lambda event, entry=width_entry: do_math(entry, event))
        width_entry.grid(row=1, column=1, sticky='w', pady=6)

        height_entry = CTkEntry(input_frame, textvariable=height_entry_var, font=('Arial', 24), width=260)
        height_entry.bind("<Return>", lambda event, entry=height_entry: do_math(entry, event))
        height_entry.grid(row=2, column=1, sticky='w', pady=6)

        self.material_entry = CTkComboBox(input_frame, values=materialList, state='readonly', font=('Arial', 24), variable=material_entry_var, width=260)
        self.material_entry.set(materialList[0])
        self.material_entry.grid(row=3, column=1, sticky='w', pady=10)

        self.material_type_entry = CTkComboBox(input_frame, values=materialType, state='readonly', font=('Arial', 24), variable=material_type_entry_var, command=material_type_seclection, width=260)
        self.material_type_entry.set(materialType[0])
        self.material_type_entry.grid(row=4, column=1, sticky='w', pady=10)

        self.material_size_entry = CTkComboBox(input_frame, state='readonly', values=sizesTube, variable=material_size_entry_var, font=('Arial', 24), width=260)
        self.material_size_entry.set(sizesTube[3])
        self.material_size_entry.grid(row=5, column=1, sticky='w', pady=10)

        self.difficulty_entry = CTkComboBox(input_frame, values=difficulty, state='readonly', font=('Arial', 24), variable=difficulty_entry_var, width=260)
        self.difficulty_entry.set(difficulty[0])
        self.difficulty_entry.grid(row=6, column=1, sticky='w', pady=12)

        self.treatment_entry = CTkComboBox(input_frame, values=list(treatmentCost.keys()), state='readonly', font=('Arial', 24), variable=treatment_entry_var, width=260)
        self.treatment_entry.set(list(treatmentCost.keys())[0])
        self.treatment_entry.grid(row=7, column=1, sticky='w', pady=12)

        self.mark_up_entry = CTkEntry(input_frame, textvariable=markup_entry_var, font=('Arial', 24), width=260).grid(row=8, column=1, sticky='w', pady=10)
        self.quote = CTkButton(input_frame, text='Quote', command=quote_structure, font=('Arial', 24), width=260).grid(row=9, column=1, sticky='w', pady=10)

        radio_var = IntVar(value=1)
        self.unit_label = CTkLabel(unit_frame, text='Unit selection').pack(expand=True, fill='both')
        self.unit_selection = CTkRadioButton(unit_frame, text='mm', command=radiobutton_event_structure, variable=radio_var, value=1).pack(expand=True, fill='both', pady=5)
        self.unit_selection = CTkRadioButton(unit_frame, text='inches', command=radiobutton_event_structure, variable=radio_var, value=2).pack(expand=True, fill='both', pady=5)

        # packing the frames
        top_frame.pack(expand=True, fill='both')
        label_frame.pack(side='left', expand=True, fill='both')
        input_frame.pack(side='left', expand=True, fill='both')
        unit_frame.place(relx=1, rely=0, anchor='ne')
        display_frame.pack(expand=True, fill='both')
        register_frame.pack(fill='x', pady=5)

        self.pack(expand=True, fill='both')


class SalesOrderCreate(CTkToplevel):
    def __init__(self, parent, title, size):
        super().__init__(parent)

        self.title(title)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (size[0] / 2)
        y = (screen_height / 2) - (size[1] / 2)

        self.geometry(f'{size[0]}x{size[1]}+{int(x)}+{int(y)}')

        self.focus()


class WorkshopScheduling(CTkToplevel):
    def __init__(self, parent, title, size):
        super().__init__(parent)

        self.title(title)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (size[0] / 2)
        y = (screen_height / 2) - (size[1] / 2)

        self.geometry(f'{size[0]}x{size[1]}+{int(x)}+{int(y)}')
        self.focus()

class Logistic(CTkToplevel):
    def __init__(self, parent, title, size):
        super().__init__(parent)

        self.title(title)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (size[0] / 2)
        y = (screen_height / 2) - (size[1] / 2)

        self.geometry(f'{size[0]}x{size[1]}+{int(x)}+{int(y)}')
        self.focus()

class SSHDatabase(CTkToplevel):
    def __init__(self, parent, title, size):
        super().__init__(parent)

        global customer_list, customer_list_combobox

        # everytime I open this window I want to update customer_list if present, if not present can leave it as blank

        self.title(title)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (size[0] / 2)
        y = (screen_height / 2) - (size[1] / 2)

        self.geometry(f'{size[0]}x{size[1]}+{int(x)}+{int(y)}')
        self.focus()

        # menu
        menu = tkinter.Menu(self)

        # sub menu
        file_menu = tkinter.Menu(menu, tearoff=False)
        file_menu.add_command(label='Import Customer list', command=self.ImportCustomerList)
        file_menu.add_command(label='Import Sales order list', command=self.ImportSalesorderList)
        file_menu.add_command(label='Import Part list', command=self.ImportPartList)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=lambda: self.destroy())
        menu.add_cascade(label='File', menu=file_menu)

        self.configure(menu=menu)

        # Create a database or connect to one that exists everytime database button pressed
        sshdb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="5c4r3cr0w",
            database="ssh",
        )

        my_cursor = sshdb.cursor()

        my_cursor.execute("CREATE TABLE IF NOT EXISTS customer ("
                          " customer VARCHAR(180),"
                          " address VARCHAR(255) NULL,"
                          " phone VARCHAR(50) NULL,"
                          " email VARCHAR(150) NULL,"
                          " currency VARCHAR(20),"
                          " PRIMARY KEY (customer))"
                          "")

        my_cursor.execute("CREATE TABLE IF NOT EXISTS parts ("
                          " part_name VARCHAR(50),"
                          " material_name VARCHAR(30),"
                          " thickness DECIMAL(5, 2),"
                          " customer VARCHAR(180),"
                          " date_created DATE,"
                          " unfold_x VARCHAR(30),"
                          " unfold_y VARCHAR(30),"
                          " order_no VARCHAR(20),"
                          " machining VARCHAR(20),"
                          " treatment VARCHAR(30),"
                          " price DECIMAL(10, 2),"
                          " comment VARCHAR(50) )"
                          "")

        my_cursor.execute("CREATE TABLE IF NOT EXISTS sales ("
                          " order_no VARCHAR(20),"
                          " customer VARCHAR(180),"
                          " start_date VARCHAR(50),"
                          " due_date VARCHAR(50),"
                          " status VARCHAR(30),"
                          " PRIMARY KEY (order_no))"
                          "")

        # loading the customer list combo box
        my_cursor.execute("SELECT * FROM customer")
        record_cust = my_cursor.fetchall()

        customer_list = []
        if len(record_cust) > 0:
            for item in record_cust:
                customer_list.append(item[0])
            customer_list.insert(0, "*")

        # Commit changes
        sshdb.commit()

        # Close our connection
        sshdb.close()

        SSHDatabase_widgets(self)
        customer_list_combobox.configure(values=customer_list)
        if len(customer_list) != 0:
            customer_list_combobox.current(0)



    def ImportCustomerList(self):
        '''
        1) I want this function to read imported Excel file or csv file in their original state √
        2) I want to extract information that I need √
        3) Covert, rename, add etc...
        4) I want to store them in mysql server
        '''
        filename = filedialog.askopenfilename(
            initialdir="C:/Users/hqy_s/PycharmProjects/QYPython/build/QC",
            title="Import customer list file",
            filetypes=(("xlsx files", "*.xlsx"), ("All files", "*.*"))
        )

        if filename:
            # filename = r"{}".format(filename)
            df = pd.read_excel(filename)

            df = df.drop(['Company', 'City', 'State', 'Country', 'Postcode', 'Attachments', 'Open Balance', 'Notes'], axis='columns')
            df = df.replace(np.nan, "NULL")

            df_rows = df.to_numpy().tolist()

            sshdb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="5c4r3cr0w",
                database="ssh",
            )

            my_cursor = sshdb.cursor()

            for row in df_rows:
                sql_command = "INSERT INTO customer (customer, address, phone, email, currency) VALUES (%s, %s, %s, %s, %s)"
                values = (row[0], row[1], row[2], row[3], row[4])
                my_cursor.execute(sql_command, values)

            # loading the customer list combo box
            my_cursor.execute("SELECT * FROM customer")
            records_cust = my_cursor.fetchall()

            customer_list = []
            if len(records_cust) > 0:
                for item in records_cust:
                    customer_list.append(item[0])
                customer_list.insert(0, "*")
            customer_list_combobox.configure(values=customer_list)
            customer_list_combobox.current(0)

            # Commit changes
            sshdb.commit()

            # Close our connection
            sshdb.close()
            messagebox.showinfo("Info", "List has been successfully added to database.")



            self.focus()

        else:
            print("File not selected")
            self.focus()


    def ImportSalesorderList(self):
        '''
        1) I want this function to read imported Excel file or csv file in their original state
        2) I want to extract information that I need
        3) Covert, rename, add etc...
        4) I want to store them in mysql server
        '''

        filename = filedialog.askopenfilename(
            initialdir="C:/Users/hqy_s/PycharmProjects/QYPython/build/QC",
            title="Import sales order detail file",
            filetypes=(("xlsx files", "*.xlsx"), ("All files", "*.*"))
        )

        if filename:
            print("File selected")
            self.focus()

        else:
            print("File not selected")
            self.focus()

    def ImportPartList(self):
        '''
        1) I want this function to read imported Excel file or csv file in their original state
        2) I want to extract information that I need
        3) Covert, rename, add etc...
        4) I want to store them in mysql server
        '''
        filename = filedialog.askopenfilename(
            initialdir="C:/Users/hqy_s/PycharmProjects/QYPython/build/QC",
            title="Import part list file",
            filetypes=(("xlsx files", "*.xlsx"), ("All files", "*.*"))
        )

        if filename:
            df = pd.read_excel(filename)

            df = df.drop(['Company', 'City', 'State', 'Country', 'Postcode', 'Attachments', 'Open Balance', 'Notes'],
                         axis='columns')
            df = df.replace(np.nan, "NULL")

            df_rows = df.to_numpy().tolist()

            sshdb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="5c4r3cr0w",
                database="ssh",
            )

            my_cursor = sshdb.cursor()
            self.focus()

        else:
            print("File not selected")
            self.focus()





class SSHDatabase_widgets(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        global customer_list_combobox, customer_list,customer_entry_var, db_table

        # top section frame
        top_frame = CTkFrame(self)
        top_frame.columnconfigure((0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24), weight=1)
        top_frame.columnconfigure(1, weight=18)

        # treeview table frame
        table_frame = CTkFrame(self)

        CTkLabel(top_frame, text='Customer Name', font=('Arial', 15)).grid(row=0, column=0, sticky='w', pady=5, padx=(10, 0))
        CTkLabel(top_frame, text='Sales Order No.', font=('Arial', 15)).grid(row=1, column=0, sticky='w', pady=5, padx=(10, 0))
        CTkLabel(top_frame, text='Part No.', font=('Arial', 15)).grid(row=2, column=0, sticky='w', pady=5, padx=(10, 0))

        customer_entry_var = StringVar()

        customer_list_combobox = ttk.Combobox(top_frame, state='readonly', values=customer_list, textvariable=customer_entry_var, font=('Arial', 12))
        customer_list_combobox.grid(row=0, column=1, sticky='ew', padx=10)

        CTkEntry(top_frame, font=('Arial', 15)).grid(row=1, column=1, sticky='ew', padx=10)
        CTkEntry(top_frame, font=('Arial', 15)).grid(row=2, column=1, sticky='ew', padx=10)

        CTkButton(top_frame, text='Find', font=('Arial', 15), command=self.FindDB).grid(row=0, column=2, sticky='w')
        CTkButton(top_frame, text='Clear', font=('Arial', 15)).grid(row=1, column=2, sticky='w')
        CTkButton(top_frame, text='Refresh', font=('Arial', 15)).grid(row=2, column=2, sticky='w')

        # database table treeview
        db_table = ttk.Treeview(table_frame, columns=('part_name', 'order_no', 'customer', 'date_created'), show='headings')
        db_table.heading('part_name', text='Part name')
        db_table.heading('order_no', text='Sales order number')
        db_table.heading('customer', text='Customer')
        db_table.heading('date_created', text='Date created')
        db_table.pack(expand=True, fill='both', padx=5, pady=5)


        top_frame.pack(fill='x')
        table_frame.pack(expand=True, fill='both',)

        style = ttk.Style()

        style.theme_use("clam")

        style.configure("Treeview",
                        background="silver",
                        foreground="black",
                        rowheight=55,
                        fieldbackground="silver")

        self.pack(expand=True, fill='both')

    def FindDB(self):
        global db_table
        # print(customer_entry_var.get())
        # sql code to find customer's information
        sshdb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="5c4r3cr0w",
            database="ssh",
        )

        my_cursor = sshdb.cursor()

        sql = "SELECT part_name FROM parts WHERE customer = %s"
        customer_entry = (customer_entry_var.get(),)

        if customer_entry_var.get() == "*":
            # clear treeview previous data
            for part in db_table.get_children():
                db_table.delete(part)

            my_cursor.execute("SELECT part_name FROM parts")
        else:
            # clear treeview previous data
            for part in db_table.get_children():
                db_table.delete(part)

            my_cursor.execute(sql, customer_entry)

        myresult = my_cursor.fetchall()
        for row in myresult:
            db_table.insert("", "end", values=row)
        print(myresult)


App('SSH Software', (600,600))
