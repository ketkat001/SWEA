# -*- coding: utf-8 -*-
def square(x, n, y):
    n = n*x
    if y == 1:
        return n
    else:
        return square(x, n, y-1)

for t in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    num = 1
    print('#{} {}'.format(T, square(N, num, M)))