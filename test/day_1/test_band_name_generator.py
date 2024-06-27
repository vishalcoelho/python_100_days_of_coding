"""
Build out tests for day_1/band_name_generator.py
"""

import pytest
from src.day_1.band_name_generator import generate_band_name

test_generate_band_name_params = [
    ('Austin', 'Rocket'),
    ('Philly', 'Muppet'),
    ('Washington', 'Aspen'),
]
@pytest.mark.parametrize("city_name, pet_name", test_generate_band_name_params)
def test_generate_band_name(monkeypatch, city_name, pet_name) -> None:
    """Test generate_band_name"""
    responses = iter([city_name, pet_name])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    assert generate_band_name() == city_name + " " + pet_name