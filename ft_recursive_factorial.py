def ft_recursive_factorial(nb):
    if nb == 0:
        return 1
    elif nb < 0:
        return 0
    else:
        return (nb * ft_recursive_factorial(nb - 1))