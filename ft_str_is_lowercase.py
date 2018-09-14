#!/usr/bin/env python

def ft_str_is_lowercase(str):
    if str == '':
        return 1
    else:
        i = 0
        while str[i:]:
            if str[i] >= 'a' and str[i] <= 'z':
                i += 1
            else:
                return 0
        return 1