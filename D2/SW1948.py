# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    Month_1, Day_1, Month_2, Day_2 = map(int, input().split())
    num, n = 0, 1
    result = 0
    date_list = []
    for x in range(1,13):
        store_list = []
        if x in (1,3,5,7,8,10,12):
            num = 31
        elif x in (4,6,9,11):
            num = 30
        else:
            num = 28
        for j in range(1, num+1):
            store_list.append(n)
            n = n + 1
        date_list.append(store_list)

    result = date_list[Month_2 - 1][(Day_2) - 1] - date_list[Month_1 - 1][(Day_1) - 1] + 1


    print(f'#{i+1} {result}')