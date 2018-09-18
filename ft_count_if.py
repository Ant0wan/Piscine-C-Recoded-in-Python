def ft_count_if(tab, f):
    i = 0
    p = 0
    while tab[i:]:
        if f(tab[i]) == 1:
            p = 1
        i += 1
    return p