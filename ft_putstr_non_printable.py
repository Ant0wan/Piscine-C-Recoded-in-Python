NON_PRINTABLE = lambda x: True if (ord(x) >= 0 and ord(x) < 32) else False

def ft_putstr_non_printable(str):
    if str != '':
        cp_str = []
        i = 0
        while str[i:]:
            if NON_PRINTABLE(str[i]):
                cp_str.append('N')
            else:
                cp_str.append(str[i])
            i += 1
        return ''.join(cp_str)
    else:
        return None

print(ft_putstr_non_printable('Hello'))