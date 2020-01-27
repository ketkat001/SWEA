# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    s = 0
    N = list(map(int, input().split()))
    N.sort()
    s = int(sum(N[1:len(N)-1]))
    result = round(s/(len(N)-2))
    print(f'#{i+1} {result}')