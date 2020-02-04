# -*- coding: utf-8 -*-

for i in range(10):
    T = int(input())
    T_list = []
    for x in range(100):
        T_list.append(list(map(int, input().split())))

    result_list = []

    for x in range(100):
        sum = 0
        for y in range(100):
            sum += T_list[x][y]
        result_list.append(sum)

    for x in range(100):
        sum = 0
        for y in range(100):
            sum += T_list[y][x]
        result_list.append(sum)

    sum = 0
    for x in range(100):
        sum += T_list[x][99-x]
    result_list.append(sum)


    sum = 0
    for x in range(100):
        sum += T_list[x][x]
    result_list.append(sum)


    print(f'#{T} {max(result_list)}')