T = int(input())
for t in range(1, T+1):
    N = int(input())
    stu_list = []
    room_list = [0] * 401
    for _ in range(N):
        a = list(map(int, input().split()))
        a.sort()
        stu_list.append(a)
    for i in range(N):
        if stu_list[i][0] % 2:
            stu_list[i][0] += 1
        if stu_list[i][1] % 2:
            stu_list[i][1] += 1
        for j in range(stu_list[i][0], stu_list[i][1]+1, 2):
            room_list[j] += 1

    result = max(room_list)
    print('#{} {}'.format(t, result))