# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N = int(input())
    sum = 0
    for num in range(1, N+1):
        if num % 2 == 0:
            sum -= num
        else:
            sum += num
    print(f'#{i+1} {sum}')