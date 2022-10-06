from calculator_model import CalculatorModel
from calculator_view import CalculatorView

class CalculatorController:
    def __init__(self, model: CalculatorModel, view: CalculatorView):
        self.model = model
        self.view = view
    
    def character_entered(self, value: str):
        self.model.result = value
        self.view.update_result(self.model.result)
