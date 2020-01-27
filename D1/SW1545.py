# -*- coding: utf-8 -*-

number = int(input())
number_list = []

for i in range(number, -1, -1):
    number_list.append(i)
print(' '.join(map(str, number_list)))

