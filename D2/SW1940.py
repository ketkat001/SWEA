# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N = int(input())
    car_distance = 0
    speed_count = 0
    for x in range(N):
        command_list = list(map(int, input().split()))
        if command_list[0] == 0:
            car_distance += speed_count
        elif command_list[0] == 1:
            speed_count = speed_count + command_list[1]
            car_distance += speed_count
        elif command_list[0] == 2:
            if command_list[1] > speed_count:
                speed_count = 0
            else:
                speed_count = speed_count - command_list[1]
                car_distance += speed_count
    print(f'#{i+1} {car_distance}')



