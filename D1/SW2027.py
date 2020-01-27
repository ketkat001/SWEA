# -*- coding: utf-8 -*-

result_list = ['+', '+', '+', '+', '+']
for i in range(0,5,1):
    result_list[i] = '#'
    print(''.join(map(str, result_list)))
    result_list[i] = '+'
