#!/usr/bin/env python

def ft_print_reverse_alphabet():
    c = 'z'
    while ord(c) >= ord('a'):
        print(c, end='')
        c = chr(ord(c) - 1)
