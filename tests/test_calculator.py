import pytest

import components.calculator_view as calcview
import components.characters as chars
from calculator import Calculator


@pytest.fixture
def calculator_app():
    return Calculator(calcview.Calculator_MockView())


@pytest.mark.parametrize(
    "operand, result",
    [(0.0, "0"), (7.3, "7.3"), (-6.0, "-6")],
)
def test_add(operand: float, result: str, calculator_app):
    assert calculator_app.model.add(operand) == result


@pytest.mark.parametrize(
    "operand, result",
    [(0.0, "0"), (3.7, "-3.7"), (-4.0, "4")],
)
def test_subtract(operand: float, result: str, calculator_app):
    assert calculator_app.model.subtract(operand) == result


@pytest.mark.parametrize(
    "operand, result",
    [(0.0, "0"), (7.3, "0"), (-6.0, "0")],
)
def test_multiply(operand: float, result: str, calculator_app):
    assert calculator_app.model.multiply(operand) == result


@pytest.mark.parametrize(
    "operand, result",
    [(0.0, "Cannot divide by 0"), (1, "0"), (-4, "0")],
)
def test_divide(operand: float, result: str, calculator_app):
    assert calculator_app.model.divide(operand) == result


@pytest.mark.parametrize("character, result", [(chars.ZERO, "0")])
def test_character_entered(character: chars.Character, result: str, calculator_app):
    calculator_app.controller.character_entered(character)
    assert calculator_app.model.result == result
    assert calculator_app.view.result == result
