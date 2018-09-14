#!/usr/bin/env python

def ft_str_is_alpha(str):
    i = 0
    while str[i:]:
        if str[i] < 'A' or (str[i] > 'Z' and str[i] < 'a') or str[i] > 'z':
            return 0
        i += 1
    return 1