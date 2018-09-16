#!/usr/bin/env python

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

def ft_print_memory(addr, size):
    i = 0
    hex_cont = []
    while i <= 16:
        hex_cont.append('0')
        i += 1
    return print(addr)
# Need to code with C some extensions...



ligne = 'Salut les aminches c\'est cool show mem on fait de truc terrible.'
print(len(ligne))
print(id(ligne), id(ligne[0]), id(ligne[1]))
print(ligne[0], ft_putnbr_base(ord(ligne[1]), BASE))
#ft_print_memory(120, 10)