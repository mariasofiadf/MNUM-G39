"""
    Quociente de Convergência tem de ser próximo de 16 para uma boa aproximação
    Método de Quarta ordem que usa parábolas
    Não é possível de ser utilizado quando o n_iterações é ímpar
"""


def simpson(lower_limit, upper_limit, function, iterations):
    if iterations % 2:
        raise ValueError("Invalid number of Iterations")

    step = (upper_limit - lower_limit) / iterations
    result = function(upper_limit) + function(lower_limit)
    n_iterations = iterations

    # calculation
    while n_iterations > 0:
        if n_iterations % 2:
            result += 4 * function(lower_limit + n_iterations * step)
        else:
            result += 2 * function(lower_limit + n_iterations * step)
        n_iterations -= 1

    result *= step / 3
    return result


def simpson_quotient(lower_limit, upper_limit, function, iterations):
    qc = simpson(lower_limit, upper_limit, function, 2*iterations) - simpson(lower_limit, upper_limit, function, iterations)
    qc /= simpson(lower_limit, upper_limit, function, 4 * iterations) - simpson(lower_limit, upper_limit, function, 2*iterations)
    return qc


def simpson_error(lower_limit, upper_limit, function, iterations):
    return simpson(lower_limit, upper_limit, function, 4*iterations) - simpson(lower_limit, upper_limit, function, 2*iterations)