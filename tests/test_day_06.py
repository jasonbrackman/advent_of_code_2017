import pytest
from .. import day_06


@pytest.mark.parametrize('param, expect', [([0, 2, 7, 0], [2, 4, 1, 2]),
                                           ([2, 4, 1, 2], [3, 1, 2, 3]),
                                           ([3, 1, 2, 3], [0, 2, 3, 4])])
def test_increment(param, expect):
    assert expect == day_06.redistribute(param)


def test_find_loop():
    assert 5 == day_06.find_loop([0, 2, 7, 0])