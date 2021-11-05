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