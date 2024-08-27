"""
Build out tests for day_4/rock_paper_scissors.py
"""

import pytest
from unittest.mock import patch

from src.day_4.rock_paper_scissor import (
    rock_paper_scissors,
    prompt_tie,
    prompt_lose,
    prompt_win
)

from typing import List



test_rock_paper_scissors_params = [
    # user choice, computer random choice, expected outcome
    (0, 1, prompt_lose),
    (0, 0, prompt_tie),
    (0, 2, prompt_win),
    (1, 0, prompt_win),
    (1, 1, prompt_tie),
    (1, 2, prompt_lose),
    (2, 0, prompt_lose),
    (2, 1, prompt_win),
    (2, 2, prompt_tie),
]

@pytest.mark.parametrize("user_choice, comp_choice, exp_result", test_rock_paper_scissors_params)
def test_rock_paper_scissors(monkeypatch, user_choice:int, comp_choice:int, exp_result:str) -> None:
    """Test rock_paper_scissors"""
    with patch('src.day_4.rock_paper_scissor.randint', lambda a,b: comp_choice):
        monkeypatch.setattr('builtins.input', lambda msg: str(user_choice))
        assert rock_paper_scissors() == exp_result