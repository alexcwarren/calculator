import abc
import tkinter as tk
from functools import partial

import components.characters as chars


class CalculatorView:
    def __init__(self):
        self.__controller = None

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, controller):
        import components.calculator_controller as calccontroller

        self.__controller: calccontroller.CalculatorController = controller

    @abc.abstractmethod
    def update_result(self, value: str):
        return


class Calculator_GUIView(tk.Tk, CalculatorView):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.FONT = "Arial"
        self.MINWIDTH = 310
        self.MINHEIGHT = 340
        self.minsize(self.MINWIDTH, self.MINHEIGHT)
        self.width = self.MINWIDTH
        self.height = self.MINHEIGHT
        self.geometry(f"{self.width}x{self.height}")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.build_menu_bar()
        self.build_result_window()
        self.build_button_grid()

    def get_font(self, size: int) -> str:
        return f"{self.FONT} {size}"

    def build_menu_bar(self):
        pass

    def build_result_window(self):
        self.result_frame = tk.Frame(self)
        self.result_frame.columnconfigure(0, weight=1)
        self.result_frame.grid(sticky=tk.EW)
        self.result_fontsize = 24
        self.result_variable = tk.StringVar()
        self.result_variable.set(chars.ZERO)
        self.result_entry = tk.Entry(
            self.result_frame,
            width=17,
            font=self.get_font(self.result_fontsize),
            justify=tk.RIGHT,
            disabledbackground="white",
            textvariable=self.result_variable,
        )
        self.result_entry.config(state=tk.DISABLED)
        self.result_entry.grid(sticky=tk.EW)

    def build_button_grid(self):
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(sticky=tk.NSEW)
        self.button_fontsize = 14
        self.buttons: dict[tk.Button] = dict()
        self.button_values: list[list[chars.Character]] = [
            [chars.PERCENT, chars.CLEAR_ERR, chars.CLEAR, chars.BACKSPACE],
            [chars.EMPTY, chars.EMPTY, chars.EMPTY, chars.DIVIDE],
            [chars.SEVEN, chars.EIGHT, chars.NINE, chars.MULTIPLY],
            [chars.FOUR, chars.FIVE, chars.SIX, chars.SUBTRACT],
            [chars.ONE, chars.TWO, chars.THREE, chars.ADD],
            [chars.PLUS_MINUS, chars.ZERO, chars.DECIMAL_POINT, chars.EQUALS],
        ]
        NUM_COLUMNS = max(len(row) for row in self.button_values)
        self.BUTTON_MINWIDTH = 75
        self.BUTTON_MINHEIGHT = 50
        for r, row in enumerate(self.button_values):
            self.button_frame.rowconfigure(r, weight=1, minsize=self.BUTTON_MINHEIGHT)
            row.extend([chars.EMPTY] * (NUM_COLUMNS - len(row)))
            for c, val in enumerate(row):
                if r == 0:
                    self.button_frame.columnconfigure(
                        c, weight=1, minsize=self.BUTTON_MINWIDTH
                    )
                if val != chars.EMPTY:
                    button_command = partial(self.button_pressed, value=val)
                    self.buttons[val] = tk.Button(
                        self.button_frame,
                        text=val,
                        font=self.get_font(self.button_fontsize),
                        command=button_command,
                    )
                    self.buttons[val].grid(row=r, column=c, sticky=tk.NSEW)

    def button_pressed(self, value: chars.Character):
        self.controller.character_entered(value)

    def update_result(self, value: str):
        self.result_variable.set(value)

    def show(self):
        self.mainloop()


class Calculator_MockView(CalculatorView):
    def __init__(self):
        super().__init__()
        self.__result = ""

    @property
    def result(self):
        return self.__result

    def update_result(self, value: str):
        self.__result = value
