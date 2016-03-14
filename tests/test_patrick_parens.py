# _*_ Coding: utf-8 _*_

import pytest

STRINGS = [
    ('((()))()((()()))', 0),
    (')()()()()()(())(', -1),
    ('(()()()()()', 1)
]

@pytest.mark.parametrize('a, b', STRINGS)
def test_parens_counter(a, b):
    from src.patrick_parens.py import parens_counter
    assert parens_counter(a) == b 