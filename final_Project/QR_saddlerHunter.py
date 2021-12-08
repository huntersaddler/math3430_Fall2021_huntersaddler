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
    return B[col-1:len(matrix)]


def ele_conj(element: complex) -> complex:
    """Conjugates the elemennt given. For some reason only was working when i made it a function

        Simply returns the conjugate of an element.

        Args:
            element, the element you want to conjugate
        Returns:
            the conjugate of the element given
    """
    return element.conjugate()


def colT_mult(C: list, CT: list) -> list:
    """ Multiplies a column by its transpose for each element (originally was having issues with my inner product function
        so I wrote this)

        Creates a result vector. Then for each elemnt in the input column and transpose, multiplies each element at the
        index

        Args:
            C, a column vector
            CT, the columns transpose
        Returns:
            result, essentially the inner product of the column with its transpose
    """
    result: complex = 0
    for i in range(len(C)):
        for x in range(len(CT[0])):
            result += (CT[i][x] * C[i])
    return result


def f_builder(cV: list) -> list:
    """Creates the F matrix for the housholder eq to use in computing Q

        Computes the transpse and norm of the column, then finds F = I -2vv*/v*v using functions from LA file.
        Outputs the matrix F for the given column

        Args:
            cV, a col vector
        Returns:
            F, a matrix computed with the formula F = I -2vv*/v*v
    """
    transposecV: list = [[cV[i]] for i in range(len(cV))]
    normcV: complex = LA_saddlerHunter.vector_norm(cV)
    ui: list = LA_saddlerHunter.scal_vec_mult(normcV, (ID_build(len(transposecV)))[0])
    U1: list = LA_saddlerHunter.add_vectors(ui, LA_saddlerHunter.scal_vec_mult(-1, cV))
    tranU1: list = [[U1[i]] for i in range(len(U1))]
    VVt: list = LA_saddlerHunter.matrix_matrix_mult([U1], tranU1)
    VtV: list = colT_mult(U1, tranU1)
    F: list = LA_saddlerHunter.matrix_matrix_add(ID_build(len(VVt)), LA_saddlerHunter.scal_matrix_mult((-2/VtV), VVt))
    return F


def q_builder(matrix: list, lg: int) -> list:
    """Builds the Q vector for a given F

        Creates an ID matrix with the given size. Builds the Q matrix by inserting the input matrix into the ID matrix
        at the bottom right of the matrix. Returns e the assembled Q for the given matrix

        Args:
            matrix, the F matrix from the householder eq stored as list of col
            lg, the number of columns in the matrix
        Returns:
            e, the Q matrix of col vectors built by F matrix input
    """
    e: list = ID_build(lg)
    for i in range(1, lg):
        for j in range(len(matrix)):
            e[i][j+1] = matrix[i-1][j]
    return e


def householder(matrix: list) -> list:
    """Computes the QR decomposition for the given matrix using the hoseholder algorithm

        Finds the first iteration of Q using F_builder and uses to calculate R. Checks R to see if it is in the Upper
        right triangualar form we desire. If not, continues the householder algorithm for the next subcolumn until
        the R matrix is in Upper right form (unfortunately there is some rounding errors with the floating points so
        most of the "zeros" end up being an extremely small number so i added a crude tolerance check). When R is of the
        correct form we return Q and R

        Args:
            matrix, a list of columns
        Returns:
            Q,R the built Q matrix followed by the upper triangular matrix R
     """
    Q: list = f_builder(matrix[0])
    R: list = LA_saddlerHunter.matrix_matrix_mult(Q, matrix)
    for i in range(len(matrix) - 1):
        for j in range(i +1, len(matrix[0])):
            if -0.1 < R[i][j] < 0.01:
                continue
            else:
                sc: list = sub_col(R, j)
                if len(sc) == len(matrix):
                    H: list = f_builder(sc)
                else:
                    H: list = q_builder(f_builder(sc), len(matrix))
                Q = LA_saddlerHunter.matrix_matrix_mult(Q, H)
                R = LA_saddlerHunter.matrix_matrix_mult(H, R)
    z: list = []
    z.append(Q)
    z.append(R)
    return z
