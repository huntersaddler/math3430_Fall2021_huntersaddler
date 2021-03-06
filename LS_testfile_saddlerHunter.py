import pytest
import LS_saddlerHunter
plsm: list = [[1, 0, 0], [2, -4, 0], [1, 1, 2]]
p1: list = [[1, 0, 0], [-2, 1, 0], [1, 6, 1]]
bm: list = [5, 2, -4]
bh: list = [4, -1, 2]

def test_leastsquares():
    assert LS_saddlerHunter.LeastSquares([5, 7], [[1, 2], [1, 3]]) == [8, 3]
    assert LS_saddlerHunter.LeastSquares([5, 9], [[1, 2], [1, 4]]) == [5.5, -0.5]

def test_backsub():
    assert LS_saddlerHunter.back_sub(plsm, bm) == [9, -1, -2]
    assert LS_saddlerHunter.back_sub(p1, bh) == [-24, -13, 2]