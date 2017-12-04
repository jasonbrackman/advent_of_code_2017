import pytest
from .. import day_03
"""

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.
"""

@pytest.mark.parametrize('param, expect', [(1, [["1"]])])
def test_build_sprial(param, expect):
    assert expect == day_03.build_spiral(param)


def test_build_sprial_2():
    assert [['1', '2']] == day_03.build_spiral(2)



def test_build_spiral_3():
    assert [['.', '3'],
            ['1', '2']] == day_03.build_spiral(3)


def test_build_spiral_4():
    assert[['4', '3'],
           ['1', '2']] == day_03.build_spiral(4)


# def test_build_spiral_5():
#     assert[['5', '4', '3'],
#            ['.', '1', '2']] == day_03.build_spiral(5)

@pytest.mark.parametrize('param, expect', [(1, 0),
                                           (12, 3)])

def test_count_steps_with_padding(param, expect):
    assert expect == day_03.count_steps_with_padding(param)


@pytest.mark.parametrize('param, expect', [(4, 4)])
def test_sum_of_adjacent_numbers(param, expect):
    assert expect == day_03.build_spiral(param, special=True)
