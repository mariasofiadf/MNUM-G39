

def trapezoid_double(matrix, delta_x, delta_y):
    """
        Matrix at param is given in the form of 3 by 3
        [ f(x0, y0), f(x1, y0), f(x2, y0)]
        [ f(x0, y1), f(x1, y1), f(x2, y1)]
        [ f(x0, y2), f(x1, y2), f(x2, y2)]
    """

    result = 0
    for i, z_line in enumerate(matrix):
        for j, z in enumerate(z_line):
            if (i == 0 and (j == 0 or j == 2)) or (i == 2 and (j == 0 or j == 2)):
                result += z
            elif (j == 1 and (i == 0 or i == 2)) or (i == 1 and (j == 0 or j == 2)):
                result += 2*z
            else:
                result += 4*z
    return result * delta_x * delta_y / 4


def trapezoid_double_error(m, delta_x, delta_y):
    return (trapezoid_double(m, delta_x/4, delta_y/4) - trapezoid_double(m, delta_x/2, delta_y/2)) / 3


def trapezoid_double_quotient(m, delta_x, delta_y):
    qc = (trapezoid_double(m, delta_x/2, delta_y/2) - trapezoid_double(m, delta_x, delta_y))
    qc /= (trapezoid_double(m, delta_x/4, delta_y/4) - trapezoid_double(m, delta_x/2, delta_y/2))
    return qc
