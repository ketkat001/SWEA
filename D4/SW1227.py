def iswall(x, y):
    if miro_list[x][y] != 1 and not visit_list[x][y]:
        return True
    return False


def DFS(r, c):
    stack_list = []
    stack_list.append((r,c))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit_list[r][c] = 1
    while stack_list:
        rc = stack_list.pop()
        r = rc[0]
        c = rc[1]
        for p in range(4):
            next_x = r + dx[p]
            next_y = c + dy[p]
            if next_x == exit_x and next_y == exit_y:
                return 1
            elif iswall(next_x, next_y):
                stack_list.append((next_x, next_y))
                visit_list[next_x][next_y] = 1
    return 0


for t in range(10):
    T = int(input())
    miro_list = [list(map(int, input())) for _ in range(100)]
    visit_list = [[0]*100 for _ in range(100)]
    entry_x, entry_y = 0, 0
    exit_x, exit_y = 0, 0
    for i in range(100):
        for j in range(100):
            if miro_list[i][j] == 2:
                entry_x, entry_y = i, j
            if miro_list[i][j] == 3:
                exit_x, exit_y = i, j
    print('#{} {}'.format(T, DFS(entry_x, entry_y)))
