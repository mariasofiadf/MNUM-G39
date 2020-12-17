PRECISION = 0.000001
"""
First Order Method for solving differential equations
QC should be neat to 2 (2^1)
"""


def euler(diff_function, x0, y0, xf, increment, verbose=False):
    iterations = 0
    result = [[x0, y0]]

    while abs(xf - x0) > PRECISION:
        delta_y = diff_function(x0, y0)
        x0 += increment
        y0 += increment * delta_y

        iterations += 1
        result.append([x0, y0])

        if verbose:
            print("It: {}, x: {}, y: {}".format(iterations, x0, y0))
    return result


def euler_quotient(diff_function, x0, y0, xf, increment):
    qc = euler(diff_function, x0, y0, xf, increment/2)[-1][-1] - euler(diff_function, x0, y0, xf, increment)[-1][-1]
    qc /= (euler(diff_function, x0, y0, xf, increment/4)[-1][-1] - euler(diff_function, x0, y0, xf, increment/2)[-1][-1])
    return qc


def euler_error(diff_function, x0, y0, xf, increment):
    return euler(diff_function, x0, y0, xf, increment/4)[-1][-1] - euler(diff_function, x0, y0, xf, increment/2)[-1][-1]
