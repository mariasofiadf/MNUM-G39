PRECISION = 0.01


def minimum_3d(function, gradient, point, step, verbose=False):
    point_old = [0] * len(point)
    for i in range(len(point)):
        point_old[i] = point[i]

    finished = False
    old_step = step

    while not finished:
        for i in range(len(point)):
            point[i] = point_old[i] - step * gradient(point_old[0], point_old[1], i)

        if function(point[0], point[1]) < function(point_old[0], point_old[1]):
            old_step = step
            step *= 2
            iteration = True
        elif function(point[0], point[1]) > function(point_old[0], point_old[1]):
            step = old_step
            step /= 2
            iteration = False
        else:
            raise ValueError("Plane Zone - Impossible Calculation")

        finished = True
        for i in range(len(point)):
            finished = finished and abs(point[i] - point_old[i]) < PRECISION

        if iteration:
            for i in range(len(point)):
                point_old[i] = point[i]

    if verbose:
        print(point)
        print("Value f(x, y): {}".format(function(point[0], point[1])))

    return point
