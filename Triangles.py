def get_triangle_field(base, height):

    return(base * height * 1/2)

def is_this_triangle(a, b, c):
    if (a+b > c) & (a+c > b) & (b+c > a):
        return(True)
    else:
        return(False)
