# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N = int(input())
    num_list = [2, 3, 5, 7, 11]
    count_list = []
    result = ''

    for num in num_list:
        count = 0
        while(True):
            if N % num == 0:
                N = N / num
                count += 1
            else:
                break
        count_list.append(count)
    result = ' '.join(map(str, count_list))
    print(f'#{i+1} {result}')
