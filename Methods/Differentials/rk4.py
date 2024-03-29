PRECISION = 0.000001
"""
Fourth Order Method for solving differential equations
QC should be neat to 16 (2^4)
"""


def rk4(diff_function, x0, y0, xf, increment, verbose=False):
    iterations = 0
    result = [[x0, y0]]
    while abs(xf - x0) > PRECISION:
        delta_1 = increment * diff_function(x0, y0)
        delta_2 = increment * diff_function(x0 + increment/2, y0 + delta_1/2)
        delta_3 = increment * diff_function(x0 + increment/2, y0 + delta_2/2)
        delta_4 = increment * diff_function(x0 + increment, y0 + delta_3)

        x0 += increment
        y0 += delta_1/6 + delta_2/3 + delta_3/3 + delta_4/6

        iterations += 1
        result.append([x0, y0])

        if verbose:
            print("It: {}, x: {}, y: {}".format(iterations, x0, y0))
    return result


def rk4_quotient(diff_function, x0, y0, xf, increment):
    qc = rk4(diff_function, x0, y0, xf, increment / 2)[-1][-1] - rk4(diff_function, x0, y0, xf, increment)[-1][-1]
    qc /= (rk4(diff_function, x0, y0, xf, increment / 4)[-1][-1] - rk4(diff_function, x0, y0, xf, increment / 2)[-1][-1])
    return qc


def rk4_error(diff_function, x0, y0, xf, increment):
    return (rk4(diff_function, x0, y0, xf, increment/4)[-1][-1]-rk4(diff_function, x0, y0, xf, increment/2)[-1][-1])/15
