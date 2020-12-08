"""
Método dos trapézio - método de 2a ordem
Quociente de convergência perto de 4 (arredondado)
"""


def trapezoid(lower_limit, upper_limit, function, iterations):
    step = (upper_limit - lower_limit) / iterations
    result = function(upper_limit) + function(lower_limit)
    n_iterations = iterations

    # calculation
    while n_iterations > 0:
        result += 2 * function(lower_limit + n_iterations * step)
        n_iterations -= 1

    result *= step / 3
    return result


def trapezoid_quotient(lower_limit, upper_limit, function, iterations):
    qc = trapezoid(lower_limit, upper_limit, function, 2*iterations)-trapezoid(lower_limit, upper_limit, function, iterations)
    qc /= trapezoid(lower_limit, upper_limit, function, 4*iterations)-trapezoid(lower_limit, upper_limit, function, 2*iterations)
    return qc


def trapezoid_error(lower_limit, upper_limit, function, iterations):
    return trapezoid(lower_limit, upper_limit, function, 4*iterations) - trapezoid(lower_limit, upper_limit, function, 2*iterations)