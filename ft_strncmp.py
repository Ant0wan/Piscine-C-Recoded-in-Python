def ft_strcmp(s1, s2, n):
    i = 0
    while s1[i:n] and s2[i:n]:
        if ord(s1[i]) > ord(s2[i]):
            return ord(s1[i]) - ord(s2[i])
        elif ord(s1[i]) < ord(s2[i]):
            return ord(s1[i]) - ord(s2[i])
        else:
            i += 1
    if s1[i:n]:
        return ord(s1[i])
    if s2[i:n]:
        return ord(s2[i]) * -1
    return 0