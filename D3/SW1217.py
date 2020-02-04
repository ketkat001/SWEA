# -*- coding: utf-8 -*-
def square(x, y):
    num = x
    if y==1:
        return x
    else:
        return square(x * num, y-1)





for t in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    print('#{} {}'.format(T, square(N, M)))