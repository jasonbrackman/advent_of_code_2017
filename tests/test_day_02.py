"""
5 1 9 5
7 5 3
2 4 6 8

    The first row's largest and smallest values are 9 and 1, and their difference is 8.
    The second row's largest and smallest values are 7 and 3, and their difference is 4.
    The third row's difference is 6.

In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
"""

import pytest
from .. import day_02

@pytest.mark.parametrize('param, expect', [('5 1 9 5', 8),
                                           ('7 5 3', 4),
                                           ('2 4 6 8', 6)])
def test_min_max_diff(param, expect):
    assert day_02.min_max_dif(param) == expect


@pytest.mark.parametrize('param, expect', [('5 9 2 8', 4),
                                          ('9 4 7 3', 3),
                                          ('3 8 6 5', 2)])
def test_get_divisible_result(param, expect):
    assert day_02.get_divisible_result(param) == expect