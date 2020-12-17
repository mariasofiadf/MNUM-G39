PRECISION = 0.000001

def false_position_abs_stop(lower_limit, upper_limit, function):
    iteration = 0
    root = 0
    while abs(upper_limit - lower_limit) > PRECISION:
        iteration += 1
        root = (lower_limit * function(upper_limit) - upper_limit * function(lower_limit))
        root /= (function(upper_limit) - function(lower_limit))

        if function(lower_limit) * function(root) < 0:
            upper_limit = root
        else:
            lower_limit = root

    print(iteration)
    return root


def false_position_null_at_root(lower_limit, upper_limit, function):
    iteration = 0
    root = 0
    while abs(function(lower_limit) - function(upper_limit)) > PRECISION:
        iteration += 1
        root = lower_limit * function(upper_limit) - upper_limit * function(lower_limit)
        root /= (function(upper_limit) - function(lower_limit))

        if function(lower_limit) * function(root) < 0:
            upper_limit = root
        else:
            lower_limit = root

    print(iteration)
    return root
