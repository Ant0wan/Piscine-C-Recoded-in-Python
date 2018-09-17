#!/usr/bin/env python3

def ft_sqrt(nb):
    i = 1
    if nb <= 0 or nb == 1:
        return 0
    else:
        while nb // i > i:
            i += 1
    if i * i == nb:
        return i
    else:
        return 0