# 5108. [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    a_list = list(map(int, input().split()))
    for i in range(M):
        a, b = map(int, input().split())
        a_list.insert(a, b)
    print('#{} {}'.format(t, a_list[L]))
