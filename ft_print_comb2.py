# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_print_comb2.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abarthel@42.fr                             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 12/09/2018                               #+#    #+#              #
#    Updated: 12/09/2018                              ###   ########.fr        #
#                                                                              #
# ############################################################################ #

#!/usr/bin/env python

def ft_print_comb2():
    c = ', '
    number_one = 0
    number_two = 0
    while number_one <= 98:
        while number_two < 99:
            number_two += 1
            if number_one == 98:
                c = ''
            print("%02d %02d" %(number_one, number_two), end=c)
        number_one += 1
        number_two = number_one