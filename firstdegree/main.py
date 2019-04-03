#!/usr/bin/env python3
import re

# Operators:
#   Addition
# Generators:
#   1, x (the variable)
# Elements in ring:
#   First degree polynomial: kx + m

class FirstDegree(object):
  def __init__(self, first, constant):
    self.first = first
    self.constant = constant

  def __add__(self, other):
    return FirstDegree(self.first + other.first,
                       self.constant + other.constant)

  def eval(self, x):
    return self.first * x + self.constant

# Generators
ONE = FirstDegree(0, 1)
X = FirstDegree(1, 0)

def main():
  import sys
  for line in sys.stdin:
    print(line)

def test():
  import math
  import random

  def test_random(poly, expected):
    for i in range(100):
      x = random.uniform(-1000, 1000)
      assert(poly.eval(i) == expected(i))

  test_random(X + X + ONE,
              lambda x: 2*x + 1)
  print("Test success")

test()
if __name__ == '__main__':
  main()
