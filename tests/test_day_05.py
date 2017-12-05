import pytest
from .. import day_05

"""
    (0) 3  0  1  -3  - before we have taken any steps.
    (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). Fortunately, the instruction is then incremented to 1.
     2 (3) 0  1  -3  - step forward because of the instruction we just modified. The first instruction is incremented again, now to 2.
     2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
     2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
     2  5  0  1  -2  - jump 4 steps forward, escaping the maze.
    """

@pytest.mark.parametrize('param, expect', [([0,3,0,1,-3], 5)])
def test_increment(param, expect):
    assert expect == day_05.increment(param)


def test_increment_special():
    param = [0, 3, 0, 1, -3]
    expect = 10
    assert expect == day_05.increment(param, special=True)
