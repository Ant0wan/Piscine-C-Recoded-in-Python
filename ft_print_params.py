#!/usr/bin/env python

import sys

def ft_print_params():
    i = 0
    while sys.argv[i:]:
        print(sys.argv[i], end='\n')
        i += 1

def main():
    ft_print_params()

if __main__ == '__main__':
    main()