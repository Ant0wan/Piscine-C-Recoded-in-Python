#!/usr/bin/env python

def ft_sort_integer_table(table, size):
    i = 1
    tmp = 0
    diff = 1
    cp_table = table
    while diff > 0:
        diff = 0
        i = 1
        while i < size:
            if cp_table[i - 1] > cp_table[i]:
                diff += 1
                tmp = cp_table[i - 1]
                cp_table[i - 1] = cp_table[i]
                cp_table[i] = tmp
            i += 1
    return cp_table