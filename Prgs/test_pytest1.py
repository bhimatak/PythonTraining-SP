import pytest

import pytest1

def test_cal_total_01():
    total = pytest1.cal_total(10,20)
    assert total == 30

    total = pytest1.cal_total(50,20)
    assert total == False

'''
python -m pytest -v -rxs
test_pytest1.py::test_cal_total PASSED                                   [ 50%]
test_pytest1.py::test_mul SKIPPED (I dont know)  

SKIPPED [1] test_pytest1.py:8: I dont know

'''
@pytest.mark.skip(reason="I dont know")
def test_mul():
    res = pytest1.cal_mul(3,5)
    assert res == 15
