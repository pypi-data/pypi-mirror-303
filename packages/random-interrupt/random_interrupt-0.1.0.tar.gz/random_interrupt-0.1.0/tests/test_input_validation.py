import pytest
from argparse import Namespace
from src.random_interrupt.main import validate_input

def test_valid_inputs():
    args = Namespace(overall_time=60, number_of_interrupts=5, min_gap=None)
    assert validate_input(args) is None

def test_invalid_overall_time():
    args = Namespace(overall_time=-60, number_of_interrupts=5, min_gap=None)
    with pytest.raises(ValueError, match="Overall time must be positive"):
        validate_input(args)

def test_invalid_number_of_interrupts():
    args = Namespace(overall_time=60, number_of_interrupts=0, min_gap=None)
    with pytest.raises(ValueError, match="Number of interrupts must be positive"):
        validate_input(args)

def test_invalid_min_gap():
    args = Namespace(overall_time=60, number_of_interrupts=5, min_gap=-1)
    with pytest.raises(ValueError, match="Minimum gap must be non-negative"):
        validate_input(args)

def test_min_gap_too_large():
    args = Namespace(overall_time=60, number_of_interrupts=5, min_gap=15)
    with pytest.raises(ValueError, match="Minimum gap is too large"):
        validate_input(args)
