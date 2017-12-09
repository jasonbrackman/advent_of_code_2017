import pytest
from .. import day_09


def test_count_braces_1():
    print(day_09.count_braces('{}'))
    assert 1 == day_09.count_braces('{}')


def test_count_braces_3():
    assert 3 == day_09.count_braces('{{}}')


def test_count_braces_6():
    assert 6 == day_09.count_braces("{{{}}}")


def test_count_braces_5():
    assert 5 == day_09.count_braces("{{},{}}")


def test_count_braces_nested():
    assert 8 == day_09.count_braces("{{},{{}}}")

def test_count_brackes_nested_b():
    assert 10 == day_09.count_braces("{{},{{}},{}}")

# def test_count_braces_with_comma():
#     assert 3 == day_09.count_braces("{,,,,{,,,,,},}")

def test_count_braces_16():
    assert 16 == day_09.count_braces("{{{},{},{{}}}}")


def test_count_braces_37():
    assert 37 == day_09.count_braces("{ { { { { {}, {}}, {}, {}}}}}}")

def test_clean_up_01():
    assert '{{},{},{},{}}' == day_09.get_bracketed_value("{{<ab>},{<ab>},{<ab>},{<ab>}}")

def test_clean_up_2():
    assert '{{},{},{},{}}' == day_09.get_bracketed_value("{{<!!>},{<!!>},{<!!>},{<!!>}}")

def test_clean_up_3():
    assert '{{}}' == day_09.get_bracketed_value('{{<a!>},{<a!>},{<a!>},{<ab>}}')
