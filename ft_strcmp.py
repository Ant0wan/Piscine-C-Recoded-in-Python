#!/usr/bin/env python3

def ft_strcmp(s1, s2):
    i = 0
    while s1[i:] and s2[i:]:
        if ord(s1[i]) > ord(s2[i]):
            return ord(s1[i]) - ord(s2[i])
        elif ord(s1[i]) < ord(s2[i]):
            return ord(s1[i]) - ord(s2[i])
        else:
            i += 1
    if s1[i:]:
        return ord(s1[i])
    if s2[i:]:
        return ord(s2[i]) * -1
    return 0