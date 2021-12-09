



"""
Recursion error
def fibonacci_function(n):
  if n <= 1:
    return 1
  return n + fibonacci_function((n-1) + (n -2))"""

def fibonacci_function(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  if n == 2:
    return 1
  return fibonacci_function(n-1) + fibonacci_function(n - 2)


def lucas_function(n):
  if n == 0:
    return 0
  if n == 1:
    return 2
  if n == 2:
    return 1
  else:
    return lucas_function(n-1) + lucas_function(n-2)


def sum_series(n, x=0, y=1):
  if n == 0:
    return x
  if n == 1:
    return y
  return sum_series(n-1, x, y) + sum_series(n-2, x, y)

def sum_series2(n, x=5, y=3):
  if n == 0:
    return x
  if n == 1:
    return y
  return sum_series(n-1, x, y) + sum_series(n-2, x, y)


"""
def sum_series(n, x=0, y=1):
  if n == 0:
    return x
  if n == 1:
    return y
  return sum_series(n-1, x, y) + sum_series(n-2, x, y)


-- Do not execute
  else:
    if n1 < n2:
      return sum_series(num-1, n1, n2) + (sum_series(num-2, n1, n2))
    else:
      return sum_series(num-1, n2, n1) + (sum_series(num-2, n2, n1))
"""

"""def test_sum_series():
  actual = sum_series()
  expected = 
  """
 