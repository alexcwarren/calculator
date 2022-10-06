import components.calculator_controller as calccontroller
import components.calculator_model as calcmodel
import components.calculator_view as calcview


class Calculator:
    def __init__(self, view=None):
        self.model = calcmodel.CalculatorModel()
        self.view = view or calcview.Calculator_GUIView()
        self.controller = calccontroller.CalculatorController(self.model, self.view)
        self.view.controller = self.controller

    def start(self):
        self.view.show()


if __name__ == "__main__":
    Calculator().start()
