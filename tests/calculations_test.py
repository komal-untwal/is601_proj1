"""Testing the Calculator"""
# From specifies the namespace
from calculator.calculations import Addition, Subtraction, Multiplication


def test_calculation_multiplication_instance():
    """Testing the Calculator Multiplication instance"""
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert isinstance(calculation, Multiplication)


def test_calculation_subtraction_instance():
    """Testing the Calculator Subtraction instance"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert isinstance(calculation, Subtraction)


def test_calculation_addition_instance():
    """Testing the Calculator addition instance"""
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert isinstance(calculation, Addition)


def test_calculation_add_get_result_method():
    """Testing the Calculator addition result"""
    # this is show using the calculator object add method
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert calculation.get_result() == 3


def test_calculation_subtract_get_result_method():
    """Testing the Calculator Subtraction result"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    # -3 since we are looping our tuple & subtracting
    assert calculation.get_result() == -3


def test_calculation_multiply_get_result_method():
    """Testing the Calculator multiplication result"""
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert calculation.get_result() == 2
