#!/usr/bin/python
# -*- coding: utf-8 -*-

patrol_car = 'パトカー'
taxi = 'タクシー'
ans = ''

for str1, str2 in zip(patrol_car, taxi):
    ans += str1 + str2

print (ans);
