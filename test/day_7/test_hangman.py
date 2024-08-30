"""
Build out tests for day_7/hangman.py
"""

import pytest
from pytest_mock import mocker

from src.day_7.hangman import (
    hangman,
    prompt_lose,
    prompt_win,
    reset_counters,
)

from typing import List

test_hangman_params = [
    # [input prompts], mocked_word_choice, expected n_lives, expected return prompt
    (['c', 'a', 'm', 'e', 'l'], "camel", 6, prompt_win),
    (['c', 'a', 'm', 'e', 'b', 'l'], "camel", 5, prompt_win),
    (['m', 'i', 'c', 'e', 'z', 'x', 'y', 'b', 'r'], "camel", 0, prompt_lose),
    (['a', 'l', 'p', 'e', 'h'], "alpha", 5, prompt_win),
]

@pytest.fixture(scope="module")
def mocker_fixture():
    return mocker

test_setup_count = 0
@pytest.fixture
def test_setup():
    global test_setup_count
    test_setup_count += 1
    print(f"Calling test_setup() {test_setup_count}")
    reset_counters()

@pytest.mark.parametrize("user_choice, randchoice_rets, exp_n_lives, exp_result", test_hangman_params)
def test_hangman(monkeypatch, mocker:mocker_fixture, test_setup,
                 user_choice:List[str], randchoice_rets:int, exp_n_lives, exp_result:str) -> None:
    """Test hangman"""

    # Patch random.choice to get these 'random' integers
    mocker.patch("random.choice", return_value=randchoice_rets)
    # Patch time.sleep to do nothing
    mocker.patch("time.sleep")

    responses = iter(user_choice)
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    n_lives, ret_prompt = hangman()
    assert ret_prompt == exp_result
    assert n_lives == exp_n_lives