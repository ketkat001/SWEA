# -*- coding: utf-8 -*-

for i in range(10):

    T = int(input())
    T_list = list(map(int, input().split()))

    result_sum = 0

    for x in range(2, T-1):
        b_list = []
        if T_list[x] > T_list[x-1] and T_list[x] > T_list[x-2] and T_list[x] > T_list[x+1] and T_list[x] > T_list[x+2]:
            for y in range(1, 3):
                b_list.append(T_list[x]-T_list[x-y])
                b_list.append(T_list[x]-T_list[x+y])
            result_sum += min(b_list)

    print(f'#{i+1} {result_sum}')


