from math import sqrt

# CONSTANTS
PRECISION = 0.0001
B = (sqrt(5) - 1) / 2
A = B * B


def minimum_2d(function, x1, x2, verbose=False):
    while abs(x1-x2) > PRECISION:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)

        if function(x3) < function(x4):
            x2 = x4  # x1 stays the same
        else:
            x1 = x3  # x2 stays the same

    if verbose:
        print("min: {}".format(min(x1, x2, x3, x4)))
    return min(x1, x2, x3, x4)


def maximum_2d(function, x1, x2, verbose=False):
    while abs(x1 - x2) > PRECISION:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)

        if function(x3) > function(x4):
            x2 = x4  # x2 stays the same
        else:
            x1 = x3  # x1 stays the same

    if verbose:
        print("max: {}".format(max(x1, x2, x3, x4)))
    return max(x1, x2, x3, x4)
