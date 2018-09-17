#!/usr/bin/env python3

NON_PRINTABLE = lambda x: True if (ord(x) >= 0 and ord(x) < 32) else False
BASE = '0123456789abcdef'

def ft_putnbr_base(nbr, base):
    nbr_base = []
    rest = nbr
    i = 0
    while base[i:]:
        i += 1
    while rest != 0:
        nbr_base.insert(0, base[rest % i])
        rest = rest // i
    return ''.join(nbr_base)

def ft_putstr_non_printable(str):
    if str != '':
        cp_str = []
        i = 0
        while str[i:]:
            if NON_PRINTABLE(str[i]):
                add = ft_putnbr_base(ord(str[i]), BASE)
                special = '0' if ord(str[i]) <= 15 else ''
                cp_str.append('\\' + special + add)
            else:
                cp_str.append(str[i])
            i += 1
        return ''.join(cp_str)
    else:
        return None