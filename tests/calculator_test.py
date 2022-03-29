"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


def tuple_list():
    """Arranging Data for AAA Testing"""
    return 1.0, 2


def test_calculator_add_method():
    """Testing the Calculator add"""
    # this is show using the calculator object add method

    # Act for AAA testing
    result_add = Calculator.add(tuple_list())

    # Assertion for AAA testing
    assert result_add == 3


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    result_sub = Calculator.subtract(tuple_list())
    assert result_sub == -3


def test_calculator_multiply_method():
    """Testing the Calculator multiply"""
    result_mult = Calculator.multiply(tuple_list())
    assert result_mult == 2
