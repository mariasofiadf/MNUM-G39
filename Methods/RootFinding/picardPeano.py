"""
Derivative of the function must be less than 1 in the guess.
Otherwise the function ust be rewritten until it matches the condition
"""

def picard_peano(guess, max_iterations, function, derivative_function):
    if derivative_function(guess) > 1:
        raise ValueError("Not convergent!")
    for iteration in range(max_iterations):
        guess = function(guess)
    return guess
