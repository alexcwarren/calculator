import tkinter as tk
from functools import partial


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
        self.__FONT = 'Arial'
        self.__MINWIDTH = 310
        self.__MINHEIGHT = 240
        self.minsize(self.__MINWIDTH, self.__MINHEIGHT)
        self.width = self.__MINWIDTH
        self.height = self.__MINHEIGHT
        self.geometry(f"{self.width}x{self.height}")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.__build_menu_bar()
        self.__build_result_window()
        self.__build_button_grid()
    
    def __get_font(self, size: int) -> str:
        return f'{self.__FONT} {size}'
    
    def __build_menu_bar(self):
        pass

    def __build_result_window(self):
        self.result_frame = tk.Frame(self)
        self.result_frame.columnconfigure(0, weight=1)
        self.result_frame.grid(sticky=tk.EW)
        self.result_fontsize = 24
        self.result_entry = tk.Entry(self.result_frame, width=17, font=self.__get_font(self.result_fontsize), justify=tk.RIGHT, disabledbackground="white")
        self.result_entry.config(state = tk.DISABLED)
        self.result_entry.grid(sticky=tk.EW)

    def __build_button_grid(self):
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(sticky=tk.NSEW)
        self.button_fontsize = 14
        self.buttons: dict[tk.Button] = dict()
        self.button_values = [
            ['7', '8', '9', '+'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '*'],
            ['.', '0', '=', '/']
        ]
        NUM_COLUMNS = max(len(row) for row in self.button_values)
        self.__BUTTON_MINWIDTH = 75
        self.__BUTTON_MINHEIGHT = 50
        for r,row in enumerate(self.button_values):
            self.button_frame.columnconfigure(r, weight=1, minsize=self.__BUTTON_MINWIDTH)
            row.extend([' '] * (NUM_COLUMNS - len(row)))
            for c,val in enumerate(row):
                self.button_frame.rowconfigure(c, weight=1, minsize=self.__BUTTON_MINHEIGHT)
                button_command = partial(self.__button_clicked, value=val)
                self.buttons[val] = tk.Button(self.button_frame, text=val, font=self.__get_font(self.button_fontsize), command=button_command)
                self.buttons[val].grid(row=r, column=c, sticky=tk.NSEW)

    def __button_clicked(self, value: str):
        print(value)
    
    def show(self):
        self.mainloop()
