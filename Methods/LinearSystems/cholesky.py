

def sum(U, L, i, j, first, second):
    result = 0
    if first:
        for k in range(j):
            result += L[i][k] * U[k][j]
    elif second:
        for k in range(i):
            result += L[i][k] * U[k][j]
    return result


def empty(dim):
    res = [[0]*dim]*dim
    for i in range(dim):
        for j in range(dim):
            if i == j:
                res[i][j] = 1
    return res


def cholesky(A, b):
    L = empty(len(A))
    U = empty(len(A))

    for k in range(len(A)):
        for i in range(len(A)):
            if i >= k:
                L[i][k] = A[i][k] - sum(U, L, i, k, True, False)
        for j in range(len(A)):
            if k < j:
                U[k][j] = (A[k][j] - sum(U, L, k, j, False, True)) / L[k][k]

    sol = []
    solutions = [0]*len(A)

    for i in range(len(A)):
        total_sum = 0
        for j in range(i):
            total_sum += L[i][j] * sol[j]
        sol.append((b[i]-total_sum) / L[i][i])

    for i in range(len(A)-1, -1, -1):
        total_sum = 0
        for j in range(i+1, len(A)):
            total_sum += U[i][j] * solutions[j]
        solutions[i] = (sol[i] - total_sum) / U[i][i]

    return solutions
