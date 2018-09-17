#!/usr/bin/env python3

def ft_str_is_printable(str):
    if str == '':
        return 1
    else:
        i = 0
        while str[i:]:
            if ord(str[i]) > 0 and ord(str[i]) < 32:
                return 0
            else:
                i += 1
        return 1