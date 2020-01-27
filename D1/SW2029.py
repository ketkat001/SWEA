# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    if a and b > 10000 or a and b < 1:
        print(False)
    print(f'#{i+1} {int(a/b)} {a%b}')
