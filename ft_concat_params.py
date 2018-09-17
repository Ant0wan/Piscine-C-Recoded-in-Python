import sys

def ft_print_params():
    i = 1
    while sys.argv[i:]:
        print(sys.argv[i], end='\n')
        i += 1