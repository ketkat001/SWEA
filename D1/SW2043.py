# -*- coding: utf-8 -*-

P, K = map(int, input().split())
result = 0
if P < K :
    print(False)
elif P > 999 or P < 0:
    print(False)

for i in range(P-K+1):
    if (P - K) >= 0:
        result += 1
        K += 1

print(result)
