class Character:
    def __init__(self, value: str):
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value

    def __repr__(self):
        return f"{self.value}"


EMPTY = Character("")


class Number(Character):
    def __init__(self, value: str):
        super().__init__(value)


ZERO = Number("0")
ONE = Number("1")
TWO = Number("2")
THREE = Number("3")
FOUR = Number("4")
FIVE = Number("5")
SIX = Number("6")
SEVEN = Number("7")
EIGHT = Number("8")
NINE = Number("9")
DECIMAL_POINT = Number(".")


class Operator(Character):
    def __init__(self, value: str):
        super().__init__(value)


ADD = Operator("+")
SUBTRACT = Operator("-")
MULTIPLY = Operator("*")
DIVIDE = Operator("/")
EQUALS = Operator("=")
CLEAR = Operator("C")
CLEAR_ERR = Operator("CE")
PERCENT = Operator("%")
PLUS_MINUS = Operator("\u00B1")
BACKSPACE = Operator("\u2190")
