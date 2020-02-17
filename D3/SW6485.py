T = int(input())
for t in range(1, T+1):
    N = int(input())
    N_list = []
    for _ in range(N):
        N_list.append(list(map(int, input().split())))
    P = int(input())
    result_list = []
    for _ in range(P):
        num = int(input())
        cnt = 0
        for i in range(N):
            for x in range(N_list[i][0], N_list[i][1]+1):
                if num == x:
                    cnt += 1
        result_list.append(cnt)
    result = ' '.join(map(str, result_list))
    print('#{} {}'.format(t, result))