import pytest
from .. import day_12

input = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

lines = input.split("\n")


def test_count_steps_1():
    input = ["0 <-> 2"]
    result = day_12.count_steps(input, 0)
    assert 1 == result


def test_count_steps_2():
    input = ["0 <-> 2",
             "1 <-> 1"]

    result = day_12.count_steps(input, 0)
    assert 1 == result

def test_count_steps_3():
    input = ["0 <-> 2",
             "1 <-> 1",
             "2 <-> 0, 3, 4"]
    result = day_12.count_steps(input, 0)
    assert 2 == result

def test_count_steps_4():
    input = ["0 <-> 2",
             "1 <-> 1",
             "2 <-> 0, 3, 4",
             "3 <-> 2, 1"]
    result = day_12.count_steps(input, 0)
    assert 3 == result

def test_count_steps_5():
    input = ["0 <-> 2",
             "1 <-> 1",
             "2 <-> 0, 3, 4",
             "3 <-> 2, 4",
             "4 <-> 2, 3"]
    result = day_12.count_steps(input, 0)
    assert 4 == result

def test_count_steps_6():
    input = ["0 <-> 2",
             "1 <-> 1",
             "2 <-> 0, 3, 4",
             "3 <-> 2, 4",
             "4 <-> 2, 3",
             "5 <-> 6",
             "6 <-> 4, 5"]
    result = day_12.create_connections(input, 0)
    assert 6 == result
