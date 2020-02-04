# -*- coding: utf-8 -*-
def color_p(L):
    result_list = [[0]*10 for _ in range(10)]
    count = 0
    for i in range(len(L)):
        c = L[i][4]
        for x in range(L[i][0], L[i][2]+1):
            for y in range(L[i][1], L[i][3]+1):
                result_list[x][y] += c
    for x in range(10):
        for y in range(10):
            if result_list[x][y] == 3:
                count += 1
    return count



T = int(input())
for t in range(1, T+1):
    N = int(input())
    N_list = []
    for i in range(N):
        P_list = list(map(int, input().split()))
        N_list.append(P_list)
    print('#{} {}'.format(t ,color_p(N_list)))