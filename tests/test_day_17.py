import pytest
from .. import day_17


def test_spinlock_1():
    assert [0] == day_17.spinlock(range_=0)


def test_spinlock_2():
    assert [0, 1] == day_17.spinlock(range_=2)


def test_spinlock_3():
    assert [0, 2, 1] == day_17.spinlock(range_=3)


def test_spinlock_4():
    assert [0, 2, 3, 1] == day_17.spinlock(range_=4)


def test_spinlock_5():
    assert [0, 2, 4, 3, 1] == day_17.spinlock(range_=5)

def test_spinlock_6():
    assert [0, 5, 2, 4, 3, 1] == day_17.spinlock(range_=6)


def test_spinlock_10():
    assert [0, 9, 5, 7,  2,  4,  3,  8,  6,  1] == day_17.spinlock(range_=10)

