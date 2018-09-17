#!/usr/bin/env python3

def ft_ﬁbonacci(index):
    if index < 0:
        return -1
    if index == 0:
        return 0
    if index == 1:
        return 1
    return ft_ﬁbonacci(index - 1) + ft_ﬁbonacci(index - 2)