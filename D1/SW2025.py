# -*- coding: utf-8 -*-

N = int(input())
result = 0
if N > 10000:
    print(False)

for i in range(1, N+1):
    result += i

print(result)