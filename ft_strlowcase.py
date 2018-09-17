#!/usr/bin/env python

def ft_strlowercase(str):
    i = 0
    cp_str = []
    while str[i:]:
        if str[i] >= 'A' and str[i] <= 'Z':
            cp_str.append(chr(ord(str[i]) - ord('A') + ord('a')))
            i += 1
        else:
            cp_str.append(str[i])
            i += 1
    return ''.join(cp_str)