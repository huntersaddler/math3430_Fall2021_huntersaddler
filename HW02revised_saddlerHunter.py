"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""


#Example:

#Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

#End Example



#Problem 01

"""

Write an algorithm to implement scalar-vector multiplication.

Q1: What do we have?

A1: One scalar stored as integer named sc1_a and one vector stored as a list named v1_a

Q2: What do we want?

A2: We want the product of sc1_a and v1_a stored as a list

Q3: How will we get there?

A3: We will make an empty list the size of v1_a and store the product of sc1_a and each 
    element of v1_a in the empty list


Alg_1: We will call this algorithm scal_vec_mult(int, vector)

Step 1: Create a list of 0's the same length as input vector v1_a and name it result

Step 2: For each index from 0 to the length of input v1_a, replace the 0's in result with
        the product of input v1_a at that index with the scaler input sc1_a
    
Step 3: return result

"""

def scal_vec_mult(sc1_a, v1_a):
  result = [0 for element in v1_a]
  for index in range(len(result)):
    result[index] = sc1_a * v1_a[index]
  return result

#Problem 02

"""

Write an algorithm to implement scalar-matrix multiplication.

Q1: What do we have?

A1: One scalar stored as integer named sc2_a and one matrix stored as a list of vectors
    named m2_a

Q2: What do we want?

A2: The product of sc2_a and m2_a stored as a list of vectors

Q3: How will we get there?

A3: We will make an empty list the size of m2_a and store the product of sc2_a and each 
    column of m2_a in the empty list


Alg_2: We will call this algorithm scal_matrix_mult(scalar, matrix)

Step 1: Create a list of vectors filled with 0's the same size as our input m2_a and name
        it result

Step 2: For each index from 0 to the length of input m1_a, use scal-vect_mult(sc2_a, m2_a) from #1
        replace the 0's in each column vector in result with the corresponding product
        of input m2_a at that index and input sc2_a

Step 3: return result

"""
def scal_matrix_mult(sc2_a, m2_a):
  result = [0 for element in m2_a]
  for index in range(len(result)):
    result[index] = scal_vec_mult(sc2_a, m2_a[index])
  return result

#Problem 03

"""

Write an algorithm to implement matrix addition.

Q1: What do we have?

A1: Two matrices stored as lists of column vectors named m3_a and m3_b

Q2: What do we want?

A2: The sum of m3_a and m3_b stored in a list named result

Q3: How will we get there?

A3: We will make an empty list the same size as our input matrices, and using add_vectors()
    we will store the sums of the corresponding vectors in our result matrix


Alg_3: We will call this algorithm matrix_matrix_add(matrix, matrix)

Step 1: Create a list of vectors filled with 0's the same size as our input m3_a and name
        it result

Step 2: For each index from 0 to the length of the m3_a, use add_vectors(m3_a, m3_b) from example 
        to replace the 0's in result at index with the corresponding sum of the vectors at 
        the index for inputs m3_a and m3_b

Step 3: return result

"""

def matrix_matrix_add(m3_a, m3_b):
  result = [0 for element in m3_a]
  for index in range(len(result)):
    result[index] = add_vectors(m3_a[index], m3_b[index])
  return result

#Problem 04

"""

Problem #4

Write an algorithm to implement matrix-vector multiplication using the linear
combination of columns method. You must use the algorithms from Problem #0 and Problem # 1
 

Q1: What do we have?

A1: One matrix stored as a list vectors named m4_a and a vector stored as a list named v4_a

Q2: What do we want?

A2: The product of m4_a and v4_a stored as a list of vectors named result

Q3: How will we get there?

A3: We will create an empty list named result the same size as a column in m4_a. Then using scal_vect_mult() for each
    column in m4_a with corresponing scalar in v4_a, using add_vector() for each column in m4_a to add each vector 
    product to the result


Alg_4: We will call this algorithm matrix_vect_mult(vector, matrix)

Step 1: Create empty list named result the size of a list in m4_a

Step 2: For each index from 0 to length of v4_a, use scal_vect_mult(v4_a(index), m4_a(index))
        to get the product of the scalar at index in v4_a and the column vector at index in m4_a
        and add this product vector with add_vectors(product, result) for each column in m4_a to result

Step 3: return result

"""

def matrix_vector_mult(v4_a, m4_a):
  result = [0 for element in m4_a[1]]
  for index in range(len(v4_a)):
    result = add_vectors(result, scal_vec_mult(v4_a[index], m4_a[index]))
  return result

