from itertools import zip_longest
import tkinter as tk
import tkinter.ttk as ttk


class CalculatorView:
    def __init__(self):
        self.__controller = None

    @property
    def controller(self):
        return self.__controller
    
    @controller.setter
    def controller(self, controller):
        from calculator_controller import CalculatorController
        self.__controller: CalculatorController = controller


class Calculator_GUIView(tk.Tk, CalculatorView):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.__build_menu_bar()
        self.__build_result_window()
        self.__build_button_grid()
    
    def __build_menu_bar(self):
        pass

    def __build_result_window(self):
        pass

    def __build_button_grid(self):
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack()
        self.buttons: dict[ttk.Button] = dict()
        self.button_values = [
            ['7', '8', '9', '+'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '*'],
            ['.', '0', '=', '/']
        ]
        NUM_COLUMNS = max(len(row) for row in self.button_values)
        for r,row in enumerate(self.button_values):
            row.extend([' '] * (NUM_COLUMNS - len(row)))
            for c,val in enumerate(row):
                self.buttons[val] = ttk.Button(self.button_frame, text=val)
                self.buttons[val].grid(row=r, column=c)
    
    def show(self):
        self.mainloop()
