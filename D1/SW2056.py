# -*- coding: utf-8 -*-

T = int(input())
month_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(T):
    date = input()
    month = int(date[4:6])
    day = int(date[6:8])
    F = '-1'
    if month > 0 and month < 13 and day > 0 and day < (month_date[month-1]) + 1:
        print(f'#{i+1} {date[0:4]}/{date[4:6]}/{date[6:8]}')
    else:
        print(f'#{i+1} {F}')


