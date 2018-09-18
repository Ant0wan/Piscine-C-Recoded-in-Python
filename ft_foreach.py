def ft_foreach(tab, length, f):
    i = 0
    while i < length:
        f(tab[i])
        i += 1