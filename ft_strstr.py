#!/usr/bin/env python

def ft_strstr(str, to_find):
    if to_find not in str:
        return
    else:
        i = 0
        while str[i:]:
            if to_find in str[i:]:
                i += 1
            elif to_find not in str[i:]:
                return str[i - 1]