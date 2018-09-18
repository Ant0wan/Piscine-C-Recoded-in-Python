def ft_split(str, charset):
    i = 0
    table = []
    while str[i:]:
        word = []
        while str[i:] and (str[i] not in charset):
            word.append(str[i])
            i += 1
        table.append(''.join(word))
        while str[i:] and (str[i] == ' ' or str[i] == '\t' or str[i] == '\n'):
            i += 1
    return table