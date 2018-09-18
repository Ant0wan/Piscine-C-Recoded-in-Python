#!/usr/bin/env python3

import sys

class s_stock_par :
    def __init__(self, argv):
        self.argv = argv

def ft_param_to_tab():
    i = 0
    tab_param = []
    while sys.argv[i:]:
        tab_param.append(s_stock_par(sys.argv[i]))

        i += 1
    return tab_param

def main():
    print(ft_param_to_tab())

if __name__ == "__main__":
    main()