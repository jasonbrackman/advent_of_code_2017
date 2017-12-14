import pytest
from .. import day_14


def test_convert_32_to_128_bytes():

    hash = '61f4c735eec4b9877b124da7486ed701'
    # conv = bin(int(hash, 16))[2:]
    # print(type(conv))

    conv = ''.join([bin(int(x, 16))[2:].zfill(4) for x in hash])

    print(conv)

    assert len(conv) == 128

