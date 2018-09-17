#!/usr/bin/env python3

def ft_iterative_factorial(nb):
    if nb == 0:
        return 1
    if nb < 0:
        return 0
    else:
        i = nb
        result = nb
        while i > 1:
            i -= 1
            result = result * i
        return result