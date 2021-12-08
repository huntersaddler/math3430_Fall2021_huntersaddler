import LA_saddlerHunter
import LS_saddlerHunter
import QR_saddlerHunter
import LS_saddlerHunter

print("""Hello, I am Hunter Saddler and this is my linear algebra library. This project is for my
computational techniques class. The library is a collection of three files, LA, QR, and
Ls containing various linear algebra algorithms.
""")
print("""LA_saddlerHunter.py is a collection of basic linear algebra functions used as a base for the project.
All functions are written to only accept matrices which are stored as lists of lists, where each
component list represents a column of the matrix.
""")
print("""
The first function, add_vectors(list, list), takes two vectors stored as lists for inputs and returns
their sum.
""")
print("""For the inputs a = [1, 2, 4] and b = [3, 1, 2], add_vectors(a, b) will return""")
a: list = [1, 2, 4]
b: list = [3, 1, 2]
print(LA_saddlerHunter.add_vectors(a, b))
print("""
The second function, scal_vec_mult(int, list), takes a scalar and a vector stored as a list for inputs and 
returns their product.
""")
print("""For the inputs a = 2 and b = [4, 3, 1], scal_vec_mult(a, b) will return""")
a: int = 2
b: list = [4, 3, 1]
print(LA_saddlerHunter.scal_vec_mult(a, b))
print("""
The third function, scal_matrix_mult(int, list), takes a scalar and a matrix for inputs and returns their 
product.
""")
print("""For the inputs a = 2 and b = [[2, 3], [6, 1], [4, 3]], scal_matrix_mult(a, b) will return""")
b: list = [[2, 3], [6, 1], [4, 3]]
a: int = 2
print(LA_saddlerHunter.scal_matrix_mult(a, b))
print("""
The fourth function, matrix_matrix_add(list, list), takes two matrices for inputs and returns their sum.
""")
print("""For the inputs a = [[1, 1], [2, 2], [3, 3]] and b = [[1, 2], [1, 2], [1, 2]], matrix_matrix_add(a, b)
will return""")
a: list = [[1, 1], [2, 2], [3, 3]]
b: list = [[1, 2], [1, 2], [1, 2]]
print(LA_saddlerHunter.matrix_matrix_add(a, b))
print("""
The fifth function, matrix_vector_mult(list, list) takes a vector and a matrix for inputs and returns their
product.
""")
print("""For the inputs a = [5, -1, 0] b = [[3, 1], [4, 3], [-1, 2]], matrix_vector_mult(a, b) will return""")
a: list = [5, -1, 0]
b: list = [[3, 1], [4, 3], [-1, 2]]
print(LA_saddlerHunter.matrix_vector_mult(a, b))
print("""
For the sixth function, matrix_matrix_mult(list, list) takes two matrices for input and returns their 
product.
""")
print("""For the inputs a = [[3, 1], [4, 3], [-1, 2]] and b = [[5, -1, 0], [2, 4, 3]], matrix_matrix_mult(a, b)
will return""")
a: list = [[3, 1], [4, 3], [-1, 2]]
b: list = [[5, -1, 0], [2, 4, 3]]
print(LA_saddlerHunter.matrix_matrix_mult(a, b))
print("""
The seventh function, absolute_val(complex), takes any number for input and returns its absolute value.
""")
print("""For the input a = 2+3j, absolute_val(a) will return""")
a: complex = 2+3j
print(LA_saddlerHunter.absolute_val(a))
print("""
The eighth function, vector_norm(list), takes a vector and an int set to p = 2 by default for input and returns the 
p-norm of the vector.
""")
print("""For the input a = [1, 2, 3, 4], vector_norm(a, 2) will return""")
a: list = [1, 2, 3, 4]
print(LA_saddlerHunter.vector_norm(a, 2))
print("""
The ninth function, infinity_norm(list), takes a vector for input and returns the infinity norm of the vector.
""")
print("""For the input a = [1, 2, 3, 4, 5, -6], infinity_norm(a) will return""")
a: list = [1, 2, 3, 4, 5, -6]
print(LA_saddlerHunter.infinity_norm(a))
print("""
The tenth function, any_norm(list, int, bool), takes a vector, an int set by default p=2 and a boolean set by defualt
to FALSE for inputs. If boolean input is given as TRUE, the function returns the infinity norm of the vector. If the
boolean input is FALSE or no boolean input is given, the function returns the p norm of the vector.
""")
print("""For the input vector a = [12, -22, 3, 44] with p and boolean inputs left to defualt, any_norm(a) will return""")
a: list = [12, -22, 3, 44]
print(LA_saddlerHunter.any_norm(a))
print("""
The final function in my LA.saddlerHunter file, inner_prod(list, list), takes two vectors for inputs and returns their
inner product.
""")
print("""For the inputs a = [1, 2, 3] b = [4, 5, 6], inner_prod(a, b) will return""")
a: list = [1, 2, 3]
b: list = [4, 5, 6]
print(LA_saddlerHunter.inner_prod(a, b))
print("""
QR_saddlerHunter.py is a collection of functions with the end goal to calculate the QR decomposition by using either the
stable gram schmidt algorithm, or the more commonly used householder algorithm. Just like my LA file, QR is built to
accept matrices as inputs only if they are stored as a list of lists, where each component list represents a column of
the matrix.
""")
print("""
The first function in QR_saddlerHunter, mat_build(list), takes a matrix for its input and returns a matrix
filled with 0's with the same number of columns as the input matrix.
""")
print("""For the input a = [[3, 1, 9], [4, 3, 6], [-1, 2, 3]], mat_build(a) returns""")
a: list = [[3, 1, 9], [4, 3, 6], [-1, 2, 3]]
print(QR_saddlerHunter.mat_build(a))
print("""
The second function, stable_gramschmidt(list), takes a matrix for its input and returns Q an orthonormal basis, and R
the upper-triangular matrix for the QR decomposition using the stable gram schmidt algorithm. Sometimes with rounding
errors, elements that should be zero return as some very small number.
""")
print("""For the input a = [[1,1,0],[1,0,1],[0,1,1]], stable_gramschmidt(a) will return Q followed by R such as""")
a: list = [[1, 1, 0],[1, 0, 1],[0, 1, 1]]
print(QR_saddlerHunter.stable_gramschmidt(a))
print("""
The third function, othonormal_basis(list), takes a matrix as its input and returns a orthonormal basis for the given 
matrix.
""")
print("""For the input a = [[1,1,0],[1,0,1],[0,1,1]], orthonormal_basis(a) will return""")
print(QR_saddlerHunter.orthonormal_basis(a))
print("""
The fourth function, deep_copy(list), takes a matrix for its input and returns a complete copy of the input matrix that
does not affect the original matrix when changed,
""")
print("""For the input a = [[5, -1, 0], [2, 4, 3]], deep_copy(a) will return""")
a: list = [[5, -1, 0], [2, 4, 3]]
print(QR_saddlerHunter.deep_copy(a))
print("""
The fifth function, ID_build(int), takes an integer for its input and returns a square identity matrix with dimensions
equal to the given integer
""")
print("""For the input a = 3, ID_build(a) will return""")
print(QR_saddlerHunter.ID_build(3))
print("""
The sixth function, sub_col(list, int), takes a matrix and an integer as its inputs and returns the sub column of the 
matrix for the column along the diagonal at the integer given.
""")
print("""For the input a = [[1, 2, 4], [3, 4, 1], [1, 1, 7]] and b = 2, sub_col(a, b) will return""")
a: list = [[1, 2, 4], [3, 4, 1], [1, 1, 7]]
print(QR_saddlerHunter.sub_col(a, 2))
print("""
The seventh function, ele_conj(complex), takes any number as its input and returns its complex conjugation
""")
print("""For the input a = 1 + 2j, ele_conj(a) will return""")
print(QR_saddlerHunter.ele_conj(1 + 2j))
print("""
The eighth function, colT_mult(list, list), takes two vectors for its inputs and returns the first input multiplied by
the second. This function was originally going to take a column and transpose it and multiply it with itself, but the 
function got integrated into other functions.
""")
print("""For the inputs a = [1, 1, 0] and b = [[1], [1], [0]] will return""")
a: list = [1, 1, 0]
b: list = [[1], [1], [0]]
print(QR_saddlerHunter.colT_mult(a, b))
print("""
The ninth function, f_builder(list), takes a vector as its input and returns the matrix F where F = I -2vv*/v*v
for the given vector v.
""")
print("""For the input a = [-1, 2, -1], f_bulder(a) will return""")
a: list = [-1, 1, -1]
print(QR_saddlerHunter.f_builder(a))
print("""
The tenth function, q_builder(list, int), takes a matrix and an integer for its inputs and returns a Q matrix for a 
given f with size being equal to the integer input.
""")
print("""For the inputs a = [[0.9659, 0.2588], [0.2588, -0.9659]] and b = 3, q_builder(a, b) will return""")
a: list = [[0.9659, 0.2588], [0.2588, -0.9659]]
b: list = 3
print(QR_saddlerHunter.q_builder(a, b))
print("""
The final function in my QR_saddlerHunter file is the householder algorithm. householder(list), takes a matrix as its
input and returns the Q followed by R by for the QR decomposition for the given matrix. Note: Sometimes when elements
should be equal to zero, they end up being some very small number due to rounding errors with the algorithm.
""")
print("""For the input a = [[-1, 1, -1], [-1, 3, -1], [1, 3, 5]], householder(a) will return""")
a: list = [[-1, 1, -1], [-1, 3, -1], [1, 3, 5]]
print(QR_saddlerHunter.householder(a))
print("""
LS_saddlerHunter.py consists of two functions; the first for implementing back substitution and the second for computing
the least squares solution for a given system, using the QR decomposition method.
""")
print("""
The first function, back_sub(list, list), takes a matrix followed by a vector as its input and returns x, the solution
for the system Ax = b by using the back substitution method.
""")
print("""For the input a = [[1, 0, 0], [2, -4, 0], [1, 1, 2]] and b = [5, 2, -4], back_sub(a, b) will return""")
a: list = [[1, 0, 0], [2, -4, 0], [1, 1, 2]]
b: list = [5, 2, -4]
print(LS_saddlerHunter.back_sub(a, b))
print("""
For the final function in my library, LeastSquares(list, list), takes a vector followed by a matrix as its inputs and
returns the Least Squares solution for the given A matrix and b vector using its QR decomposition.
""")
print("""For the input a = [[1, 2], [1, 3]] and b = [5, 7], LeastSquares(b, a) will return""")
a: list = [[1, 2], [1, 3]]
b: list = [5, 7]
print(LS_saddlerHunter.LeastSquares(b, a))
print("""
And with the least squares algorithm being the point that we have been building towards for this semester, this
concludes my basic linear algebra library. Hopefully in the future I can go back and make this demo a little cleaner
and possibly a little interactive.
""")