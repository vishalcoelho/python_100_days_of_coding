"""
Build out tests for day_3/treasure_island.py
"""

import pytest
from src.day_3.treasure_island import (
    treasure_island,
    prompt_left_wait_red,
    prompt_left_wait_yellow,
    prompt_left_wait_blue,
    prompt_left_swim,
    prompt_right,
    prompt_error
)

from typing import List

test_treasure_island_params = [
    (["nonsense"], prompt_error),
    (["left", "swim"], prompt_left_swim),
    (["left", "wait", "red"], prompt_left_wait_red),
    (["left", "wait", "blue"], prompt_left_wait_blue),
    (["left", "wait", "yellow"], prompt_left_wait_yellow),
    (["right"], prompt_right)
]
@pytest.mark.parametrize("decision_tree, exp_result", test_treasure_island_params)
def test_treasure_island(monkeypatch, decision_tree:List[str], exp_result:str) -> None:
    """Test treasure_island"""
    responses = iter(decision_tree)
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    assert treasure_island() == exp_result