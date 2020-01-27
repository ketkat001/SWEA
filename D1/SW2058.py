# -*- coding: utf-8 -*-

N = int(input())
result = 0
if N > 9999 and N < 1:
    print(False)
else:
    for i in range(4):
        result += N % 10
        N = int(N / 10)
print(result)