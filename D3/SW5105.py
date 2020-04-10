# 5105.[파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
def is_wall(x, y):
    if 0 <= x < N and 0 <= y < N and visited[x][y] == 0 and miro[x][y] != 1:
        return True
    return False


dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    queue = []
    result = 0
    flag = 0
    for i in range(N):
        if flag:
            break
        else:
            for j in range(N):
                if miro[i][j] == 2 or miro[i][j] == 3:
                    visited[i][j] = 1
                    queue.append([i, j])
                    flag = 1
                    break

    while queue:
        if not flag:
            break
        x, y = queue.pop(0)
        for p in range(4):
            next_x = x + dx[p]
            next_y = y + dy[p]
            if is_wall(next_x, next_y):
                if miro[next_x][next_y] == 2 or miro[next_x][next_y] == 3:
                    flag = 0
                    result = visited[x][y] - 1
                    break
                else:
                    visited[next_x][next_y] = visited[x][y] + 1
                    queue.append([next_x, next_y])

    print('#{} {}'.format(t, result))