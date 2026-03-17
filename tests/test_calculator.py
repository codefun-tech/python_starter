"""Calculator tests."""

import pytest

from src.python_starter import Calculator, add, divide, multiply, subtract


class TestBasicOperations:
    """Basic arithmetic function tests."""

    def test_add_integers(self) -> None:
        """Test integer addition."""
        assert add(1, 2) == 3
        assert add(-1, 1) == 0
        assert add(0, 0) == 0

    def test_add_floats(self) -> None:
        """Test float addition."""
        assert add(1.5, 2.5) == 4.0
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract(self) -> None:
        """Test subtraction."""
        assert subtract(5, 3) == 2
        assert subtract(3, 5) == -2
        assert subtract(0, 0) == 0

    def test_multiply(self) -> None:
        """Test multiplication."""
        assert multiply(3, 4) == 12
        assert multiply(-2, 3) == -6
        assert multiply(0, 100) == 0

    def test_divide(self) -> None:
        """Test division."""
        assert divide(10, 2) == 5.0
        assert divide(7, 2) == 3.5
        assert divide(-10, 2) == -5.0

    def test_divide_by_zero(self) -> None:
        """Test division by zero."""
        with pytest.raises(ValueError, match="Divisor cannot be 0"):
            divide(10, 0)


class TestCalculator:
    """Calculator class tests."""

    def test_initial_value(self) -> None:
        """Test initial value."""
        calc = Calculator()
        assert calc.result == 0

        calc = Calculator(10)
        assert calc.result == 10

    def test_chain_operations(self) -> None:
        """Test chained operations."""
        calc = Calculator(10)
        result = calc.add(5).multiply(2).subtract(10).divide(2).result
        assert result == 10.0

    def test_reset(self) -> None:
        """Test reset functionality."""
        calc = Calculator(100)
        calc.add(50).reset()
        assert calc.result == 0

        calc.reset(42)
        assert calc.result == 42


# Parameterized test example
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, -1, -2),
        (100, 200, 300),
        (1.5, 2.5, 4.0),
    ],
)
def test_add_parametrized(a: float, b: float, expected: float) -> None:
    """Parameterized test: addition."""
    assert add(a, b) == expected
