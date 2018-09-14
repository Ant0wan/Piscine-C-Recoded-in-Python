#!/usr/bin/env python

def base_check(base):
    if base == '':
        return 0
    i = 0
    p = 0
    while base[i:]:
        if base[i] == '+' or base[i] == '-':
            p = 1
        i += 1
    elif i == 1 or p == 1:
        return 0


def ft_putnbr_base(nbr, base):
    if base_check(base) == 0:
        return 0
    else:
