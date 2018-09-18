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
    tab_param.append(0)
    return tab_param