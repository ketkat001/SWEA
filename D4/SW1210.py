def find_ladder(l):
    dx = [-1, 0, 0]
    dy = [0, 1, -1]
    lx = 99
    ly = 0
    flag = 0
    for y in range(100):
        if l[99][y] == 2:
            ly = y

    while lx > 0:
        lx += dx[flag]
        ly += dy[flag]
        if flag == 0:
            if ly == 0:
                if l[lx][ly+1] == 1:
                    flag = 1
            elif ly < 99:
                if l[lx][ly-1] == 1:
                    flag = 2
                elif l[lx][ly+1] == 1:
                    flag = 1
            else:
                if l[lx][ly-1] == 1:
                    flag = 2
        elif flag == 1:
            if l[lx+1][ly] == 1:
                flag = 0
        elif flag == 2:
            if l[lx+1][ly] == 1:
                flag = 0
    return ly


for t in range(10):
    T = int(input())
    ladder_list = [list(map(int, input().split())) for i in range(100)]
    print('#{} {}'.format(T, find_ladder(ladder_list)))