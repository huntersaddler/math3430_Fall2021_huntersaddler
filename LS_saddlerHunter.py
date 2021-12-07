import LA_saddlerHunter
import QR_saddlerHunter

def back_sub(Rmatrix: list, Dvector: list) -> list:
    """Finds the solution vector x for some system Ax = b for the given A matrix and b column vector by using the
    back substitution method.

    We calculate the first solution of the back sub method for the system which corresponds to the last row in the
    matrix and the vector. After storing the first solution, we find each of the next solutions by using the back sub
    method and the previous solutions.

    Args:
        Rmatrix: The upper triangular matrix for the system stored as a list of lists where each component list is a
        column
        Dvector: the b vector for the system stored as a list
    Returns:
        The x vector, the solution to the system Ax = b
    """
    xn: list = [Dvector[-1] * (1/Rmatrix[-1][-1])] #this is the first sol
    for i in range(len(Rmatrix)-2, -1, -1):
        ele: float = Dvector[i]
        for j in range(len(xn)):
            ele -= Rmatrix[len(Rmatrix)-1-j][i] * xn[j]
        xn.append(ele * 1/(Rmatrix[i][i]))
    xn = xn[::-1]
    return xn

def LeastSquares(Bvector: list, Amatrix: list) -> list:
    """Finds the least squares solution for the given A matrix and b solution vector with back substitution

        Finds the QR decomp for the A matrix and sets Qm and Rm to Q and R respectively. Then finds the transpose of Qm
        and multiplies Q transpose by the solution vector b to find d (d = Qtranspose * b). Then uses backsubstitution
        to find Rx = d. Returns the x in Ax = b

        Args:
            Bvector, the b column vector
            Amatrix, the A matrix for the system
        Returns:
            x, the x solution to the system for Ax = b
    """
    QandR: list = QR_saddlerHunter.householder(Amatrix)
    Qm: list = QandR[0]
    Rm: list = QandR[1]
    Qtransp: list = []
    for row in range(len(Qm[0])):
        Qtr: list = []
        for col in range(len(Qm)):
            Qtr.append(Qm[col][row])
        Qtransp.append(Qtr)
    d: list = LA_saddlerHunter.matrix_vector_mult(Bvector, Qtransp)
    x: list = back_sub(Rm, d)
    return x
