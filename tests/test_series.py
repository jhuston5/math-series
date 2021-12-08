from math_series.series import fibonacci_function, lucas_function
import pytest


"""
def test_version():
  assert __version__ == '0.1.0'
"""
def test_fib_two():
  actual = fibonacci_function(2)
  expected = 1
  assert actual == expected

def test_fib_eight():
  actual = fibonacci_function(8)
  expected = 21
  assert actual == expected

def test_fib_five():
  actual = fibonacci_function(5)
  expected = 5
  assert actual == expected

def test_lucas_eight():
  actual = lucas_function(8)
  expected = 29
  assert actual == expected


 