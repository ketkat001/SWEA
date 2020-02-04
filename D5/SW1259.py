# -*- coding: utf-8 -*-
T = int(input())
for t in range(1, T+1):
    n = int(input())
    n_list = list(map(int, input().split()))

    x_list = []
    y_list = []
    for i in range(len(n_list)):
        if i % 2 == 0:
            x_list.append(n_list[i])
        else:
            y_list.append(n_list[i])

    result_list = []

    for i in range(n):
        if x_list[i] not in y_list:
            a = x_list.pop(i)
            b = y_list.pop(i)
            result_list.append(a)
            result_list.append(b)
            break

    while(len(x_list) > 0):
        for i in range(len(x_list)):
            if result_list[-1] == x_list[i]:
                a = x_list.pop(i)
                b = y_list.pop(i)

                result_list.append(a)
                result_list.append(b)
                break

    result = ' '.join(map(str, result_list))
    print(f'#{t} {result}')


