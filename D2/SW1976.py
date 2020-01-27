# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    time_1, min_1, time_2, min_2 = map(int, input().split())

    result_time = 0
    result_min = 0
    time_up = 0

    if min_1 + min_2 > 60:
        result_min = min_1 + min_2 - 60
        time_up = 1
    else:
        result_min = min_1 + min_2

    if time_1 + time_2 + time_up > 12:
        result_time = time_1 + time_2 + time_up - 12
    else:
        result_time = time_1 + time_2 + time_up

    print(f'#{i+1} {result_time} {result_min}')