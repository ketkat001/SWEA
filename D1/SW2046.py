# -*- coding: utf-8 -*-

N = int(input())
result = []

if N > 100000:
    print(False)

for i in range(N):
    result.append('#')

print(''.join(result))
