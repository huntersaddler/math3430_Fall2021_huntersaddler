import QR_saddlerHunter
import pytest

"""Adding this so I remember to come back and fix the tests so that they will work with the rounding errors. Will update
with tolerances this weekend"""

qrtest1 = [[1,1,0],[1,0,1],[0,1,1]]
qrtest2 = [[2,2,1], [3,4,1]]


assert QR_saddlerHunter.stable_gramschmidt(qrtest2) == [[[2/3, 2/3, 1/3], [-1/3, 2/3, -2/3], [[3, 0],[5, 1]]]]
assert QR_saddlerHunter.stable_gramschmidt(qrtest1) == [[[(1/(2**(1/2))), 1/(2**(1/2)), 0],[1/(6**(1/2)), -1/(6**(1/2)), 2/(6**(1/2))], [-1/(3**(1/2)), 1/(3**(1/2)), 1/(3**(1/2))]],
                                                        [[(2/(2**(1/2))), 0, 0], [(1/(2**(1/2))), (3/(6**(1/2))), 0], [(1/(2**(1/2))), (1/(6**(1/2))), (2/(3**(1/2)))]]]


assert QR_saddlerHunter.orthonormal_basis(qrtest2) == [[2/3, 2/3, 1/3], [-1/3, 2/3, -2/3]]
assert QR_saddlerHunter.orthonormal_basis(qrtest1) == [[(1/(2**(1/2))), 1/(2**(1/2)), 0],[1/(6**(1/2)), -1/(6**(1/2)), 2/(6**(1/2))], [-1/(3**(1/2)), 1/(3**(1/2)), 1/(3**(1/2))]]




"""Test for functions for HW7"""

testm_a: list = [[1, 2], [3, 4]]
testm_b: list = [[5, -1, 0], [2, 4, 3]]
#test for deep copy creator
assert QR_saddlerHunter.deep_copy(testm_a) == [[1, 2], [3, 4]]
assert QR_saddlerHunter.deep_copy(testm_b) == [[5, -1, 0], [2, 4, 3]]
#test for Identity builder
assert QR_saddlerHunter.ID_build(2) == [[1, 0], [0, 1]]
assert QR_saddlerHunter.ID_build(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
#test for sub column generator
assert QR_saddlerHunter.sub_col(testm_a, 2) == [4]
assert QR_saddlerHunter.sub_col(testm_a, 1) == [1, 2]
#test for element conjugator
assert QR_saddlerHunter.ele_conj(2) == 2
assert QR_saddlerHunter.ele_conj(1+2j) == 1-2j
#test for conjugate transpose
assert QR_saddlerHunter.conjugate_transpose(testm_a) == [[1, 3], [2, 4]]
assert QR_saddlerHunter.conjugate_transpose(testm_b) == [[5, 2], [-1, 4], [0, 3]]


