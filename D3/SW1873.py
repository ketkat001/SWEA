def is_wall(a, b):
    if a > H-1 or a < 0 or b > W-1 or b < 0 or map_list[a][b] == '#':
        return False
    return True


def direction(d):
    d_dir = 0
    dir_list = ['U', 'D', 'L', 'R']
    for i in range(4):
        if d == dir_list[i]:
            d_dir = i
    return d_dir


def tank_war(x, y):
    global dir
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(len(order_list)):
        if order_list[i] == 'S':
            next_x, next_y = x + dx[dir], y + dy[dir]
            if is_wall(next_x, next_y):
                while True:
                    if is_wall(next_x, next_y):
                        if map_list[next_x][next_y] == '#':
                            break
                        elif map_list[next_x][next_y] == '*':
                            map_list[next_x][next_y] = '.'
                            break
                        else:
                            next_x += dx[dir]
                            next_y += dy[dir]
                    else:
                        break
        else:
            dir = direction(order_list[i])
            tank_dir = ['^', 'v', '<', '>']
            map_list[x][y] = tank_dir[dir]
            next_x, next_y = x+dx[dir], y+dy[dir]
            if is_wall(next_x, next_y):
                if map_list[next_x][next_y] == '.':
                    map_list[x][y], map_list[next_x][next_y] = map_list[next_x][next_y], map_list[x][y]
                    x, y = next_x, next_y
    return map_list


T = int(input())
for t in range(1, T+1):
    H, W = map(int, input().split())
    map_list = [list(input()) for _ in range(H)]
    N = int(input())
    order_list = list(input())
    entry_x, entry_y = 0, 0
    for p in range(H):
        for q in range(W):
            if map_list[p][q] == '>' or map_list[p][q] == '<' or map_list[p][q] == '^' or map_list[p][q] == 'v':
                entry_x, entry_y = p, q
                if map_list[p][q] == '^':
                    dir = 0
                elif map_list[p][q] == 'v':
                    dir = 1
                elif map_list[p][q] == '<':
                    dir = 2
                elif map_list[p][q] == '>':
                    dir = 3
    result = tank_war(entry_x, entry_y)
    print("#{}".format(t), end=' ')
    for i in range(H):
        print(''.join(result[i]))