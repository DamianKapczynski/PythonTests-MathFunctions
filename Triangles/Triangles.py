import math


def get_triangle_field(base, height):
    if (base > 0) & (height > 0):
        return base * height * 1 / 2
    else:
        return "The inputs must be greater than 0"


def is_this_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a) and (a > 0) and (b > 0) and (c > 0)


def get_triangle_perimeter(a, b, c):
    if is_this_triangle(a, b, c):
        return a + b + c
    else:
        return "This is not triangle"


def get_triangle_field_using_Heron_formula(a, b, c):
    if is_this_triangle(a, b, c):
        p = (a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    else:
        return "This is not triangle"


def is_equilateral_triangle(a, b, c):
    return is_this_triangle(a, b, c) and (a == b == c)


def is_isosceles_triangle(a, b, c):
    return is_this_triangle(a, b, c) and ((a == b) or (b == c) or (a == c))


def is_right_angled_triangle(a, b, c):
    return is_this_triangle(a, b, c) and \
        ((a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (c ** 2 + b ** 2 == a ** 2))


def type_of_triangle(a, b, c):
    if is_equilateral_triangle(a, b, c):
        return('Equilateral triangle')
    elif is_isosceles_triangle(a, b, c):
        return('Isosceles triangle')
    elif is_right_angled_triangle(a, b, c):
        return('Right-angled triangle')
    elif is_this_triangle(a, b, c):
        return('Scalene triangle')
    else:
        return('This is not triangle')
