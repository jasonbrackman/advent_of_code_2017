import pytest
from .. import day_04



"""
aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - 
"""

"""
    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
"""
@pytest.mark.parametrize('param, expect', [('abcde fghij', 1),
                                           ('abcde xyz ecdab', 0),
                                           ('a ab abc abd abf abj', 1),
                                           ('iiii oiii ooii oooi oooo', 1),
                                           ('oiii ioii iioi iiio', 0),
                                           ('oaoe rxeq vssdqtu xrk cjv yaoqp loo', 1),
                                           ('abcde fghij\nabcde xyz ecdab\na ab abc abd abf abj\niiii oiii ooii oooi oooo', 3)])
def test_something(param, expect):
    assert expect == day_04.do_work(param, ag=True)