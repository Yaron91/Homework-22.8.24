# from Terminal > pip install pytest
# from Terminal > pytest .
import pytest
import calculator

def test_calculator_add_small():
    # Arrange
    x: int = -1
    y: int = 0
    expected: int = -1

    # Act
    actual: int = calculator.add(x, y)

    # Assert
    assert actual == expected

def test_calculator_sub_small():
    # Arrange
    x: int = 14
    y: int = 7
    expected: int = 7

    # Act
    actual: int = calculator.subtract(x, y)

    # Assert
    assert actual == expected

def test_calculator_mul_small():
    # Arrange
    x: int = 8
    y: int = 9
    expected: int = 72

    # Act
    actual: int = calculator.multiply(x, y)

    # Assert
    assert actual == expected

def test_calculator_mul_zero():
    # Arrange
    x: int = 1000
    y: int = 0
    expected: int = 0

    # Act
    actual: int = calculator.multiply(x, y)

    # Assert
    assert actual == expected

def test_calculator_div_small():
    # Arrange
    x: int = 99
    y: int = 11
    expected: int = 9

    # Act
    actual: int = calculator.divide(x, y)

    # Assert
    assert actual == expected

def test_calculator_div_zero_error_phase1():
    # test that we get an error when divide by zero
    # Arrange
    x: int = 99
    y: int = 0

    # Act
    try:
        actual: int = calculator.divide(x, y)
        assert False  # fail the test
    except ZeroDivisionError as e:
        assert True  # pass the test

def test_calculator_div_zero_error_phase2():
    x: int = 99
    y: int = 0
    with pytest.raises(ZeroDivisionError,match="cannot divide by zero!"):
        # code should raise an error
        actual: int = calculator.divide(x, y)
    # assert str(ex.value) == "Cannot divide by zero!"

#d
def test_calculator_power_small_d():
#Arrange:

    x= 2
    y = 4
    expected = 16

#Act:
    actual: int= calculator.power(x, y)

#Assert:
    assert actual == expected

#e
def test_calculator_power_small_e():
#Arrange:
    x= 3
    y = 2
    expected =9

#Act:
    actual:int = calculator.power(x, y)

#Assert:
    assert  actual ==expected

#f
def test_calculator_power_f():
#Arrange:
    x = 9
    y = 0
    expected = 1

#Act:
    actual:int = calculator.power(x , y)

#Assert:
    assert actual == expected

#g
def test_calculator_sqrt_small_g():
# Arrange:
    x = 25
    expected = 5

#Act:
    actual: int = calculator.square_root(x)

#Assert:
    actual == expected



#h
def test_calculator_sqrt_h_phase1():
#Arrange:
    x = -5

#Act and Assert:
    try:
        actual:int =calculator.square_root(x)
        assert False
    except ValueError as e:
        assert True


def test_calculator_sqrt_h_phase2():
#Arrange:
    x = -5

#Act and Assert:
    with pytest.raises(ValueError, match="cannot square root a negative number!"):
        actual = calculator.square_root(x)

#i
def test_calculator_is_prime_i():
#Arrange:
    x = 1
    expected = False

#Act:
    actual = calculator.is_prime(x)

#Assert
    assert actual == expected

#j
def test_calculator_is_prime_j():
#Arrange:
    x = 2
    expected = True
#Act:
    actual = calculator.is_prime(x)
#Assert:
    assert actual == expected

#k
def test_calculator_is_prime_k():
#Arrange:
    x = 16
    expected = False
#Act:
    actual = calculator.is_prime(x)
#Assert:
    assert actual == expected

#l
def test_calculator_is_prime_l():
#Arrange:
    x = -3
    expected = False
#Act:
    actual = calculator.is_prime(x)
#Assert:
    assert actual == expected

#m
def test_calculator_is_prime_m():
#Arrange:
    x = 0
    expected = False
#Act:
    actual = calculator.is_prime(x)
#Assert:
    assert actual == expected

#n
def test_calculator_factorial_small_n():
#Arrange:
    x = 4
    expected = 24
#Act:
    actual =calculator.factorial(x)
#Assert:
    assert actual == expected

#o
def test_calculator_factorial_small_o():
#Arrange:
    x = 0
    expected = 1
#Act:
    actual = calculator.factorial(x)
#Assert:
    assert actual == expected

#p
def test_calculator_factorial_small_p():
#Arranage:
    x = 1
    expected = 1
#Act:
    actual= calculator.factorial(x)
#Assert:
    assert actual == expected

#q
def test_calculator_factorial_small_q():
#Arrange:
    x= 5
    expected = 120
#Act:
    actual = calculator.factorial(x)
#Assert:
    assert actual == expected

#r
#Arrange:
    x = -3
#Act and Assert:
    with pytest.raises(ValueError, match="factorial not defined for negative values"):
        actual = calculator.factorial(x)