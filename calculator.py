# https://github.com/GraberMN/lab10-MG-MG.git
# Partner 1: Mateo Graber (git config user.email "grabermn3@gmail.com")
# Partner 2: Mateo Graber (git config user.email "graberm@ufl.edu")
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    if a < 0:
        raise ValueError
    try:
        return math.sqrt(a)
    except ValueError:
        print("square root cannot be negative")

def hypotenuse(a, b):
    try:
        if a < 0 or b < 0:
            raise Exception
    except:
        pass
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a               # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a <= 0:
        raise ValueError
    return math.log(b, a)          # use math library/raise ValueError

def exp(a, b):
    return a ** b


