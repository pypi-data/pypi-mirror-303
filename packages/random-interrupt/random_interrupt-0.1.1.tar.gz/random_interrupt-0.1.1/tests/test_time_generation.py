import pytest
from argparse import Namespace
from src.random_interrupt.main import generate_interrupt_times

def test_correct_number_of_interrupts():
    args = Namespace(overall_time=60, number_of_interrupts=5, min_gap=None)
    interrupts = generate_interrupt_times(args)
    assert len(interrupts) == 5

def test_interrupts_within_range():
    args = Namespace(overall_time=60, number_of_interrupts=10, min_gap=None)
    interrupts = generate_interrupt_times(args)
    for interrupt in interrupts:
        assert 0 <= interrupt <= 60

def test_interrupts_are_sorted():
    args = Namespace(overall_time=60, number_of_interrupts=10, min_gap=None)
    interrupts = generate_interrupt_times(args)
    assert interrupts == sorted(interrupts)

def test_randomness():
    args = Namespace(overall_time=60, number_of_interrupts=100, min_gap=None)
    interrupts1 = generate_interrupt_times(args)
    interrupts2 = generate_interrupt_times(args)
    
    # Check that at least 50% of the interrupts are different
    differences = sum(1 for a, b in zip(interrupts1, interrupts2) if abs(a - b) > 1e-6)
    assert differences >= 50, f"Generated interrupt times are not sufficiently random. Only {differences} out of 100 were different."

def test_min_gap_respected():
    args = Namespace(overall_time=60, number_of_interrupts=10, min_gap=2)
    interrupts = generate_interrupt_times(args)
    gaps = [j-i for i, j in zip(interrupts[:-1], interrupts[1:])]
    assert all(gap >= 2 for gap in gaps)
