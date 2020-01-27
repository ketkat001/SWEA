# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N = int(input())

    result = list(map(int, input().split()))

    result.sort(reverse=False)

    print(f'#{i+1}', ' '.join(map(str, result)))