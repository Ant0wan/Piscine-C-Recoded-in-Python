def ft_show_tab(par):
    i = 0
    while par[i].copy != '0':
        print(par[i].size_param)
        print(par[i].argv)
        print(par[i].copy)
        print(par[i].tab)
        i += 1