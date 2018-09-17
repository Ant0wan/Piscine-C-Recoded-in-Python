#!/usr/bin/env python

def ft_is_prime(nb):
    i = 2
    count = 0
    if nb == 0 or nb == 1:
        return 0
    elif nb >= 2:
        while nb % i != 0 and i < nb:
            i += 1
        if i >= nb:
            return 1
        return 0