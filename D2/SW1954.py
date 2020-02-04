# -*- coding: utf-8 -*-

def snail_list(n):
    s_list = [[0]*n for i in range(n)]

    num = 1
    dir_list =[(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    l_num1, l_num2 = 0, -1

    while(n*n >= num):
        dir = dir_list[direction]
        x_num = l_num1 + dir[0]
        y_num = l_num2 + dir[1]


        if x_num < 0 or y_num < 0 or x_num >= n or y_num >=n or s_list[x_num][y_num] != 0:
            direction += 1
            if direction == 4:
                direction = 0
        else:
            l_num1, l_num2 = x_num, y_num
            s_list[l_num1][l_num2] = num
            num += 1
    return s_list



T = int(input())
for i in range(T):
    N = int(input())
    result = snail_list(N)

    print(f'#{i+1}')
    for x in range(N):
        print(' '.join(map(str, result[x])))





        