#Problem 05

"""

Write an algorithm to implement matrix-matrix multiplication using your
algorithm from Problem #4.

Q1: What do we have?

A1: Two matrices(assuming input dimensions can be multiplied) stored as lists of vectors named m5_a and m5_b

Q2: What do we want?

A2: The product of our inputs m5_a and m5_b stored in a list of vectors named result

Q3: How will we get there?

A3: We will create a list of 0's named result the same size as m5_b. Using matrix-vect_mult() to find each linear combination 
    then add the product vectors to result 


Alg_5: We will call this algorithm matrix_matrix_mult(matrix, matrix)

Step 1: Create empty list named result same size as m5_b

Step 2: For each index from 0 to the length of m5_b, use matrix_vect_mult(m5_a(index), m5_b) to find the product of the column
        vector of m5_a at the index with m5_b,  then add each product at the index
        to the result matrix
        
Step 3: return result

"""

def matrix_matrix_mult(m5_a, m5_b):
  result = [0 for element in m5_b]
  for index in range(len(m5_b)):
    result[index] = matrix_vector_mult(m5_b[index], m5_a)
  return result


"""TEST INPUTS"""

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]


print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4, 3, 6]')

testv_4a = [5, -1, 0]
testv_4b = [1, 3, 4]


print('Test Output for add_vectors: ' + str(add_vectors(testv_4a,testv_4b)))
print('Should have been [6, 2, 4]')

#Test for problem 1

testv_1a = [4, 3, 1, 7, 2]
tests_1a = 2

print('Test Output for scal_vec_mult: ' + str(scal_vec_mult(tests_1a, testv_1a)))
print('Should have been [8, 6, 2, 14, 4]')

testv_1b = [3, 0, 10, 111]
tests_1b = 3

print('Test Output for scal_vec_mult: ' + str(scal_vec_mult(tests_1b, testv_1b)))
print('Should have been [9, 0, 30, 333]')

#Test for problem 2

testm_2a = [[2,3], [6,1], [4,3]]
tests_2a = 2

print('Test Output for scal_matrix_mult: ' + str(scal_matrix_mult(tests_2a, testm_2a)))
print('Should have been [[4, 6], [12, 2], [8, 6]]')

testm_2b = [[1,2], [3,3], [0,0], [0,111]]
tests_2b = 3

print('Test Output for scal_matrix_mult: ' + str(scal_matrix_mult(tests_2b, testm_2b)))
print('Should have been [[3, 6], [9, 9], [0, 0], [0, 333]]')

#Test for problem 3

testm_3a = [[1, 1], [2, 2], [3, 3]]
testm_3b = [[1, 2], [1, 2], [1, 2]]

print('Test Output for matrix_matrix_add: ' + str(matrix_matrix_add(testm_3a, testm_3b)))
print('Should have been [[2, 3], [3, 4], [4, 5]]')

testm_3c = [[1, 0], [7, 1], [29, 3], [100, 100]]
testm_3d = [[1, 2], [1, 2], [1, 2], [100, 100]]

print('Test Output for matrix_matrix_add: ' + str(matrix_matrix_add(testm_3c, testm_3d)))
print('Should have been [[2, 2], [8, 3], [30, 5], [200, 200]]')

#Test for problem 4

testv_4a = [5, -1, 0]
testm_4a = [[3, 1], [4, 3], [-1, 2]]

print('Test Output for matrix_vector_mult: ' + str(matrix_vector_mult(testv_4a, testm_4a)))
print('Should have been [11,2]')

testv_4b = [1, 3, 4]
testm_4b = [[1, 3], [1, 2], [1, 2]]

print('Test Output for matrix_vector_mult: ' + str(matrix_vector_mult(testv_4b, testm_4b)))
print('Should have been [8, 17]')

#Test for problem 5

testm_5a = [[3, 1], [4, 3], [-1, 2]]
testm_5b = [[5, -1, 0], [2, 4, 3]]

print('Test Output for matrix_matrix_mult: ' + str(matrix_matrix_mult(testm_5a, testm_5b)))
print('Should have been [[11, 2], [19, 20]]')

testm_5c = [[1, 2], [3, 4]]
testm_5d = [[1, 2], [3, 4]]

print('Test Output for matrix_matrix_mult: ' + str(matrix_matrix_mult(testm_5c, testm_5d)))
print('Should have been [[7, 10], [15, 22]]')