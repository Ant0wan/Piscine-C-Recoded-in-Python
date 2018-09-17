#!/usr/bin/env python

def base_check(base):
    try:
        assert base != ''
        i = 0
        while base[i:]:
            assert base[i] != '+'
            assert base[i] != '-'
            assert base[i] not in base[i + 1:]
            i += 1
        assert i > 1
    except (AssertionError, ValueError, TypeError, AttributeError):
        return 0
    else:
        return 1

def ft_atoi_base(str, base):
    i = 0
    if base_check(base) and str[i:]:
        sign = 1
        while str[i:] and (str[i] == ' ' or str[i] == '\t' or str[i] == '\n' or str[i] == '\v' or str[i] == '\f'):
            i += 1
        if str[i:] and (str[i] == '-' or str[i] == '+'):
            sign = -1 if str[i] == '-' else 1
            i += 1
        length_base = 0
        while base[length_base:]:
            length_base += 1
        if str[i:]:
            number = 0
        else:
            return None
        while str[i:] and str[i] in base:
            number = number * length_base + base.index(str[i])
            i += 1
        return number * sign
    else:
        return None