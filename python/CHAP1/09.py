#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = str.split()
shuffle = []

for word in words:
    if len(word) < 5:
        pass
    else:
        char_list = list(word)
        mid_list = char_list[1:-1]
        random.shuffle(mid_list)
        word = word[0] + "".join(mid_list) + word[-1]
    shuffle.append(word)

ans = " ".join(shuffle)
print (ans)
