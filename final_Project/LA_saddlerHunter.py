# Begin Example
# Problem #0

def add_vectors(vector_a: list[float],
                vector_b: list[float]) -> list:
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
def scal_vec_mult(sc1_a: complex, v1_a: list) -> list:
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
    result: list = [0 for element in v1_a]
    for index in range(len(result)):
        result[index] = sc1_a * v1_a[index]
    return result



#Problem 2
def scal_matrix_mult(sc2_a: complex, m2_a: list) -> list:
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
    result: list = [0 for element in m2_a]
    for index in range(len(result)):
        result[index] = scal_vec_mult(sc2_a, m2_a[index])
    return result




#Problem 3
def matrix_matrix_add(m3_a: list, m3_b: list) -> list:
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
    result: list = [0 for element in m3_a]
    for index in range(len(result)):
        result[index] = add_vectors(m3_a[index], m3_b[index])
    return result

#Problem 4
def matrix_vector_mult(v4_a: list, m4_a: list) -> list:
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
    result: list = [0 for element in m4_a[0]]
    for index in range(len(v4_a)):
        result = add_vectors(result, scal_vec_mult(v4_a[index], m4_a[index]))
    return result




#Problem 5
def matrix_matrix_mult(m5_a: list, m5_b: list) -> list:
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
    result: list = [0 for element in m5_b]
    for index in range(len(m5_b)):
        result[index] = matrix_vector_mult(m5_b[index], m5_a)
    return result

#HOMEWORK 04 STARTS HERE

#Problem 1
def absolute_val(sc_1: complex) -> complex:
    """ Takes the absolute value of a scalar input

       Takes a scalar input and squares the real and imaginary parts and adds them together, then takes the square root of
       the total. Returns the absolute value

       Args:
           sc_1 a scalar stored as complex type

        Returns:
           The absolute value of the input scalar """
    if sc_1 is int:
        if sc_1 < 0:
            return -sc_1
        else:
            return sc_1
    else:
        return (sc_1.real**2 + sc_1.imag**2)**(1/2)


#Problem 2
def vector_norm(v_2: list, sc_2: int = 2) -> complex:
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
def infinity_norm(v_3: list) ->complex:
    """ Computes the infinity norm of the given input vector

       Creates a complex variable named IF and sets it to 0. For the length of the vector input v_3, we check if the absolute
       value of the element at the index in v_3 is greater than IF. If true then IF is set to the element at the index and
       we go next. If false we go next index. Returns IF at end

       Args:
           v_3 is a vector stored as a list

        Returns:
           IF is the infinity norm of the input vector """
    IF: complex = 0
    for index in range(len(v_3)):
        if absolute_val(v_3[index]) > IF:
            IF = absolute_val(v_3[index])
        else:
            continue
    return IF


#Problem 4
def any_norm(v_4: list, sc_4: int = 2, b_4: bool = False) -> complex:
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
    if b_4:
        an4: complex = infinity_norm(v_4)
        return an4
    else:
        an4: complex = vector_norm(v_4, sc_4)
        return an4


#Problem 5
def inner_prod(v_5a: list, v_5b: list) ->complex:
    """ Computes the inner product of the two input vectors

       Creates result variable set to 0 with complex type. For the length of the input vector v_5a, we take the product of
       the real parts of the elements in v_5a and v_5b at the index, and the product of the imaginary parts of v_5a and v_5b
       at the index and add them, adding the total of each index to the result. At end we return result

       Args:
           v_5a is a vector stored as a list
           v_5b is a vector stored as a list

        Returns:
           result, the inner product of the two input vectors"""
    result: complex = 0
    for index in range(len(v_5a)):
        result += (v_5a[index].real*v_5b[index].real) + (v_5a[index].imag*v_5b[index].imag)
    return result