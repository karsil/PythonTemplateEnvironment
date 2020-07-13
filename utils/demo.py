"""
A collection of functions
"""

def add_one(number):
    """
    Increment the give parameter
    """
    return number + 1

def sum_up(arg: list) -> int:
    """
    Sum up all values in a list and return sum
    """
    if arg is None:
        raise ValueError("Input must not be null!")
    total = 0
    for val in arg:
        total += val
    return total

def divide(numerator, denominator) -> float:
    """A simple divide functionaity"""
    if denominator == 0:
        raise ZeroDivisionError("Division by zero")
    return numerator / denominator
