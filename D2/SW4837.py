# -*- coding: utf-8 -*-

def subset_sum(n, k):
    a_list = [i for i in range(1, 13)]
    a = len(a_list)
    count = 0
    for i in range(1<<a):
        sum = 0
        sum_list = []
        for j in range(a):
            if i & (1<<j):
                sum_list.append(a_list[j])
                sum += a_list[j]
        if len(sum_list) == n and sum == k:
            count += 1
    return count



T = int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    print('#{} {}'.format(t, subset_sum(N, K)))