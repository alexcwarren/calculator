import components.characters as chars


class CalculatorModel:
    __SIGNIFICANT_DIGITS: int = 14

    def __init__(self):
        self.__result: str = "0"
        self.__operation = None

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, ch: chars.Character):
        if isinstance(ch, chars.Number):
            if ch == chars.ZERO and self.__result.startswith(chars.ZERO.value):
                return
            if ch == chars.DECIMAL_POINT and chars.DECIMAL_POINT.value in self.__result:
                return
            if self.__result.startswith(chars.ZERO.value):
                self.__result = ""
            self.__result += ch.value
        else:
            if ch == chars.CLEAR:
                self.__result = ""
            elif ch == chars.CLEAR_ERR:
                self.__result = ""
            elif ch == chars.BACKSPACE:
                self.__result = self.__result[:-1]
            elif ch == chars.PLUS_MINUS:
                self.multiply(-1.0)
            elif ch == chars.ADD:
                self.__operation = self.add

    def add(self, operand: float) -> str:
        return self.__approximate(float(self.__result) + operand)

    def subtract(self, operand: float) -> str:
        return self.__approximate(float(self.__result) - operand)

    def multiply(self, operand: float) -> str:
        return self.__approximate(float(self.__result) * operand)

    def divide(self, operand: float) -> str:
        if operand == 0:
            return "Cannot divide by 0"
        return self.__approximate(float(self.__result) / operand)

    def __approximate(self, number: float) -> str:
        result: str = str(round(number, CalculatorModel.__SIGNIFICANT_DIGITS))
        if chars.DECIMAL_POINT.value in result:
            result = result.rstrip("0")
            if result.endswith("."):
                result = result[:-1]
        if float(result) == 0:
            result = chars.ZERO.value
        self.__result = result
        return result
