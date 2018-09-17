#!/usr/bin/env python

def ft_ultimate_div_mod(a, b):
    tmp_a = a[0]
    a[0] = a[0] / b[0]
    b[0] = tmp_a % b[0]