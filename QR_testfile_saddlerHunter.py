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