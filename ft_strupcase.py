#!/usr/bin/env python

def ft_strupcase(str):
    i = 0
    cp_str = []
    while str[i:]:
        if str[i] >= 'a' and str[i] <= 'z':
            cp_str.append(chr(ord(str[i]) - ord('a') + ord('A')))
            i += 1
        else:
            cp_str.append(str[i])
            i += 1
    return ''.join(cp_str)