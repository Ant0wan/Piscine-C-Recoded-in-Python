def base_check(base):
    try:
        assert base != ''
        i = 0
        while base[i:]:
            assert base[i] != '+'
            assert base[i] != '-'
            assert base[i] not in base[i + 1:]
            i += 1
        assert i > 1
    except (AssertionError, ValueError, TypeError, AttributeError):
        return 0
    else:
        return 1

def ft_putnbr_base(nbr, base):
    if base_check(base):
        if isinstance(nbr, str):
            inbr = int(nbr)
        else:
            inbr = nbr
        nbr_base = []
        rest = inbr * -1 if inbr < 0 else inbr
        i = 0
        while base[i:]:
            i += 1
        while rest != 0:
            nbr_base.insert(0, base[rest % i])
            rest = rest // i
        if inbr < 0:
            nbr_base.insert(0, '-')
        return ''.join(nbr_base)
    else:
        return 0

def ft_convert_base(nbr, base_from, base_to):
    i = 0
    if base_check(base_from) and base_check(base_to) and nbr[i:]:
        sign = 1
        if nbr[i] == '-' or nbr[i] == '+':
            sign = -1 if nbr[i] == '-' else 1
            i += 1
        len_base_from = 0
        while base_from[len_base_from:]:
            len_base_from += 1
        if nbr[i:]:
            number_b10 = 0
        else:
            return None
        while nbr[i:]:
            number_b10 = number_b10 * len_base_from + base_from.index(nbr[i])
            i += 1
        return ft_putnbr_base(number_b10, base_to)
    else:
        return None