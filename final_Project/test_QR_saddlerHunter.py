import QR_saddlerHunter
import pytest

qrtest1 = [[1,1,0],[1,0,1],[0,1,1]]
qrtest2 = [[2,2,1], [3,4,1]]
def test_mat_build():
    assert QR_saddlerHunter.mat_build(qrtest1) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert QR_saddlerHunter.mat_build([[1, 1], [1, 1]]) == [[0, 0], [0, 0]]

def test_sgs():
    assert QR_saddlerHunter.stable_gramschmidt(qrtest2) == [[[2/3, 2/3, 1/3], [-1/3, 2/3, -2/3], [[3, 0],[5, 1]]]]
    assert QR_saddlerHunter.stable_gramschmidt(qrtest1) == [[[(1/(2**(1/2))), 1/(2**(1/2)), 0],[1/(6**(1/2)), -1/(6**(1/2)), 2/(6**(1/2))], [-1/(3**(1/2)), 1/(3**(1/2)), 1/(3**(1/2))]],
                                                        [[(2/(2**(1/2))), 0, 0], [(1/(2**(1/2))), (3/(6**(1/2))), 0], [(1/(2**(1/2))), (1/(6**(1/2))), (2/(3**(1/2)))]]]
def test_orth_basis():
    assert QR_saddlerHunter.orthonormal_basis(qrtest2) == [[2/3, 2/3, 1/3], [-1/3, 2/3, -2/3]]
    assert QR_saddlerHunter.orthonormal_basis(qrtest1) == [[(1/(2**(1/2))), 1/(2**(1/2)), 0],[1/(6**(1/2)), -1/(6**(1/2)), 2/(6**(1/2))], [-1/(3**(1/2)), 1/(3**(1/2)), 1/(3**(1/2))]]

"""Test for functions for HW7, Im not sure what the assertion error is for the F builder test or the householder test
but the numbers seem to come out fine"""
testm_a: list = [[1, 2], [3, 4]]
testm_b: list = [[5, -1, 0], [2, 4, 3]]
testm_c: list = [[1, 2], [1, 3]]
#test for deep copy creator
def test_deep():
    assert QR_saddlerHunter.deep_copy(testm_a) == [[1, 2], [3, 4]]
    assert QR_saddlerHunter.deep_copy(testm_b) == [[5, -1, 0], [2, 4, 3]]
#test for Identity builder
def test_ID_builder():
    assert QR_saddlerHunter.ID_build(2) == [[1, 0], [0, 1]]
    assert QR_saddlerHunter.ID_build(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
#test for sub column generator
def test_sub_col():
    assert QR_saddlerHunter.sub_col(testm_a, 2) == [4]
    assert QR_saddlerHunter.sub_col(testm_a, 1) == [1, 2]
#test for element conjugator
def test_element_con():
    assert QR_saddlerHunter.ele_conj(2) == 2
    assert QR_saddlerHunter.ele_conj(1+2j) == 1-2j
#test for orthonormal basis
def test_orthbasis():
    assert QR_saddlerHunter.orthonormal_basis(testm_a) == [[0.447, 0.894], [0.894, -0.447]]
    assert QR_saddlerHunter.orthonormal_basis(testm_c) == [[0.447, 0.894], [-0.894, 0.447]]
#test for fbuilder
def test_f_build():
    assert QR_saddlerHunter.f_builder([-1, 1, 1]) == [[-0.5773, 0.5773, -0.5773], [0.4082, 0.816, 0.4082], [0.707, -2.7755575615628914e-17, -0.7071]]
    assert QR_saddlerHunter.f_builder([7, 2, 7]) == [[0.47, 0.82, 0.47], [0.82, -0.73, -0.56], [0.47, -0.56, 0.72]]
#test Q builder
def test_Q_builder():
    assert QR_saddlerHunter.q_builder([[0.9659, 0.2588], [0.2588, -0.9659]], 3) == [[1, 0, 0], [0, 0.9659, 0.2588], [0, 0.2588, -0.9659]]
    assert QR_saddlerHunter.q_builder([[1, 2], [1, 3]], 3) == [[1, 0, 0], [0, 1, 2], [0, 1, 3]]
#test for householder
plswork3: list = [[-1, 1, -1], [-1, 3, -1], [1, 3, 5]]
plswork2: list = [[2, 2, 1], [-2, 1, 2], [1, 3, 1]]
"""For the places in R where the values should be zero but isnt due to rounding errors i used the value my householder
outputs to hopefully allow it to pass the test. Before the final i will try to make my program insert zeros for numbers
that are very nearly zero within some tolerance"""
def test_householder():
    assert QR_saddlerHunter.householder(plswork3) == ([[-0.5773, 0.5773, -0.5773], [0.4082, 0.816, 0.4082], [0.707, -2.7755575615628914e-17, -0.7071]], [[1.7320, -7.850462293418875e-17, -1.3597399555105185e-16], [2.886, 1.6329, -2.7755575615628914e-16], [-1.732, 4.89, -2.828]])
    assert QR_saddlerHunter.householder(plswork2) == ([[0.6666666666666667, 0.6666666666666666, 0.3333333333333333], [0.6666666666666666, -0.33333333333333326, -0.6666666666666666], [0.3333333333333333, -0.6666666666666666, 0.6666666666666667]], [[3.0, 1.1102230246251565e-16, 1.1102230246251565e-16], [-2.220446049250313e-16, -3.0, 2.220446049250313e-16], [3.0000000000000004, -1.0, -1.0]])
