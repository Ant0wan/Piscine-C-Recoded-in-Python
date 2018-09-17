#!/usr/bin/env python3

def ft_strncpy(src, dest, n):
    i = 0
    try:
        while src[i:] and i < n:
            dest.append(src[i])
            i += 1
        return ''.join(dest)
    except (TypeError, ValueError, AttributeError):
        try:
            return dest + src[:n]
        except (TypeError, ValueError, AttributeError):
            return