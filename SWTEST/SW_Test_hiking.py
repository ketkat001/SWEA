def find_hiking(p, q, k):
    hike_queue = [(p, q)]
    




dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
result = [0]
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    hiking_list = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0
    start = []
    for i in range(N):
        if max_value < max(hiking_list[i]):
            max_value = max(hiking_list[i])
    for i in range(N):
        for j in range(N):
            if hiking_list[i][j] == max_value:
                start.append((i, j))
    for p in range(len(start)):
        start_x = start[p][0]
        start_y = start[p][1]
        find_hiking(start_x, start_y, K)