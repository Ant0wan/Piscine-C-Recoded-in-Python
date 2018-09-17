#!/usr/bin/env python

import sys

def ft_rev_params():
    i = 0
    while sys.argv[i:]:
        i += 1
    while i > 0:
        i -= 1
        print(sys.argv[i], end='\n')

def main():
    ft_rev_params()

if __main__ == '__main__':
    main()