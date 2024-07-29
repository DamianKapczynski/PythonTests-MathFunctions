import math


def get_triangle_field(base, height):
    if (base > 0) & (height > 0):
        return base * height * 1 / 2
    else:
        return "The inputs must be greater than 0"


def is_this_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a) and (a > 0) and (b > 0) and (c > 0)


def get_triangle_field_using_Heron_formula(a, b, c):
    if is_this_triangle(a, b, c):
        p = (a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    else:
        return "This is not triangle"