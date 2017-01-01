#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ngram(input, n):
    last = len(input) - n + 1
    ret = []
    for i in range(0, last):
        ret.append(input[i:i+n])
    return ret

str = "I am an NLPer"

# 単語 N グラムを実行するための前処理 (空白で文字列を分割し、リストに格納)
list = str.split()
print (ngram(list, 2))

# 文字 N グラムを実行するための前処理 (空白文字を除去し 'IamanNLPer' のように文字列を修正)
str = str.replace(' ', '')
print (ngram(str, 2))
