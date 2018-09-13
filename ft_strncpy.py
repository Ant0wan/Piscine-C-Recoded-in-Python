#!/usr/bin/env python

def ft_strncpy(src, dest):
    i = 0
    try:
        while src[i:]:
            dest.append(src[i])
            i += 1
        return ''.join(dest)
    except (TypeError, ValueError, AttributeError):
        try:
            return dest + src
        except (TypeError, ValueError, AttributeError):
            return