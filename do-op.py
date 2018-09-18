#!/usr/bin/env python3

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

class g_opptab:
    def __int__(self):
        self.ok = ''

def main():
    print(funcdict['-'])

if __name__ == '__main__':
    main()