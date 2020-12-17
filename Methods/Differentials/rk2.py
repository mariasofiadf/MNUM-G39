PRECISION = 0.000001
"""
Second Order Method for solving differential equations
QC should be neat to 4 (2^2)
"""


def rk2(diff_function, x0, y0, xf, increment, verbose=False):
    iterations = 0
    result = [[x0, y0]]
    while abs(xf - x0) > PRECISION:
        temp_x, temp_y = x0, y0
        x0 = temp_x + increment
        y0 = temp_y+increment*diff_function(temp_x + increment/2, temp_y + increment/2 * diff_function(temp_x, temp_y))

        result.append([x0, y0])
        iterations += 1

        if verbose:
            print("It: {}, x: {}, y: {}".format(iterations, x0, y0))
    return result


def rk2_quotient(diff_function, x0, y0, xf, increment):
    qc = rk2(diff_function, x0, y0, xf, increment / 2)[-1][-1] - rk2(diff_function, x0, y0, xf, increment)[-1][-1]
    qc /= (rk2(diff_function, x0, y0, xf, increment / 4)[-1][-1] - rk2(diff_function, x0, y0, xf, increment / 2)[-1][-1])
    return qc


def rk2_error(diff_function, x0, y0, xf, increment):
    return (rk2(diff_function, x0, y0, xf, increment/4)[-1][-1] - rk2(diff_function, x0, y0, xf, increment/2)[-1][-1])/3
