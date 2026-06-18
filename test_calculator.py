import pytest
from calculator import *

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(12, 3) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
