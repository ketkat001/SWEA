# -*- coding: utf-8 -*-
def my_sort(n):
    result_list = []
    for i in range(len(n)):
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]

    while(True):
        a = n.pop(-1)
        result_list.append(a)
        b = n.pop(0)
        result_list.append(b)
        if len(result_list) == 10:
            break
    return result_list

T = int(input())
for t in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))

    result = ' '.join(map(str, my_sort(N_list)))
    print('#{} {}'.format(t, result))