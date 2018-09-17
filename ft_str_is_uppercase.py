def ft_str_is_uppercase(str):
    if str == '':
        return 1
    else:
        i = 0
        while str[i:]:
            if str[i] >= 'A' and str[i] <= 'Z':
                i += 1
            else:
                return 0
        return 1