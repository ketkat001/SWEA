def check(x, y, visited, tmp_map):
    if 0 <= x < H and 0 <= y < W and not visited[x][y] and tmp_map[x][y] != 0:
        return True
    return False


def cnt(brick_map):
    a = 0
    for i in range(H):
        for j in range(W):
            if brick_map[i][j] != 0:
                a += 1
    return a


def crash(x, y, brick_map):
    tmp_map = [brick_map[k][:] for k in range(H)]
    visited = [[0] * W for _ in range(H)]
    stack = [(x, y)]
    visited[x][y] = 1
    tmp_map[x][y] = 0
    while stack:
        x, y = stack.pop()
        if brick_map[x][y] > 1:
            for di in range(4):
                for l in range(1, brick_map[x][y]):
                    next_x, next_y = x + dx[di] * l, y + dy[di] * l
                    if check(next_x, next_y, visited, tmp_map):
                        visited[next_x][next_y] = 1
                        tmp_map[next_x][next_y] = 0
                        stack.append((next_x, next_y))
    down(tmp_map)
    return tmp_map


def down(tmp_map):
    for c in range(W):
        for r in range(H-1, 0, -1):
            if tmp_map[r][c] == 0:
                next_x = r - 1
                while next_x >= 0:
                    if tmp_map[next_x][c] != 0:
                        tmp_map[r][c], tmp_map[next_x][c] = tmp_map[next_x][c], 0
                        break
                    next_x -= 1
                else:
                    break


def next_location(n, brick_map):
    global min_brick
    if min_brick != 0:
        if n == 0:
            temp = cnt(brick_map)
            if min_brick > temp:
                min_brick = temp
        else:
            flag = 1
            for q in range(W):
                for p in range(H):
                    if brick_map[p][q] != 0:
                        next_location(n-1, crash(p, q, brick_map))
                        flag = 0
                        break
            if flag:
                min_brick = 0


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = [0]
T = int(input())
for _ in range(T):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]
    min_brick = 10000
    next_location(N, brick)
    result.append(min_brick)
for t in range(1, T+1):
    print('#{} {}'.format(t, result[t]))

