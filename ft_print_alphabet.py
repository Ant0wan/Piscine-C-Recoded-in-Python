#!/usr/bin/env python

def ft_print_alphabet():
    c = 'a'
    while ord(c) <= ord('z'):
        print(c, end='')
        c = chr(ord(c) + 1)
