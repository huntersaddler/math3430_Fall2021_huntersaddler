"""
This homework is due on 10/15/2021 by 11:59pm. 


For this assignment you will be writing a python script to be named LA.py. In
this script you will need to write 6 functions. Every function must 

1) Have a doc string.

2) Have type annotations

3) Be tested using unit testing. 

Once you have finished writing LA.py you will upload it to the same github repo
you used for HW02. The functions you need to write are 

#0 A function which takes as it's arguments two vectors stored as
lists and returns their sum, also stored as a list.


#1 A function which takes as it's arguments a vector stored as a list and a
scalar, and returns the scalar vector multiplication stored as a list.


#2 A function which takes as it's arguments a matrix, stored as a list of lists
where each component list represents a column of the matrix(you cannot represent
the matrix as a list of rows!) and a scalar and returns their product, also
stored as a list of lists where each component list represents a column. You
must use the function from problem #1. Failure to use this function will result
in an earned grade of 0.

#3 A function which takes as it's arguments two matrices stored as lists of
lists where each component list represents a column vector, and returns their
sum stored in the same manner. You must use the function in problem #0 in your
method here. Failure to use the function from problem #0 will reuslt in an
earned grade of 0.

#4 A function which takes as it's argument a matrix (stored as a list of lists,
each component list representing a column vector), and a vector stored as a
list, and returns the matrix-vector product. This function must compute the
matrix-vector product by calculating the neccessary linear combination of the
input matrices columns. All other methods of matrix-vector multiplication are
strictly forbidden and their use will result in a grade of 0. For this function
you must use the functions written for problem #0 and problem #1. Failure to use
these functions will result in an earned grade of 0.

#5 A function which takes as it's arguments two matrices, each stored as a list
of lists where each component list represents a column vector, and returns their
product stored in the same manner. To earn any credit on this problem you must
use the function from problem #4 to implement the matrix-vector method of
matrix-matrix multiplication. Use of any other method will result in an earned
grade of 0.
"""


# Begin Example
# Problem #0

def add_vectors(vector_a: list[float],
                vector_b: list[float]):
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result: list = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result

# End Example

#Problem 1
"""
   Multiplies the input vector by the scalar input

   Creates a result vector stored as a list of 0's the same length as the input vector. Then using a for loop over length of 
   result, replaces the 0's in result with the product of input v1_a at that index with the scaler input sc1_a

   Args:
       sc1_a: A scalar stored as int
       v1_a: A vector stored as a list representing a column of a matrix

    Returns:
       The product of the scalar and vector stored as a list
   """

def scal_vec_mult(sc1_a: int, v1_a: list):
   result: list = [0 for element in v1_a]
   for index in range(len(result)):
    result[index] = sc1_a * v1_a[index]
   return result



#Problem 2
"""
   Multiplies the input vector by the matrix input using scal_vector_mult()

   Creates a result matrix stored as a list of 0's the same length as the input matrix. Then using a for loop over length of 
   result, replaces the 0's in result with the product of input m2_a at that index with the scaler input sc2_a

   Args:
       sc2_a: A scalar stored as int
       m2_a: A matrix stored as a list of lists with each list being a column in the matrix

    Returns:
       The product of the scalar and matrix stored as a matrix(list of list)
   """

def scal_matrix_mult(sc2_a: int, m2_a: list):
  result: list = [0 for element in m2_a]
  for index in range(len(result)):
    result[index] = scal_vec_mult(sc2_a, m2_a[index])
  return result




#Problem 3
"""
   Adds the two input matrices

   Creates a result matrix stored as a list of 0's the same length as the input matrices. Then using a for loop over length of 
   result, replaces the 0's in result with the sum of input m3_a at that index with the input m3_b at that index

   Args:
       m3_a: A matrix stored as a list of lists with each list being a column in the matrix m3_a
       m3_b: A matrix stored as a list of lists with each list being a column in the matrix m3_b

    Returns:
       The sum of the two matrices stored as a matrix(list of list)
   """

def matrix_matrix_add(m3_a: list, m3_b: list):
  result: list = [0 for element in m3_a]
  for index in range(len(result)):
    result[index] = add_vectors(m3_a[index], m3_b[index])
  return result




