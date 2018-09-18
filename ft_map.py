def ft_map(tab, length, f):
    i = 0
    cp_tab = tab
    while i < length:
        cp_tab[i] = f(cp_tab[i])
        i += 1
    return cp_tab