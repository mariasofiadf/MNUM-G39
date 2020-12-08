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


def bissection_consecutive_stops(lower_limit, upper_limit, function):
    iteration = 0
    lower_aux = 0
    upper_aux = 1
    while abs(lower_aux - upper_aux) > PRECISION:
        iteration += 1
        upper_aux = lower_aux
        lower_aux = lower_limit * function(upper_limit) - upper_limit * function(lower_limit)
        lower_aux /= (function(upper_limit) - function(lower_limit))

        if function(lower_limit) * function(lower_aux) < 0:
            upper_limit = lower_aux
        else:
            lower_limit = lower_aux

    print(iteration)
    return lower_aux
