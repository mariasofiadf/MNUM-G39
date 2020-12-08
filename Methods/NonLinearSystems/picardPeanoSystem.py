PRECISION = 0.0000001
"""
PicardPeano method is iterative
Important to check if the partial derivatives of the guess are less than 1
"""


# PICARD PEANO
def picard_peano_system_error(function_x, function_y, guess_x, guess_y):
    x = guess_x
    y = guess_y
    iteration = 0
    while abs(x-guess_x) >= PRECISION and abs(y-guess_y) >= PRECISION:
        guess_x = x
        guess_y = y
        x = function_x(guess_x, guess_y)
        y = function_y(guess_x, guess_y)

        iteration += 1

    print("x: {}, y: {}, iter: {}".format(x, y, iteration))


def picard_peano_system_iterations(function_x, function_y, guess_x, guess_y, max_iteration):
    for iteration in range(max_iteration):
        x = guess_x
        guess_x = function_x(guess_x, guess_y)
        guess_y = function_y(x, guess_y)

    print("x: {}, y: {}".format(guess_x, guess_y))
