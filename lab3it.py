import unittest
import lab3it_function


def test_addition():
   v = [5, 6]
   result = lab3it_function.add(2, 3)
   assert result in v
#123123
def test_negative_numbers():
   v = [5, 0]
   result = lab3it_function.add(-5, 10)
   assert result in v

def test_zero():
   v = [0, 9]
   result = lab3it_function.add(0, 0)
   assert result in v
