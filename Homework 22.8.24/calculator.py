import test_calculator
import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero!")
    return a / b

#a
def power (a, b):
    return a ** b

#b
def square_root (a):
    if a < 0:
        raise ValueError("cannot square root a negative number!")
    return math.sqrt(a)
# testing:
# check all cases
# auto keep functionality working
# make QA life more simple
# keep bug fix working

#c
def is_prime (a:int) -> bool:
    if a <= 1:
        return False
    for i in range (2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

#c part 2

def factorial (a:int) -> int:
    if a < 0:
        raise ValueError("factorial not defined for negative values")
    elif a == 1 or a == 0:
        return 1
    ans = 1
    for i in range (2,a + 1):
        ans *= i
    return ans
