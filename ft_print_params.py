#!/usr/bin/env python3

import sys

def ft_print_params():
    i = 0
    while sys.argv[i:]:
        print(sys.argv[i], end='\n')
        i += 1

def main():
    ft_print_params()

if __name__ == '__main__':
    main()
