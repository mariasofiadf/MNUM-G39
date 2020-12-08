PRECISION = 0.000001
"""
First Order Method for solving differential equations
QC should be neat to 2 (2^1)
"""


def euler(diff_function, x0, y0, xf, increment, verbose=False):
    numberIterations = 0
    while abs(xf - x0) > PRECISION:
        delta_y = diff_function(x0, y0)
        x0 += increment
        y0 += increment * delta_y
        numberIterations += 1
        if verbose:
            print("It: {}, x: {}, y: {}".format(numberIterations, x0, y0))
    return y0


# NOT IMPLEMENTED
def improved_euler(diff_function, x0, y0, xf, increment, verbose=False):
    while abs(xf - x0) > PRECISION:
        delta_y = diff_function(x0, y0)
        x0 += increment
        y0 = y0 + increment * (delta_y + diff_function(x0 + increment, y0 + increment * delta_y)) / 2
        if verbose:
            print("x: {}, y: {}".format(x0, y0))
    return y0


def euler_quotient(diff_function, x0, y0, xf, increment):
    qc = euler(diff_function, x0, y0, xf, increment/2) - euler(diff_function, x0, y0, xf, increment)
    qc /= (euler(diff_function, x0, y0, xf, increment/4) - euler(diff_function, x0, y0, xf, increment/2))
    return qc


# NEED TO TEST
def euler_error(diff_function, x0, y0, xf, increment):
    return euler(diff_function, x0, y0, xf, increment/4) - euler(diff_function, x0, y0, xf, increment/2)
