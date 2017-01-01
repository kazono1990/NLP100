#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cipher(input):
    ret = ''
    for char in input:
        ret += chr(219 - ord(char)) if char.islower() else char
    return ret

str = 'Hello, world!'

print (cipher(str))
print (cipher(cipher(str)))
