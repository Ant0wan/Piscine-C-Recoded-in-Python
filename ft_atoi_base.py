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

def ft_batoi(str):
    i = 0
    sign = 1
    number = []
    while str[i] == ' ' or str[i] == '\t' or str[i] == '\n' or str[i] == '\v' or str[i] == '\f':
        i += 1
    if str[i] == '-' or str[i] == '+':
        sign = -1 if str[i] == '-' else 1
        i += 1
    while str[i].isdigit():
        number.append(str[i])
        i += 1
    try:
        return int(''.join(number)) * sign
    except (TypeError, ValueError, AttributeError):
        return

def ft_readnbr_base(nbr, base):
    if base_check(base):
        if isinstance(nbr, str):
            inbr = int(nbr)
        else:
            inbr = nbr
        nbr_base = []
        rest = inbr * -1 if inbr < 0 else inbr
        i = 0
        while base[i:]:
            i += 1
        while rest != 0:
            nbr_base.insert(0, base[rest % i])
            rest = rest // i
        if inbr < 0:
            nbr_base.insert(0, '-')
        return ''.join(nbr_base)
    else:
        return 0

def ft_atoi_base(str, base):
    if base_check(base):
        i = 0
        sign = 1
        number = []
        while str[i] == ' ' or str[i] == '\t' or str[i] == '\n' or str[i] == '\v' or str[i] == '\f':
            i += 1
        if str[i] == '-' or str[i] == '+':
            sign = -1 if str[i] == '-' else 1
            i += 1
        while str[i:] and str[i] in base:
            i += 1
        return 'ok'

print(ft_atoi_base('    -1E49EA', '0123456789ABCDEF'))
