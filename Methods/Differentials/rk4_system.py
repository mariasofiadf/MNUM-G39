PRECISION = 0.000001


# VER AS VARIÁVEIS INDEPENDENTES E DEPENDENTES
def rk4_system(dfunction1, dfunction2, x0, y0, z0, xf, increment, verbose=False):
    while abs(xf - x0) > PRECISION:
        delta_1_y = increment * dfunction1(x0, y0, z0)
        delta_1_z = increment * dfunction2(x0, y0, z0)

        delta_2_y = increment * dfunction1(x0 + increment/2, y0 + delta_1_y/2, z0 + delta_1_z/2)
        delta_2_z = increment * dfunction2(x0 + increment/2, y0 + delta_1_y/2, z0 + delta_1_z/2)

        delta_3_y = increment * dfunction1(x0 + increment/2, y0 + delta_2_y/2, z0 + delta_2_z/2)
        delta_3_z = increment * dfunction2(x0 + increment/2, y0 + delta_2_y/2, z0 + delta_2_z/2)

        delta_4_y = increment * dfunction1(x0 + increment, y0 + delta_3_y, z0 + delta_3_z)
        delta_4_z = increment * dfunction2(x0 + increment, y0 + delta_3_y, z0 + delta_3_z)

        y0 += delta_1_y/6 + delta_2_y/3 + delta_3_y/3 + delta_4_y/6
        z0 += delta_1_z/6 + delta_2_z/3 + delta_3_z/3 + delta_4_z/6
        x0 += increment
        if verbose:
            print("x: {}, y: {}, z:{}".format(x0, y0, z0))
    return [y0, z0]


def rk4_qc(d_function1, d_function2, x0, y0, z0, xf, increment):
    error_0 = rk4_system(d_function1, d_function2, x0, y0, z0, xf, increment)
    error_1 = rk4_system(d_function1, d_function2, x0, y0, z0, xf, increment/2)
    error_2 = rk4_system(d_function1, d_function2, x0, y0, z0, xf, increment/4)
    er = [0]*2
    for i in range(len(er)):
        er[i] = (error_1[i] - error_0[i]) / (error_2[i] - error_1[i])
    return er


def rk4_system_error(d_function1, d_function2, x0, y0, z0, xf, increment):
    error_1 = rk4_system(d_function1, d_function2, x0, y0, z0, xf, increment/2)
    error_2 = rk4_system(d_function1, d_function2, x0, y0, z0, xf, increment/4)
    er = [err2 - err1 for err2, err1 in zip(error_2, error_1)]
    for i in range(len(er)):
        er[i] /= 15
    return er
