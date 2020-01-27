# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N = int(input())
    N_list = map(int, input().split())
    N_list = list(N_list)

    max_price = N_list[N - 1]
    num_price = 0
    num = 0
    result = 0

    for x in range(N-2, -1, -1):

        if N_list[x] > max_price:
            if num != 0:                                   # max_price가 변할 때 num값이 0이 아닌경우 result 값에 저장
                result += max_price * num - num_price
                num = 0
                num_price = 0                             # result 값에 저장 후 num값과 num_price값을 0으로 초기화
            else:
                pass
            max_price = N_list[x]
        elif N_list[x] < max_price or N_list[x] == max_price:
            num_price = num_price + N_list[x]
            num += 1

    result = result + (max_price * num) - num_price
    print(f'#{i+1} {result}')

