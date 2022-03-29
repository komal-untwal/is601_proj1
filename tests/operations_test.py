"""Testing the calculator operations """

from calculator.operations import Addition, Subtraction, Multiplication


def test_calculator_operations_add():
    """Testing the Calculator addition operation"""
    assert Addition.add(1, 1) == 2


def test_calculator_operations_subtract():
    """Testing the Calculator subtraction operation"""
    assert Subtraction.subtract(1, 1) == 0


def test_calculator_operations_multiply():
    """Testing the Calculator multiplication operation"""
    assert Multiplication.multiply(1, 1) == 1
