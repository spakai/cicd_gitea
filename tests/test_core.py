"""Tests for Fibonacci core logic."""
import pytest
from fib.core import fibonacci

@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (5, 5), (10, 55)])
def test_fibonacci_values(n: int, expected: int) -> None:
    assert fibonacci(n) == expected

def test_fibonacci_negative() -> None:
    with pytest.raises(ValueError):
        fibonacci(-1)
