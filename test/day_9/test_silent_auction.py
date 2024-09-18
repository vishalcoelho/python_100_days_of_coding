"""
Build out tests for day_9/silent_auction.py
"""

import pytest

from src.day_9.silent_auction import (
    silent_auction
)

from typing import List

test_silent_auction_params = [
    # [input prompts], exp_result
    (['Willow', '23', 'yes', 'Jinto', '24', 'yes', 'Franky', '67', 'no'], "Franky"),
    (['Willow', '13', 'yes', 'Jinto', '24', 'yes', 'Franky', '23', 'no'], "Jinto"),
    (['Willow', '123', 'yes', 'Jinto', '24', 'yes', 'Franky', '67', 'no'], "Willow"),
]

@pytest.mark.parametrize("user_choice, exp_result", test_silent_auction_params)
def test_silent_auction(monkeypatch, user_choice:List[str], exp_result:str) -> None:
    """Test caesar cipher"""
    responses = iter(user_choice)
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ret_text = silent_auction()
    assert (ret_text == exp_result), f'ERROR: Got {ret_text}, expected {exp_result}'
