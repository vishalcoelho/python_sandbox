""" Module docstring"""


class Arithmetic:
    """ Defines all the arithmetic operation."""

    def __init__(self) -> None:
        self.result = 0.0

    def add(self, operand: float) -> None:
        """Add a value to the running result."""
        self.result += operand

    def sub(self, operand: float) -> None:
        """subtract a value from the running result."""
        self.result -= operand

    def mul(self, operand: float) -> None:
        """Multiply a value with the running result."""
        self.result *= operand

    def exp(self, operand: float) -> None:
        """Raise the running result to the operand."""
        self.result **= operand

    def calculate(self, op_name: str, op_operand: float) -> None:
        """ Call the right arithmetic operation based on the op_name passed
        in."""
        match op_name:
            case 'add':
                self.add(op_operand)
            case 'subtract':
                self.sub(op_operand)
            case 'divide':
                self.div(op_operand)
            case 'multiply':
                self.mul(op_operand)
            case 'exponent':
                self.exp(op_operand)
            case _:
                raise Exception("Unknown op")

    def div(self, operand: float) -> None:
        """Divide the running result by the operand."""
        self.result /= operand

    def print_result(self) -> None:
        """Prints result"""
        print(f"Result: {self.result}")

    def clear(self) -> None:
        """ Clears the result."""
        self.result = 0.0
