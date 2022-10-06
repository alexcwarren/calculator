import components.calculator_model as calcmodel
import components.calculator_view as calcview
from components.characters import Character


class CalculatorController:
    def __init__(self, model: calcmodel.CalculatorModel, view: calcview.CalculatorView):
        self.model = model
        self.view = view

    def character_entered(self, value: Character):
        self.model.result = value
        self.view.update_result(self.model.result)
