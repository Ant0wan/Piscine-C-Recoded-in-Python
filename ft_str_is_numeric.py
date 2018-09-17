def ft_str_is_numeric(str):
    if str == '':
        return 1
    try:
        if int(str):
            return 1
    except (TypeError, ValueError, AttributeError):
        return 0
    i = 0
    while str[i:]:
        try:
            if int(str[i]) or int(str[i]) == 0:
                i += 1
        except (TypeError, ValueError, AttributeError):
            return 0
    return 1