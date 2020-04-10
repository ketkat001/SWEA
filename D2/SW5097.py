# [파이썬 S/W 문제해결 기본] 6일차 - 회전
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Que = list(input().split())
    for m in range(M):
        a = Que.pop(0)
        Que.append(a)
    print('#{} {}'.format(t, Que[0]))