#!/usr/bin/env python3

import sys

def ft_rev_params():
    i = 1
    while sys.argv[i:]:
        i += 1
    while i > 1:
        i -= 1
        print(sys.argv[i], end='\n')

def main():
    ft_rev_params()

if __name__ == '__main__':
    main()
