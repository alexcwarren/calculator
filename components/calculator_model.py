class CalculatorModel:
    __SIGNIFICANT_DIGITS: int = 14

    def __init__(self):
        self.__result = ""

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value: str):
        self.__result = value

    def add(self, operand1: float, operand2: float) -> str:
        return self.__approximate(operand1 + operand2)

    def subtract(self, operand1: float, operand2: float) -> str:
        return self.__approximate(operand1 - operand2)

    def multiply(self, operand1: float, operand2: float) -> str:
        return self.__approximate(operand1 * operand2)

    def divide(self, operand1: float, operand2: float) -> str:
        if operand2 == 0:
            return "Cannot divide by 0"
        return self.__approximate(operand1 / operand2)

    def __approximate(self, number: float) -> str:
        result: str = str(round(number, CalculatorModel.__SIGNIFICANT_DIGITS))
        if "." in result:
            result = result.rstrip("0")
            if result.endswith("."):
                result = result[:-1]
        self.__result = result
        return result
