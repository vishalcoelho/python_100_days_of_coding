"""
Build out tests for day_2/tip_calculator.py
"""

import pytest
from src.day_2.tip_calculator import tip_calculator

test_tip_calculator_params = [
    (150.0, 12, 5, 33.6),
    (245.67, 10, 8, 33.78),
    (311.96, 15, 3, 119.58),
]
@pytest.mark.parametrize("bill_total, tip, n_people, exp_bill_per_head", test_tip_calculator_params)
def test_tip_calculator(monkeypatch, bill_total, tip, n_people, exp_bill_per_head) -> None:
    """Test tip_calculator"""
    responses = iter([bill_total, tip, n_people])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    assert tip_calculator() == exp_bill_per_head