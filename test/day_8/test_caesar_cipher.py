"""
Build out tests for day_8/caesar_cipher.py
"""

import pytest

from src.day_8.caesar_cipher import (
    caesar_cipher
)

from typing import List

test_caesar_cipher_params = [
    # [input prompts], exp_result
    (['encode', 'able', '2'], "cdng"),
    (['decode', 'cdng', '2'], "able"),
    (['encode', 'abcd', '25'], "zabc"),
    (['decode', 'zabc', '25'], "abcd"),
    (['encode', 'abcd', '26'], "abcd"),
    (['decode', 'zabc', '26'], "zabc"),
    (['encode', 'wxyz', '3'],  "zabc"),
    (['decode', 'zabc', '3'], "wxyz"),
]

@pytest.mark.parametrize("user_choice, exp_result", test_caesar_cipher_params)
def test_caesar_cipher(monkeypatch, user_choice:List[str], exp_result:str) -> None:
    """Test caesar cipher"""
    responses = iter(user_choice)
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    ret_text = caesar_cipher()
    assert (ret_text == exp_result), f'ERROR: Got {ret_text}, expected {exp_result}'
