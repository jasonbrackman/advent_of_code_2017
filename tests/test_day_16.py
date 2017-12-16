import pytest
from .. import day_16

def test_one_pass():

    start = 'abcde'
    for _ in range(1):
        s = day_16.spin(start, 1)
        e = day_16.exchange(s, 3, 4)
        p = day_16.partner(e, 'e', 'b')

        assert s == 'eabcd'
        assert e == 'eabdc'
        assert p == 'baedc'
        start = p




