# _*_ Coding: utf-8 _*_

def parens_counter(string):
    counter = 0
    for i in string:
        if counter < 0:
            return -1
        else:
            if i == '(':
                counter += 1
            if i == ')':
                counter -= 1
    if counter > 0:
        return 1
    else:
        return 0