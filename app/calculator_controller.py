from calculator_model import CalculatorModel
from calculator_view import CalculatorView

class CalculatorController:
    def __init__(self, model: CalculatorModel, view: CalculatorView):
        self.model = model
        self.view = view
