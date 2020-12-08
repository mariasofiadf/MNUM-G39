PRECISION = 0.000001

"""
Gauss Seidel is very similar to picardPeano system, however it has less iterations
because we use the most recent value of x to calculate y
"""
def gauss_seidel_system_error(function_x, function_y, guess_x, guess_y):
    x = guess_x
    y = guess_y
    iteration = 0
    while abs(x-guess_x) >= PRECISION and abs(y-guess_y) >= PRECISION:
        guess_x = x
        guess_y = y
        x = function_x(guess_x, guess_y)
        y = function_y(x, guess_y)

        iteration += 1

    print("x: {}, y: {}, iter: {}".format(x, y, iteration))


def gauss_seidel_system_iterations(function_x, function_y, guess_x, guess_y, max_iteration):
    for iteration in range(max_iteration):
        x = guess_x
        guess_x = function_x(guess_x, guess_y)
        guess_y = function_y(guess_x, guess_y)

    print("x: {}, y: {}".format(guess_x, guess_y))