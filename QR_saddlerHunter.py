import LA_saddlerHunter

def mat_build(M: list) -> list:
    """Builds an empty matrix with the size of the input matrix

        Creates an empty list A. Then for each element in the input matrix we add a zero to A. Returns A

        Args:
            M a matrix which is a list of column vectors
        Returns:
            A, a matrix of 0's with the same size as the input matrix
    """
    A: list = []
    for element in M:
        A.append([0 for i in range(len(M))])
    return A

def stable_gramschmidt(matrix: list)->list:
    """Finds the QR decomp of a matrix using stable gram schmidt process

        Creates a temp matrix V as a copy of the input matrix. Creates the Q and R matrices setting R to the same size
        of the input so we can index. For each column of the input matrix we find the vector norm and store it at the
        index in R. Then adds the product of the column at the index in V with 1/norm at the index in R using functions
        from my LA file. Then for each row in the column at the index we set the element at the index in R to the inner
        product of Q and V at there respective indexes, while also subtracting the product of the norm at the index with
        the column in Q at the index from V. When outer for loop terminates outputs [Q,R]

        Args:
            matrix is a list of column vectors
        Returns:
            result, which is a list containing Q and R
        """
    V: list = []
    for index in range(len(matrix)):
        V.append(matrix[index])
    R: list = mat_build(matrix)
    Q: list = []
    for col in range(len(matrix)):
        R[col][col] = LA_saddlerHunter.vector_norm(V[col])
        Q.append(LA_saddlerHunter.scal_vec_mult(1/R[col][col], V[col]))
        for row in range(col+1, len(matrix)):
            R[row][col] = LA_saddlerHunter.inner_prod(Q[col], V[row])
            V[row] = LA_saddlerHunter.add_vectors(V[row], LA_saddlerHunter.scal_vec_mult(-R[row][col], Q[col]))
    return [Q, R]

def orthonormal_basis(matrix: list) ->list:
    """Outputs a matrix of columns which are orthogonal and share the same span

        Creates a list and sets it to the stable gram schmidt of the input matrix. Returns the Q matrix of the QR decomp

        Args:
            matrix is a list of column vectors
        Returns:
            result, which is the Q from the stable gram schmidt
    """
    H: list = stable_gramschmidt(matrix)
    return H[0]


def deep_copy(matrix: list) -> list:
    """Outputs a copy of the input matrix that can be changed without changing the original

        Creates a empty list V then for each col in the input matrix we append each col to V

        Args:
             matrix is a list of column vectors
        Returns:
            V, a deep copy of matrix
    """
    V: list = []
    for index in range(len(matrix)):
        V.append(matrix[index])
    return V


def ID_build(size: int) -> list:
    """Creates an identity matrix with the given size

        Makes empty list I and c, then for each col we check if the row is equal to the col. If equal, we append 1 to c.
        else we append 0 to c. Then we append each col stored in c to I. returns I

        Args:
            size, the desired size of the id matrix
        Returns:
            I, the identity matrix
    """
    I: list = []
    for col in range(size):
        c: list = []
        for row in range(size):
            if row == col:
                c.append(1)
            else:
                c.append(0)
        I.append(c)
    return I


def sub_col(matrix: list, col: int) -> list:
    """Takes the sub col of the given matrix along the diagonol for the given col

        Creates a vector B and stores the desired col. Then deletes the numbers above until we have the desired subcol
        along the diaganol of the matrix

        Args:
            matrix, a list of col vectors
            col, the desired col to take the sub col
        Returns:
            B, the sub col along the diaganol of the input matrix
    """
    B = (matrix[(col-1)])
    for int in range(col-1):
        del B[int]
    return B


def ele_conj(element: complex) -> complex:
    """Conjugates the elemennt given. For some reason only was working when i made it a function

        Simply returns the conjugate of an element.

        Args:
            element, the element you want to conjugate
        Returns:
            the conjugate of the element given
    """
    return element.conjugate()


def conjugate_transpose(matrix: list) -> list:
    """Takes the conjugate transpose of a matrix

        Creates an empty list V then for each col in the given matrix we append the element at the given row to r. Then we
        append r to V. Returns V

        Args:
            matrix, a list of col vectors
        Returns:
            V the conjugate transpose of the given matrix
    """
    V: list = []
    for col in range(len(matrix[0])):
        r = []
        for row in range(len(matrix)):
            r.append(ele_conj(matrix[row][col]))
        V.append(r)
    return V


def f_builder(V: list) -> list:
    """Creates the F matrix for the housholder eq to use in computing Q

        Computes the transpse and inner product of V the input vector, then finds 2 * Vtranspose * V and stores as Vmulti. Then finds the difference
        between I and the negated Vmulti. Returns F

        Args:
            V, a col vector
        Returns:
            F, the result of the formula in the householder equation
    """
    transposeV: list = conjugate_transpose(V)
    innerV: complex = LA_saddlerHunter.matrix_matrix_mult(transposeV, V)[0][0]
    Vmulti: list = LA_saddlerHunter.scal_matrix_mult((2/innerV), LA_saddlerHunter.matrix_matrix_mult(V, transposeV))
    nVmulti: list = (LA_saddlerHunter.scal_matrix_mult(-1, Vmulti))
    F = LA_saddlerHunter.matrix_matrix_add(ID_build(len(Vmulti)), nVmulti)
    return F

"""Unfortunately i have broken my f builder due to an issue with how I wrote my norm functions in my LA script.
    I believe all the support functions are working correctly but i have run out of time
   
   REMINDER to finish this weekend or be in office hours on monday
"""


def q_builder(matrix: list, k: int):
    """Builds the Q vector for a given F and k the col number

        Creates and Id matrix +1 the size of the F matrix given. Then for each col in Q we check if the row and col is the same
        as k. If it is we replace that index with the corresponding index in the input matrix until we have built Q. Returns Q

        Args:
            matrix, the F matrix from the householder eq stored as list of col
            k, the col where the F matrix needs to be in Q
        Returns:
            Q, the matrix of col vectors built by F
    """

def householder(matrix: list):
    """Finds the QR orth of the given matrix and returns [Q, R]
     """