#Problem 4
"""
   Multiplies the vector input and the matrix input

   Creates a result matrix stored as a list of 0's the same length as a column in the input matrix. Then using a for loop 
   over length of input vector, finds the product of input m4_a at that index 
   with the input v4_a at that index, and adds it to the result using add_vectors()

   Args:
       v4_a: A vector stored as a list of floats
       m4_a: A matrix stored as a list of lists with each list being a column in the matrix m4_a

    Returns:
       The product of the input vector and the input matrix stored as a matrix(list of list)
   """

def matrix_vector_mult(v4_a: list, m4_a: list):
  result: list = [0 for element in m4_a[1]]
  for index in range(len(v4_a)):
    result = add_vectors(result, scal_vec_mult(v4_a[index], m4_a[index]))
  return result




#Problem 5
"""
   Multiplies two input matrices using the linear combination of columns method

   Creates a result matrix stored as a list of 0's the same length as the input matrix m5_b. Then using a for loop 
   over length of m5_b, finds the product of input m5_a at that index with the input m5_b at that index using 
   matrix_vect_mult() and adds it to the result matrix

   Args:
       m5_a: A matrix stored as a list of lsts with each list being a column in matrix m5_a. This input must be the matrix
       with more rows if not square
       
       m4_a: A matrix stored as a list of lists with each list being a column in the matrix m5_b. This input must be the
       matrix with more columns if not square

    Returns:
       The product of the two input matrices stored as a matrix(list of list)
   """

def matrix_matrix_mult(m5_a: list, m5_b: list):
  result: list = [0 for element in m5_b]
  for index in range(len(m5_b)):
    result[index] = matrix_vector_mult(m5_b[index], m5_a)
  return result


"""Test functions"""

import pytest

def test_zero_add_vectors():
    test_vector_01: list = [1, 2, 4]
    test_vector_02: list = [3, 1, 2]

    assert add_vectors(test_vector_01, test_vector_02) == [4, 3, 6]
    assert add_vectors(test_vector_01, [0, 0, 0]) == [1, 2, 4]

def test_one_scal_vect_mult():
    testv_1a: list = [4, 3, 1]
    tests_1a: int = 2
    testv_1b: list = [3, 0, 10, 111]
    tests_1b: int = 3

    assert scal_vec_mult(tests_1a, testv_1a) == [8, 6, 2]
    assert scal_vec_mult(tests_1b, testv_1b) == [9, 0, 30, 333]

def test_two_scal_matrix_mult():
    testm_2a: list = [[2, 3], [6, 1], [4, 3]]
    tests_2a: int = 2
    testm_2b: list = [[1, 2], [3, 3], [0, 0], [0, 111]]
    tests_2b: int = 3

    assert scal_matrix_mult(tests_2a, testm_2a) == [[4, 6], [12, 2], [8, 6]]
    assert scal_matrix_mult(tests_2b, testm_2b) == [[3, 6], [9, 9], [0, 0], [0, 333]]

def test_three_matrix_matrix_add():
    testm_3a: list = [[1, 1], [2, 2], [3, 3]]
    testm_3b: list = [[1, 2], [1, 2], [1, 2]]
    testm_3c: list = [[1, 0], [7, 1], [29, 3], [100, 100]]
    testm_3d: list = [[1, 2], [1, 2], [1, 2], [100, 100]]

    assert matrix_matrix_add(testm_3a, testm_3b) == [[2, 3], [3, 4], [4, 5]]
    assert matrix_matrix_add(testm_3c, testm_3d) == [[2, 2], [8, 3], [30, 5], [200, 200]]

def test_four_matrix_vector_mult():
    testv_4a: list = [5, -1, 0]
    testm_4a: list = [[3, 1], [4, 3], [-1, 2]]
    testv_4b: list = [1, 3, 4]
    testm_4b: list = [[1, 3], [1, 2], [1, 2]]

    assert matrix_vector_mult(testv_4a, testm_4a) == [11, 2]
    assert matrix_vector_mult(testv_4b, testm_4b) == [8, 17]

def test_five_matrix_matrix_mult():
    testm_5a: list = [[3, 1], [4, 3], [-1, 2]]
    testm_5b: list = [[5, -1, 0], [2, 4, 3]]
    testm_5c: list = [[1, 2], [3, 4]]
    testm_5d: list = [[1, 2], [3, 4]]

    assert matrix_matrix_mult(testm_5a, testm_5b) == [[11, 2], [19, 20]]
    assert matrix_matrix_mult(testm_5c, testm_5d) == [[7, 10], [15, 22]]