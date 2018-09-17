#!/usr/bin/env python

def ft_atoi(str):
    i = 0
    sign = 1
    number = []
    while str[i:] and (str[i] == ' ' or str[i] == '\t' or str[i] == '\n' or str[i] == '\v' or str[i] == '\f'):
        i += 1
    if str[i:] and (str[i] == '-' or str[i] == '+'):
        sign = -1 if str[i] == '-' else 1
        i += 1
    while str[i:] and str[i].isdigit():
        number.append(str[i])
        i += 1
    try:
        return int(''.join(number)) * sign
    except (TypeError, ValueError, AttributeError):
        return None