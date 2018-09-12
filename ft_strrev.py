#!/usr/bin/env python

def ft_strrev(str):
    a = 0
    i = 0
    while str[i:]:
        i += 1
    tmp_str = [''] * i
    i -= 1
    while a <= i:
        tmp_str[a] = str[i - a]
        a += 1
    return ''.join(tmp_str)