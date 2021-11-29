import LA_saddlerHunter
import QR_saddlerHunter

"""I have confused my self with my iterations. Unfortunately my back sub is not working and it is time to submit. I will
update my github soon as it works but wanted to get something turned in"""

def back_sub(Rmatrix: list, Dvector: list) -> list:
    xi: list = []
    xn: float = Dvector[len(Dvector)-1] * (1/Rmatrix[len(Rmatrix)-1][len(Rmatrix)-1]) #this is the first sol
    xi.append(xn)
    for i in range(len(Rmatrix)-2, -1, -1):
        summ: float = 0
        for j in range(len(Rmatrix[i])-1, 0, -1):
            print(i,j)
            print(Rmatrix[i][j])
            print(xi[i-1])
            summ = summ + (Rmatrix[i][j] * xi[i-1])
            print(Rmatrix[i][j] * xi[i-1])
        xi.append((Dvector[i] - summ) * (1/Rmatrix[i][i]))
        """print(summ)
        print(Dvector[i])
        print(Dvector[i] - summ)"""
        """need to print in reverse since i am appending the last value first"""
    return xi

plsm: list = [[1, 0, 0], [2, -4, 0], [1, 1, 2]]
bm: list = [5, 2, -4]
print(back_sub(plsm, bm))






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
    Qtransp: list = [[Qm[i]] for i in range(len(Qm))]
    d: list = LA_saddlerHunter.matrix_vector_mult(Bvector, Qtransp)
    x: list = back_sub(Rm, d)
    return x
