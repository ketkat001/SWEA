# -*- coding: utf-8 -*-

for t in range(1, 11):
    T = int(input())
    T_list = list(map(int, input().split()))
    sum = 0

    for i in range(2, T-2):
        store_list = []
        if T_list[i] > T_list[i-1] and T_list[i] > T_list[i-2] and T_list[i] > T_list[i+1] and T_list[i] > T_list[i+2]:
             for j in range(1, 3):
                 store_list.append(T_list[i] - T_list[i-j])
                 store_list.append(T_list[i] - T_list[i+j])
             sum = sum + min(store_list)

    print(f'#{t} {sum}')