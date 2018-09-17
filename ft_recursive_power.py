#!/usr/bin/env python3

def ft_recursive_power(nb, power):
    if power == 0:
        return 1
    elif nb == 0:
        return 0
    else:
        return nb * ft_recursive_power(nb, power - 1)