import sys

def ft_strlen(str):
    i = 0
    while str[i:]:
        i += 1
    return i

def ft_split_whitespaces(str):
    i = 0
    table = []
    while str[i:]:
        word = []
        while str[i:] and (str[i] != ' ' and str[i] != '\t' and str[i] != '\n'):
            word.append(str[i])
            i += 1
        table.append(''.join(word))
        while str[i:] and (str[i] == ' ' or str[i] == '\t' or str[i] == '\n'):
            i += 1
    return table

class s_stock_par :
    def __init__(self, argv):
        self.size_param = ft_strlen(argv)
        self.argv = id(argv)
        self.copy = argv
        self.tab = ft_split_whitespaces(argv)

def ft_param_to_tab():
    i = 0
    tab_param = []
    while sys.argv[i:]:
        tab_param.append(s_stock_par(sys.argv[i]))
        i += 1
    tab_param.append(s_stock_par('0'))
    return tab_param