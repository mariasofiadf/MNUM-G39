

def triGAUSS(aMatrix, verbose=False):
    """
    Gauss upper triangular extended matrix.

    Reduces the augmented matrix [A , b] to upper triangular form,
    with unit diagonal, using Gauus substitution.
    Arguments:
        aMatrix - augmented matrix, as a list of lists;
        verbose - True for iteration printing, default False.
    Return:
        aLocalMatrix - the triangular matrix, as a list of lists.
    """

    aLocalMatrix = aMatrix

    dimV = len(aLocalMatrix)
    for diag in range(dimV):
        # save diagonal pivot element
        pivot = aLocalMatrix[diag][diag]
        # divide diagonal line by pivot
        for col in range(dimV + 1):
            aLocalMatrix[diag][col] /= pivot
        # zero diagonal column
        for lin in range(diag + 1, dimV):
            # save factor
            factor = aLocalMatrix[lin][diag]
            for col in range(diag, dimV + 1):
                aLocalMatrix[lin][col] -= aLocalMatrix[diag][col] * factor
    if verbose:
        for diag in range(dimV):
            print(aLocalMatrix[diag])
    return aLocalMatrix


def backJordan(aMatrix, verbose=False):
    """
    Gauss-Jordan augmented [identity, solution] matrix.

    Reduces the augmented upper triangular matrix [A , b],
    obtained by triGAUSS()to to [identity, solution] form.
    Used in the order:
        >>> triGAUSS()
        >>> backJordan()
    implements Gauss-Jordan method.
    Arguments:
        aMatrix - augmented matrix, as a list of lists;
        verbose - True for iteration printing, default False.
    Return:
        the last column of the id matrix,
        as a list obtained by comprehension.
    """

    aLocalMatrix = aMatrix
    dimV = len(aLocalMatrix)
    # and now, back up!
    for diag in range(dimV - 1, - 1, - 1):
        for lin in range(diag - 1, - 1, - 1):
            factor = aLocalMatrix[lin][diag]
            for col in range(dimV, diag - 1, -1):
                aLocalMatrix[lin][col] -= aLocalMatrix[diag][col] * factor

    # a unit matrix adjointed with a solution column
    if verbose:
        for diag in range(dimV):
            print(aLocalMatrix[diag])
    # return the list of the last column values
    return [aLocalMatrix[x][dimV] for x in range(dimV)]


def residueSLE(aMatrix, solutionMatrix, verbose=False):
    """
    Residue calculation in systems of linear equations.

    Calculate the residue of a given solution in a system of LE.
    residue = independentMatrix - coefMatrix . solutionMatrix
    Arguments:
        aMatrix - augmented matrix, as a list of lists;
        solutionMatrix - solutions (column matrix);
        verbose - True for iteration printing, default False.
    Return:
        resid - residues (column matrix).
    """

    dimV = len(aMatrix)
    # checking residues
    # create a list for residues, initially filled with zeros

    resid = [0] * dimV
    for eq in range(dimV):
        for sol in range(dimV):
            resid[eq] += aMatrix[eq][sol] * solutionMatrix[sol]
        # print(mc[eq][dimV], resid[eq])
        resid[eq] = aMatrix[eq][dimV] - resid[eq]
    if verbose:
        print(resid)
    return resid