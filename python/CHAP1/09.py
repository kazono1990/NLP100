#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

def shuffle(word):
    if len(word) < 5:
        return word

    middle = list(word[1:-1])
    while middle == list(word[1:-1]):
        random.shuffle(middle)
    return word[0] + "".join(middle) + word[-1]


def typoglycemia(str):
    list = []
    for word in str.split():
        list.append(shuffle(word))
    return " ".join(list)


str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(str))
