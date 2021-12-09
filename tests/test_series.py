from math_series.series import fibonacci_function, lucas_function, sum_series
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

def test_sum_series():
  actual = sum_series(8, 4, 3)
  expected = 115
  assert actual == expected

def test_sum_series_lucas():
  actual = sum_series(6, 2, 1)
  expected = 18
  assert actual == expected

def test_sum_series_fibonacci():
  actual = sum_series(8)
  expected = 21
  assert actual == expected