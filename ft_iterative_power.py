def ft_iterative_power(nb, power):
    if power == 0:
        return 1
    elif nb == 0:
        return  0
    else:
        return nb ** power