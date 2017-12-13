import pytest
from .. import day_13


@pytest.mark.parametrize('param, expect', [(0, 0)])
def test_increment(param, expect):
    assert expect == day_13.test(param)

