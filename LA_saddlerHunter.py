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


#HOMEWORK 04 STARTS HERE
"""
This assignment is due by 11:59pm on 10/22/2021. 

For this assignment you will be adding functions to the LA.py script from HW03.
All functions must satisfy the same requirements as in HW03. The functions you
will need to add are

#1) A function which takes a scalar as it's input and returns it's absolute
value. Note that this function must be able to take both real numbers and
complex numbers as input!!!

#2) A function which takes the as it's arguments

1) A vector stored as a list.

2) An integer valued scalar, set to default as 2. 

and returns the norm of the input vector. Which norm must be determined using
the integer valued scalar input. If not argument is given, it should default to
2. 

#3) A function which takes as it's argument a vector stored as a list and
returns the infinity norm of the input vector.

#4) A function which takes as it's arguments

1) A vector stored as a list.

2) An integer valued scalar, set to default as 2.

3) A boolean value, set to default as False.

The function will return the norm of the input vector. If the boolean value is
given as True, the function will return the infinity norm of the input vector.
Otherwise it will return the p-norm of the vector corresponding to the integer
scalar argument. This function must use the functions from problem #2 and
problem #3 to earn credit. 

#5) A function which takes as it's arguments two vectors, stored as lists. This
function then returns the inner product of these vectors. Your function must be
able to handle complex numbers!
"""

#Problem 1
""" Takes the absolute value of a scalar input

   Takes a scalar input and squares the real and imaginary parts and adds them together, then takes the square root of 
   the total. Returns the absolute value

   Args:
       sc_1 a scalar stored as complex type

    Returns:
       The absolute value of the input scalar """

def absolute_val(sc_1: complex) -> complex:
    sc_1 = ((sc_1.real**2) + (sc_1.imag**2))**(1/2)
    return sc_1


#Problem 2
""" Computes the p-norm of a vector with the default p being the two norm

   Creates a result variable with complex type set to 0. If p is 1 then for the length of input vector v_2 we take the
   absolute value of the element in v_2 at the index and adds it to the result, then returns result at end. If p is not 1 then 
   for the length of v_2 we take the element at the index and raise it to p and add it to result. Then at the end we take 
   the p-root of the result and return result. If no scalar input is given the function defualts to the two norm

   Args:
       v_2 is a vector stored as a list
       sc_2 is a scalar set to default as 2

    Returns:
       returns the result which is the p norm of the vector, and has complex type """

def vector_norm(v_2: list, sc_2: int = 2) -> complex:
    result: complex = 0
    if sc_2 == 1:
        for index in range(len(v_2)):
            result += absolute_val(v_2[index])
        return result
    else:
        for index in range(len(v_2)):
            result += (((v_2[index].real)**sc_2) + ((v_2[index].imag)**sc_2))
        result = result**(1/(sc_2))
        return result

#Problem 3
""" Computes the infinity norm of the given input vector

   Creates a complex variable named IF and sets it to 0. For the length of the vector input v_3, we check if the absolute
   value of the element at the index in v_3 is greater than IF. If true then IF is set to the element at the index and 
   we go next. If false we go next index. Returns IF at end

   Args:
       v_3 is a vector stored as a list

    Returns:
       IF is the infinity norm of the input vector """

def infinity_norm(v_3: list) ->complex:
    IF: complex = 0
    for index in range(len(v_3)):
        if absolute_val(v_3[index]) > IF:
            IF = absolute_val(v_3[index])
        else:
            continue
    return IF


#Problem 4
""" Computes the either the infinity norm or the p-norm with default being the 2 norm, to be decided by user input

   Checks if the boolean input is True. If True returns the infinity norm using infinity_norm() for the input vector v_4.
   If false, computes the p-norm of input vector v_4 using vector_norm() with p being the input scalar sc_4.
   If no scalar input is given, computes the 2 norm by default

   Args:
       v_4 is a vector stored as a list
       sc_4 is a scalar stored as an int with default value of 2
       b_4 is a boolean type with default set to False

    Returns:
       Either returns the infinity norm or the p-norm of the vector depending on user inputs"""

def any_norm(v_4: list, sc_4: int = 2, b_4: bool = False) -> complex:
    if b_4:
        an4: complex = infinity_norm(v_4)
        return an4
    else:
        an4: complex = vector_norm(v_4, sc_4)
        return an4


#Problem 5
""" Computes the inner product of the two input vectors

   Creates result variable set to 0 with complex type. For the length of the input vector v_5a, we take the product of
   the real parts of the elements in v_5a and v_5b at the index, and the product of the imaginary parts of v_5a and v_5b
   at the index and add them, adding the total of each index to the result. At end we return result

   Args:
       v_5a is a vector stored as a list
       v_5b is a vector stored as a list
       
    Returns:
       result, the inner product of the two input vectors"""

def inner_prod(v_5a: list, v_5b: list) ->complex:
    result: complex = 0
    for index in range(len(v_5a)):
        result += (v_5a[index].real*v_5b[index].real) + (v_5a[index].imag*v_5b[index].imag)
    return result


"""Test Functions for HW04"""


def test_absolute_val():
    tests1_absval: int = -2
    tests2_absval: complex = 2+3j

    assert absolute_val(tests1_absval) == 2
    assert absolute_val(tests2_absval) == (13)**(1/2)  #square root 13


def test_vector_norm():
    testv1_vecnorm: list = [1, 2, 3, 4]
    testv2_vecnorm: list = [1+1j, 2+1j]
    tests1_vecnorm: int = 1

    assert vector_norm(testv1_vecnorm, tests1_vecnorm) == 10
    assert vector_norm(testv2_vecnorm) == (7)**(1/2)


def test_infinity_norm():
    testv1_infnorm: list = [1, 2, 3, 4, 5, -6]
    testv2_infnorm: list = [-12, 25, -40]

    assert infinity_norm(testv1_infnorm) == 6.0
    assert infinity_norm(testv2_infnorm) == 40.0


def test_any_norm():
    testv1_anynorm: list = [12, -22, 3, 44]
    testv2_anynorm: list = [1+1j, 2+2j, 3+3j]
    tests1_anynorm: int = 3
    testb1_anynorm: bool = True

    assert any_norm(testv2_anynorm, 2, testb1_anynorm) == 4.242640687119285
    assert any_norm(testv1_anynorm, tests1_anynorm, False) == 42.41222947336992


def test_inner_product():
    testv1_innerprod: list = [1, 2, 3]
    testv2_innerprod: list = [4, 5, 6]
    testv3_innerprod: list = [1+1j, 2+2j, 3+3j]
    testv4_innerprod: list = [1+1j, 2+2j, 3+3j]

    assert inner_prod(testv1_innerprod, testv2_innerprod) == 32
    assert inner_prod(testv3_innerprod, testv4_innerprod) == 28


