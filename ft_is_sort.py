def ft_is_sort(tab, length, f):
    i = 1
    while i < length:
        if f(tab[i - 1], tab[i]) < 0:
            d = 1
        elif f(tab[i - 1], tab[i]) > 0:
            c = 1
        i += 1
    if (d and c):
        return 0
    if (d and not c) or (c and not d):
        return 1
    if (not d and not c):
        return 1
    return None