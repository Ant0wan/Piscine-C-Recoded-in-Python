#!/usr/bin/env python3

import sys

def ft_add(a, b):
    return a + b

def ft_sub(a, b):
    return a - b

def ft_mul(a, b):
    return a *b

def ft_div(a,b):
    return a // b

def ft_mod(a, b):
    return a % b

def ft_usage():
    return None

funcdict = {
    '+': ft_add,
    '-': ft_sub,
    '*': ft_mul,
    '/': ft_div,
    '%': ft_mod,
    '': ft_usage
}

def main():
    i = 0
    while sys.argv[i:]:
        i += 1
    if i != 3:
        return None
    else:
        if isinstance(sys.argv[1], int) and (sys.argv[2] in list(funcdict.keys())) and isinstance(sys.argv[3], int):
            if sys.argv[2] == '/' and int(sys.argv[3]) == 0:
                print('Stop : division by zero')
            elif sys.argv[2] == '%' and int(sys.argv[3]) == 0:
                print('Stop : modulo by zero ')
            else:
                print(funcdict[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3])))
        else:
            return None

if __name__ == '__main__':
    main()