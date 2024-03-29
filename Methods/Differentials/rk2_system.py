PRECISION = 0.000001


# VER AS VARIÁVEIS INDEPENDENTES E DEPENDENTES
def rk2_system(d_function1, d_function2, x0, y0, z0, xf, increment, verbose=False):
    iterations = 0
    result = [[x0, y0, z0]]

    if (verbose):
        print("It: {}, x: {}, y: {}, z:{}".format(iterations, x0, y0, z0))

    while abs(xf - x0) > PRECISION:
        temp_x, temp_y, temp_z = x0, y0, z0
        x0 += increment
        y0 += increment * d_function1(temp_x + increment/2, temp_y+increment/2*d_function1(temp_x, temp_y, temp_z), temp_z+increment/2*d_function2(temp_x, temp_y, temp_z))
        z0 += increment * d_function2(temp_x + increment/2, temp_y+increment/2*d_function1(temp_x, temp_y, temp_z), temp_z+increment/2*d_function2(temp_x, temp_y, temp_z))

        iterations += 1
        result.append([x0, y0, z0])

        if verbose:
            print("It: {}, x: {}, y: {}, z:{}".format(iterations, x0, y0, z0))
    return result


def rk2_qc(d_function1, d_function2, x0, y0, z0, xf, increment):
    error_0 = rk2_system(d_function1, d_function2, x0, y0, z0, xf, increment)[-1][1:]
    error_1 = rk2_system(d_function1, d_function2, x0, y0, z0, xf, increment/2)[-1][1:]
    error_2 = rk2_system(d_function1, d_function2, x0, y0, z0, xf, increment/4)[-1][1:]
    er = [0]*2
    for i in range(len(er)):
        er[i] = (error_1[i] - error_0[i]) / (error_2[i] - error_1[i])
    return er


def rk2_system_error(d_function1, d_function2, x0, y0, z0, xf, increment):
    error_1 = rk2_system(d_function1, d_function2, x0, y0, z0, xf, increment/2)[-1][1:]
    error_2 = rk2_system(d_function1, d_function2, x0, y0, z0, xf, increment/4)[-1][1:]
    er = [err2 - err1 for err2, err1 in zip(error_2, error_1)]
    for i in range(len(er)):
        er[i] /= 3
    return er
