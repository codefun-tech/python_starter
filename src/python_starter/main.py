"""Simple calculator module.

Simple calculator module that provides basic arithmetic operations and a Calculator class for chaining operations.
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Add two numbers.

    Args:
        a: The first number
        b: The second number

    Returns:
        The sum of the two numbers

    Examples:
        >>> add(1, 2)
        3
        >>> add(1.5, 2.5)
        4.0
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract two numbers.

    Args:
        a: The minuend
        b: The subtrahend

    Returns:
        The difference of the two numbers
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers.

    Args:
        a: The first number
        b: The second number

    Returns:
        The product of the two numbers
    """
    return a * b


def divide(a: Number, b: Number) -> float:
    """Divide two numbers.

    Args:
        a: The dividend
        b: The divisor

    Returns:
        The quotient of the two numbers

    Raises:
        ValueError: If the divisor is 0
    """
    if b == 0:
        raise ValueError("Divisor cannot be 0")
    return a / b


class Calculator:
    """Calculator class that supports chained operations.

    Attributes:
        result: The current calculation result

    Examples:
        >>> calc = Calculator(10)
        >>> calc.add(5).multiply(2).result
        30
    """

    def __init__(self, initial_value: Number = 0) -> None:
        """Initialize the calculator.

        Args:
            initial_value: The initial value, default is 0
        """
        self.result: Number = initial_value

    def add(self, value: Number) -> "Calculator":
        """Add a value to the current result.

        Args:
            value: The value to add

        Returns:
            The calculator instance to support method chaining
        """
        self.result = add(self.result, value)
        return self

    def subtract(self, value: Number) -> "Calculator":
        """Subtract a value from the current result.

        Args:
            value: The value to subtract

        Returns:
            The calculator instance to support method chaining
        """
        self.result = subtract(self.result, value)
        return self

    def multiply(self, value: Number) -> "Calculator":
        """Multiply a value with the current result.

        Args:
            value: The value to multiply

        Returns:
            The calculator instance to support method chaining
        """
        self.result = multiply(self.result, value)
        return self

    def divide(self, value: Number) -> "Calculator":
        """Divide a value from the current result.

        Args:
            value: The value to divide

        Returns:
            The calculator instance to support method chaining

        Raises:
            ValueError: If the divisor is 0
        """
        self.result = divide(self.result, value)
        return self

    def reset(self, value: Number = 0) -> "Calculator":
        """Reset the calculator.

        Args:
            value: The value to reset to, default is 0

        Returns:
            The calculator instance to support method chaining
        """
        self.result = value
        return self
