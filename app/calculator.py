from calculator_model import CalculatorModel
from calculator_view import *
from calculator_controller import CalculatorController


class Calculator:
    def __init__(self, view=None):
        self.model = CalculatorModel()
        self.view = view or Calculator_GUIView()
        self.controller = CalculatorController(self.model, self.view)
        self.view.controller = self.controller
    
    def start(self):
        self.view.show()


if __name__ == '__main__':
    Calculator().start()
