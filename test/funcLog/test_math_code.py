"""
Build out tests for funcLog/math_code.py
"""

from funcLog.math_code import add, sub, mul, div

def test_add() -> None:
    """Test adding"""
    assert add(1, 2) == 3

def test_mul() -> None:
    """Test multiplying"""
    assert mul(4, 2) == 8

def test_div() -> None:
    """Test dividing"""
    assert div(1, 2) == 0

def test_sub() -> None:
    """Test subtracting"""
    assert sub(1, 2) == -1
