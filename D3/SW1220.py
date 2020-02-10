def magnetic(ln, n):
    cnt = 0
    for y in range(ln):
        check = 0
        for x in range(ln):
            if n[x][y] == 0:
                continue
            elif n[x][y] == 1:
                check = 1
            elif check == 0 and n[x][y] == 2:
                continue
            elif check == 1 and n[x][y] == 2:
                cnt += 1
                check = 0
    return cnt




for t in range(1, 11):
    N = int(input())
    n_list = []
    for _ in range(N):
        n_list.append(list(map(int, input().split())))

    print('#{} {}'.format(t, magnetic(N, n_list)))