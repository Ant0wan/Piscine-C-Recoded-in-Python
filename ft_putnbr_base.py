#!/usr/bin/env python

def base_check(base):
    try:
        assert base != ''
        i = 0
        while base[i:]:
            assert base[i] != '+'
            assert base[i] != '-'
            i += 1
        assert i > 1
    except (AssertionError, ValueError, TypeError, AttributeError):
        return 0
    else:
        return 1

def ft_putnbr_base(nbr, base):
    if base_check(base):
        #code here
    else:
        return 0
