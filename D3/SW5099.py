# 5099.[파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    waiting = [i for i in range(1, M+1)]
    fire = []
    for n in range(N):
        fire.append(waiting.pop(0))
    idx = 0
    while True:
        cheese[fire[idx]-1] = cheese[fire[idx]-1]//2
        if cheese[fire[idx]-1] == 0:
            result = fire[idx]
            if len(waiting) > 0:
                fire[idx] = waiting.pop(0)
        if sum(cheese)==0:
            break
        idx = (idx+1) % N
    print('#{} {}'.format(t, result))

