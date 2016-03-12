# _*_Coding: utf-8 _*_
from stacks import Stack


def matching_parens(text):
    open_parens = Stack()
    for c in text:
        try:
            if c == "(":
                open_parens.push(c)
            elif c == ")":
                open_parens.pop()
        except AttributeError:
            return -1
    try:
        open_parens.pop()
        return 1
    except AttributeError:
        return 0
