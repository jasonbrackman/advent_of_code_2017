# coding=utf-8
from .. import day_01
import pytest


@pytest.mark.parametrize('param, expected', [(12, 0),
                                             (11, 2),
                                             (22, 4),
                                             (122, 2),
                                             (1122, 3),
                                             (1111, 4),
                                             (1234, 0),
                                             (91212129, 9)
                                             ])
def test_captcha(param, expected):
    assert expected == day_01.captcha(param)


@pytest.mark.parametrize('param, expected', [(1212, 6),
                                             (1221, 0),
                                             (123425, 4),
                                             (123123, 12),
                                             (12131415, 4)
                                             ])

def test_captcha_halfway_round(param, expected):
    assert expected == day_01.captcha_halfway_round(param)