# -*- coding: utf-8 -*-

number = int(input())
result = []
result_number = 1
result.append(result_number)
if number > 30:
    print(False)
else:
    for i in range(1, number+1):
        result_number = result_number * 2
        result.append(result_number)
print(' '.join(map(str, result)))