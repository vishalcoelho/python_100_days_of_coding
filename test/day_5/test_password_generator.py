"""
Build out tests for day_5/password_generator.py
"""

import pytest
from pytest_mock import mocker

from src.day_5.password_generator import (
    password_generator,
)

from typing import List

test_password_generator_params = [
    # [input prompts], [randint return choice] expected password
    #                  |
    #                  v
    #                  [[rand letter idx],[rand symbol idx],[rand number idx],[rand reordeing of all chars]]
    #
    ([2, 2, 2], [[23, 4], [2, 6], [1, 7], [5,4,3,2,1,0]] , '71)$ex'),
    ([3, 4, 5], [[23, 4, 9], [2, 6, 8, 0], [4, 0, 7, 8, 2], [0,11,1,10,2,9,3,8,4,7,5,6]] , 'x2e8j7$0)4+!'),
]

@pytest.fixture(scope="module")
def mocker_fixture():
    return mocker

@pytest.mark.parametrize("user_choice, randint_rets, exp_result", test_password_generator_params)
def test_password_generator(monkeypatch, mocker:mocker_fixture,
                            user_choice:List[str], randint_rets:List[int], exp_result:str) -> None:
    """Test password_generator"""

    # Patch radnint to get these 'random' integers
    # mock_response = mocker.MagicMock()
    # mock_response.side_effect = iter(randint_rets)
    mocker.patch("random.sample", side_effect=randint_rets)

    responses = iter(user_choice)
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    assert password_generator() == exp_result