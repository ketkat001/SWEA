# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    sum_list = []

    a = 0

    if len(A_list) > len(B_list):
        a = len(A_list) - len(B_list)
        for x in range(a+1):
            sum = 0
            for y in range(len(B_list)):
                sum += (A_list[y+x] * B_list[y])
            sum_list.append(sum)

    else:
        a = len(B_list) - len(A_list)
        for x in range(a+1):
            sum = 0
            for y in range(len(A_list)):
                sum += (B_list[y + x] * A_list[y])
            sum_list.append(sum)

    print(f'#{i+1} {max(sum_list)}')