# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    flies = []
    for j in range(N):
        flies.append(list(map(int, input().split())))       # N * N 의 배열 완성

    dies = []

    for x in range(N-M+1):
        for y in range(N-M+1):
            s = 0
            for m in range(M):
                s += sum(flies[x+m][y:y+M])
            dies.append(s)
    print(f'#{i+1} {max(dies)}')
