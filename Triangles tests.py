import math

import pytest
from Triangles import *


def test_get_triangle_field_with_correct_inputs():
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


def test_get_triangle_field_using_Heron_formula():
    assert get_triangle_field_using_Heron_formula(3, 4, 5) == 6.0
    assert get_triangle_field_using_Heron_formula(1, 1, 2) == 'This is not triangle'
    assert math.isclose(get_triangle_field_using_Heron_formula(7, 10, 5), 16.24807680927192)
    assert get_triangle_field_using_Heron_formula(-3, 4, 5) == 'This is not triangle'
    assert get_triangle_field_using_Heron_formula(0, 4, 5) == 'This is not triangle'


def test_is_equilateral_triangle():
    assert is_equilateral_triangle(4569, 4569, 4569) == True
    assert is_equilateral_triangle(math.e, math.e, math.e) == True
    assert is_equilateral_triangle(3, 5, 4) == False
    assert is_equilateral_triangle(-5, -5, -5) == False
    assert is_equilateral_triangle(4, 4, 2) == False
    assert is_equilateral_triangle(4, 2, 4) == False
    assert is_equilateral_triangle(2, 4, 4) == False
    assert is_equilateral_triangle(0, 0, 0) == False


def test_is_isosceles_triangle():
    assert is_isosceles_triangle(4, 4, 2) == True
    assert is_isosceles_triangle(4, 2, 4) == True
    assert is_isosceles_triangle(2, 4, 4) == True
    assert is_isosceles_triangle(math.e, math.e, math.e) == True
    assert is_isosceles_triangle(3, 5, 4) == False
    assert is_isosceles_triangle(-5, -5, -5) == False
    assert is_isosceles_triangle(2, -5, -5) == False
    assert is_isosceles_triangle(1, 0, 0) == False
    assert is_isosceles_triangle(0, 0, 0) == False


def test_is_right_angled_triangle():
    assert is_right_angled_triangle(3, 5, 4) == True
    assert is_right_angled_triangle(3, 4, 5) == True
    assert is_right_angled_triangle(4, 5, 3) == True
    assert is_right_angled_triangle(4, 3, 5) == True
    assert is_right_angled_triangle(5, 3, 4) == True
    assert is_right_angled_triangle(5, 4, 3) == True
    assert is_right_angled_triangle(0, 2, 2) == False
    assert is_right_angled_triangle(-3, -5, -4) == False
    assert is_right_angled_triangle(5, 8, 10) == False

