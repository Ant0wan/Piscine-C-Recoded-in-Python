def ft_print_comb():
    n = 3
    i = 0
    c = ', '
    numbers = []
    while i < n:
        numbers.append(0)
        i += 1
    while numbers[0] <= 7:
        numbers[1] = numbers[0] + 1
        while numbers[1] <= 8:
            numbers[2] = numbers[1] + 1
            while numbers[2] <= 9:
                if numbers[0] == 7:
                    c = ''
                print(numbers[0], numbers[1], numbers[2], sep='', end=c)
                numbers[2] += 1
            numbers[1] += 1
        numbers[0] += 1
