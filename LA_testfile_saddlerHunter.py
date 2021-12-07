import LA_saddlerHunter
import pytest
def test_zero_add_vectors():
    test_vector_01: list = [1, 2, 4]
    test_vector_02: list = [3, 1, 2]
    assert LA_saddlerHunter.add_vectors(test_vector_01, test_vector_02) == [4, 3, 6]
    assert LA_saddlerHunter.add_vectors(test_vector_01, [0, 0, 0]) == [1, 2, 4]
def test_one_scal_vect_mult():
    testv_1a: list = [4, 3, 1]
    tests_1a: int = 2
    testv_1b: list = [3, 0, 10, 111]
    tests_1b: int = 3
    assert LA_saddlerHunter.scal_vec_mult(tests_1a, testv_1a) == [8, 6, 2]
    assert LA_saddlerHunter.scal_vec_mult(tests_1b, testv_1b) == [9, 0, 30, 333]
def test_two_scal_matrix_mult():
    testm_2a: list = [[2, 3], [6, 1], [4, 3]]
    tests_2a: int = 2
    testm_2b: list = [[1, 2], [3, 3], [0, 0], [0, 111]]
    tests_2b: int = 3
    assert LA_saddlerHunter.scal_matrix_mult(tests_2a, testm_2a) == [[4, 6], [12, 2], [8, 6]]
    assert LA_saddlerHunter.scal_matrix_mult(tests_2b, testm_2b) == [[3, 6], [9, 9], [0, 0], [0, 333]]
def test_three_matrix_matrix_add():
    testm_3a: list = [[1, 1], [2, 2], [3, 3]]
    testm_3b: list = [[1, 2], [1, 2], [1, 2]]
    testm_3c: list = [[1, 0], [7, 1], [29, 3], [100, 100]]
    testm_3d: list = [[1, 2], [1, 2], [1, 2], [100, 100]]
    assert LA_saddlerHunter.matrix_matrix_add(testm_3a, testm_3b) == [[2, 3], [3, 4], [4, 5]]
    assert LA_saddlerHunter.matrix_matrix_add(testm_3c, testm_3d) == [[2, 2], [8, 3], [30, 5], [200, 200]]
def test_four_matrix_vector_mult():
    testv_4a: list = [5, -1, 0]
    testm_4a: list = [[3, 1], [4, 3], [-1, 2]]
    testv_4b: list = [1, 3, 4]
    testm_4b: list = [[1, 3], [1, 2], [1, 2]]
    assert LA_saddlerHunter.matrix_vector_mult(testv_4a, testm_4a) == [11, 2]
    assert LA_saddlerHunter.matrix_vector_mult(testv_4b, testm_4b) == [8, 17]
def test_five_matrix_matrix_mult():
    testm_5a: list = [[3, 1], [4, 3], [-1, 2]]
    testm_5b: list = [[5, -1, 0], [2, 4, 3]]
    testm_5c: list = [[1, 2]]
    testm_5d: list = [[1], [3]]
    assert LA_saddlerHunter.matrix_matrix_mult(testm_5a, testm_5b) == [[11, 2], [19, 20]]
    assert LA_saddlerHunter.matrix_matrix_mult(testm_5c, testm_5d) == [[1, 2], [3, 6]]
    """Test Functions for HW04"""
def test_absolute_val():
    tests1_absval: int = -2
    tests2_absval: complex = 2 + 3j
    assert LA_saddlerHunter.absolute_val(tests1_absval) == 2
    assert LA_saddlerHunter.absolute_val(tests2_absval) == (13) ** (1 / 2)  # square root 13
def test_vector_norm():
    testv1_vecnorm: list = [1, 2, 3, 4]
    testv2_vecnorm: list = [1 + 1j, 2 + 1j]
    tests1_vecnorm: int = 1
    assert LA_saddlerHunter.vector_norm(testv1_vecnorm, tests1_vecnorm) == 10
    assert LA_saddlerHunter.vector_norm(testv2_vecnorm) == (7) ** (1 / 2)
def test_infinity_norm():
    testv1_infnorm: list = [1, 2, 3, 4, 5, -6]
    testv2_infnorm: list = [-12, 25, -40]
    assert LA_saddlerHunter.infinity_norm(testv1_infnorm) == 6.0
    assert LA_saddlerHunter.infinity_norm(testv2_infnorm) == 40.0
def test_any_norm():
    testv1_anynorm: list = [12, -22, 3, 44]
    testv2_anynorm: list = [1 + 1j, 2 + 2j, 3 + 3j]
    tests1_anynorm: int = 3
    testb1_anynorm: bool = True
    assert LA_saddlerHunter.any_norm(testv2_anynorm, 2, testb1_anynorm) == 4.242640687119285
    assert LA_saddlerHunter.any_norm(testv1_anynorm, tests1_anynorm, False) == 42.41222947336992
def test_inner_product():
    testv1_innerprod: list = [1, 2, 3]
    testv2_innerprod: list = [4, 5, 6]
    testv3_innerprod: list = [1 + 1j, 2 + 2j, 3 + 3j]
    testv4_innerprod: list = [1 + 1j, 2 + 2j, 3 + 3j]
    assert LA_saddlerHunter.inner_prod(testv1_innerprod, testv2_innerprod) == 32
    assert LA_saddlerHunter.inner_prod(testv3_innerprod, testv4_innerprod) == 28