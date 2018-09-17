#!/usr/bin/env python

def ft_strcapitalize(str):
    cp_str = []
    i = 0
    while str[i:]:
        if i == 0 and (str[i] >= 'a' and str[i] <= 'z'):
            cp_str.append(chr(ord(str[i]) - ord('a') + ord('A')))
        elif i > 0 and (str[i - 1] == ' ' or str[i - 1] == '-' or str[i - 1] == '+') and (str[i] >= 'a' and str[i] <= 'z'):
            cp_str.append(chr(ord(str[i]) - ord('a') + ord('A')))
        elif i > 0 and (str[i - 1] != ' ' and str[i - 1] != '-' and str[i - 1] != '+') and (str[i] >= 'A' and str[i] <= 'Z'):
            cp_str.append(chr(ord(str[i]) - ord('A') + ord('a')))
        else:
            cp_str.append(str[i])
        i += 1
    return ''.join(cp_str)
