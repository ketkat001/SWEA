T = int(input())
for t in range(1, T+1):
    num = list(map(int, input().split()))
    sum_x, sum_y = 0, 0
    for i in range(2):
        nx, ny = 1, 1
        max_x = 1
        if num[i] == 1:
            pass
        else:
            while num[i] > max_x:
                nx += 1
                max_x += nx
        if max_x == num[i]:
            pass
        else:
            cha = max_x - num[i]
            nx = nx - cha
            ny = ny + cha
        sum_x += nx
        sum_y += ny
    result = 0
    for x in range(1, sum_x+1):
        result += x
    for y in range(0, sum_y-1):
        result += sum_x + y
    print('#{} {}'.format(t, result))
