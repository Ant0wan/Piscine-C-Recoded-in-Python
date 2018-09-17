#!/usr/bin/env python3

import sys

def ft_strcmp(s1, s2):
    i = 0
    while s1[i:] and s2[i:]:
        if ord(s1[i]) > ord(s2[i]):
            return ord(s1[i]) - ord(s2[i])
        elif ord(s1[i]) < ord(s2[i]):
            return ord(s1[i]) - ord(s2[i])
        else:
            i += 1
    if s1[i:]:
        return ord(s1[i])
    if s2[i:]:
        return ord(s2[i]) * -1
    return 0

def ft_sort_table(table, size):
    i = 1
    tmp = 0
    diff = 1
    cp_table = table
    while diff > 0:
        diff = 0
        i = 1
        while i < size:
            if ft_strcmp(cp_table[i - 1], cp_table[i]) > 0:
                diff += 1
                tmp = cp_table[i - 1]
                cp_table[i - 1] = cp_table[i]
                cp_table[i] = tmp
            i += 1
    return cp_table

def ft_sort_params():
    i = 1
    cp_arg = []
    while sys.argv[i:]:
        cp_arg.append(sys.argv[i])
        i += 1
    cp_arg = ft_sort_table(cp_arg, i - 1)
    return '\n'.join(cp_arg)

def main():
    print(ft_sort_params())

if __name__ == '__main__':
    main()
