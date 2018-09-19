def ft_putchar(c):
    if isinstance(c, str) and c != '':
        print(c[0], end='')
    elif isinstance(c, int):
        print(str(c)[0], end='')