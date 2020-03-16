T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    map_list = [list(input()) for _ in range(N)]
    w, b, r = 0, 0, 0
    min_cnt = 100000
    color = [[],[],[]]
    for x in range(N):
        color[0].append(M - map_list[x].count('W'))
    for x in range(N):
        color[1].append(M - map_list[x].count('B'))
    for x in range(N):
        color[2].append(M - map_list[x].count('R'))
    for i in range(0, N-2):
        cnt = 0
        for j in range(i+1, N-1):
            cnt = sum(color[0][:i+1]) + sum(color[1][i+1:j+1]) + sum(color[2][j+1:])
            if cnt < min_cnt:
                min_cnt = cnt
    print('#{} {}'.format(t, min_cnt))
