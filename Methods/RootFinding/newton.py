"""
Great Method that requires very few iterations if used in a well known function.
However we need to know the derivative of the function
"""


def newton_one_var(guess, max_iterations, function, derivative_function):
    for iteration in range(max_iterations):
        guess = guess - function(guess) / derivative_function(guess)
    return guess
