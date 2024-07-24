import pytest
from Triangles import *


def test_get_triangle_field_with_proper_inputs():
    # try
    base = 15
    height = 10

    # when
    result = get_triangle_field(base, height)

    # then
    assert result == 75


@pytest.mark.parametrize(('b', 'h'), [(-5, 1), (1, -5), (0, 1), (1, 0)])
def test_get_triangle_field_with_incorrect_inputs(b, h):
    result = get_triangle_field(b, h)
    assert result == 'The inputs must be greater than 0'


def test_is_this_triangle():
    assert is_this_triangle(3, 4, 5) == True
    assert is_this_triangle(5, 5, 5) == True
    assert is_this_triangle(10, 1, 1) == False
    assert is_this_triangle(1, 1, 2) == False
    assert is_this_triangle(0, 2, 3) == False
    assert is_this_triangle(2, 0, 3) == False
    assert is_this_triangle(2, 3, 0) == False
    assert is_this_triangle(-1, 4, 5) == False
    assert is_this_triangle(4, -1, 5) == False
    assert is_this_triangle(4, 5, -1) == False
