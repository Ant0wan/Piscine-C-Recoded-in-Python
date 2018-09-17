def ft_is_prime(nb):
    i = 2
    count = 0
    if nb == 0 or nb == 1:
        return 0
    elif nb >= 2:
        while nb % i != 0 and i < nb:
            i += 1
        if i >= nb:
            return 1
        return 0

def ft_ﬁnd_next_prime(nb):
    if ft_is_prime(nb):
        return nb
    else:
        return ft_ﬁnd_next_prime(nb + 1)