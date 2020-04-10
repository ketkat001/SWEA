# 5122. [파이썬 S/W 문제해결 기본] 7일차 - 수열 편집

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    first_list = list(input().split())
    for i in range(M):
        order_list = list(input().split())
        if order_list[0] == "I":
            first_list.insert(int(order_list[1]), order_list[2])
        elif order_list[0] == "D":
            first_list.pop(int(order_list[1]))
        else:
            first_list[int(order_list[1])] = order_list[2]
    if L >= len(first_list):
        print('#{} {}'.format(t, -1))
    else:
        print('#{} {}'.format(t, first_list[L]))