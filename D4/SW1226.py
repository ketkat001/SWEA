def iswall(x, y):
    if miro_list[x][y] != 1 and not visit_list[x][y]:
        return True
    return False


def DFS(r, c):
    visit_list[r][c] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    if r == exit_x and c == exit_y:
        return 1
    for p in range(4):
        next_x = r + dx[p]
        next_y = c + dy[p]
        if iswall(next_x, next_y):
            if DFS(next_x, next_y) == 1:
                return 1
    return 0


for t in range(10):
    T = int(input())
    miro_list = [list(map(int, input())) for _ in range(16)]
    visit_list = [[0]*16 for _ in range(16)]
    entry_x, entry_y = 0, 0
    exit_x, exit_y = 0, 0
    for i in range(16):
        for j in range(16):
            if miro_list[i][j] == 2:
                entry_x, entry_y = i, j
            if miro_list[i][j] == 3:
                exit_x, exit_y = i, j
    print('#{} {}'.format(T, DFS(entry_x, entry_y)))
