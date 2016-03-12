# _*_Coding: utf-8 _*_
import pytest


PAREN_LIST = [
    ("()()()", 0),
    ("(((((())))))", 0),
    ("()", 0),
    ("((()()))", 0),
    (")()()(", -1),
    ("((())))", -1),
    ("()()())", -1),
    ("())()())", -1),
    ("(()()()", 1),
    ("(((()))", 1),
    ("(()((())", 1),
]


@pytest.mark.parametrize('a, b', PAREN_LIST)
def test_matching_parens(a, b):
    from src.selena_parens import matching_parens
    assert matching_parens(a) == b
