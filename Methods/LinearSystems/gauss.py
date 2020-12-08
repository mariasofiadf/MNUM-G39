

def swap_line(mtx, first_line, second_line):
    mtx[first_line], mtx[second_line] = mtx[second_line], mtx[first_line]


def sublist(lst1, lst2):
    if len(lst1) - len(lst2):
        raise Exception("Lists with different dimensions!")
    for i in range(len(lst1)):
        lst1[i] -= lst2[i]


def multiply_scalar(lst, scalar):
    return [lst[i] * scalar for i in range(len(lst))]


def vector_product(lst1, lst2):
    result = 0
    for i in range(len(lst1)):
        result += lst1[i] * lst2[i]
    return result


def gauss(coef_matrix, ind_matrix):
    dim = len(ind_matrix)

    for i, line in enumerate(coef_matrix):
        if abs(line[0]) == 1 and i == 0:
            break
        elif abs(line[0]) == 1:
            swap_line(coef_matrix, 0, i)
            swap_line(ind_matrix, 0, i)
            break

    for j in range(len(coef_matrix) - 1):
        for i in range(j + 1, len(coef_matrix)):
            a = coef_matrix[i][j] / coef_matrix[j][j]
            sublist(coef_matrix[i], multiply_scalar(coef_matrix[j], a))
            ind_matrix[i] -= a*ind_matrix[j]

            b = 1 / coef_matrix[i][j+1]
            coef_matrix[i] = multiply_scalar(coef_matrix[i], b)
            ind_matrix[i] *= b

    for j in range(len(coef_matrix) - 1):
        for i in range(j + 1, len(coef_matrix)):
            a = coef_matrix[dim-1-i][dim-1-j] / coef_matrix[dim-1-j][dim-1-j]
            sublist(coef_matrix[dim-1-i], multiply_scalar(coef_matrix[dim-1-j], a))
            ind_matrix[dim-1-i] -= a*ind_matrix[dim-1-j]

            b = 1 / coef_matrix[dim-1-i][dim-1-j-1]
            coef_matrix[dim-1-i] = multiply_scalar(coef_matrix[dim-1-i], b)
            ind_matrix[dim-1-i] *= b