"""
Build out tests for day_10/test_calculator.py
"""

import pytest

from src.day_10.calculator import (
    calculator
)

from typing import List

test_calculator_params = [
# [input prompts], exp_result
    (['1.0', '+', '2.0', 'q'], 3.0),
    (['3.0', '*', '2.0', 'q'], 6.0),
    (['1.0', '-', '2.0', 'q'], -1.0),
    (['1.0', '/', '2.0', 'q'], 0.5),
    (['1.0', '+', '2.0', 'y', '*', '4.0', 'y', '-', '2', 'q'], 10.0),
    (['1.0', '+', '2.0', 'y', '*', '4.0', 'y', '-', '2', 'n', '1.0', '/', '8.0', 'q'], 0.125),
]

@pytest.mark.parametrize("user_choice, exp_result", test_calculator_params)
def test_calculator(monkeypatch, user_choice:List[str], exp_result:float) -> None:
    """Test calculator"""
    responses = iter(user_choice)
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ret_val = calculator()
    assert (ret_val == exp_result), f'ERROR: Got {ret_val}, expected {exp_result}'
