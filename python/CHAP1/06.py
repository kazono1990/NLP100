#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ngram(input, n):
    last = len(input) - n + 1
    ret = []
    for i in range(0, last):
        ret.append(input[i:i+n])
    return ret

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(ngram(str1, 2))
Y = set(ngram(str2, 2))

print (X)
print (Y)
print (X.union(Y))
print (X.intersection(Y))
print (X.difference(Y))

# in: X に "se" が含まれていれば True, いなければ False
print ("se" in X)
# in: Y に "se" が含まれていれば True, いなければ False
print ("se" in Y)
