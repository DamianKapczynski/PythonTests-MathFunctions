import pytest
from Triangles import *

def test_get_triangle_field():
    #try
    base = 15
    height = 10

    #when
    result = get_triangle_field(base, height)

    #then
    assert result == 75

def test_correct_triangle():

    result = is_this_triangle(2, 3, 4)
    assert result == True

def test_incorrect_triangle():

    result = is_this_triangle(2, 2, 5)
    assert result == False