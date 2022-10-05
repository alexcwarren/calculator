import pytest

from app.calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator().model


@pytest.mark.parametrize(
    "operand1, operand2, result",
    [(0, 0, "0"), (3, 7, "10"), (-4, -6, "-10"), (3, -6, "-3")],
)
def test_add(operand1: float, operand2: float, result: str, calculator):
    assert calculator.add(operand1, operand2) == result


@pytest.mark.parametrize(
    "operand1, operand2, result",
    [(0, 0, "0"), (3, 7, "-4"), (-4, -6, "2"), (3, -6, "9")],
)
def test_subtract(operand1: float, operand2: float, result: str, calculator):
    assert calculator.subtract(operand1, operand2) == result


@pytest.mark.parametrize(
    "operand1, operand2, result",
    [(0, 0, "0"), (3, 7, "21"), (-4, -6, "24"), (3, -6, "-18")],
)
def test_multiply(operand1: float, operand2: float, result: str, calculator):
    assert calculator.multiply(operand1, operand2) == result


@pytest.mark.parametrize(
    "operand1, operand2, result",
    [
        (1, 0, "Cannot divide by 0"),
        (0, 1, "0"),
        (6, 3, "2"),
        (-4, -6, "0.66666666666667"),
        (3, -6, "-0.5"),
    ],
)
def test_divide(operand1: float, operand2: float, result: str, calculator):
    assert calculator.divide(operand1, operand2) == result
