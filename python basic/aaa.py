def snail_list(N):
    result_list = []
    n = 1
    m = 0
    count, length = 1, N
    for i in range(N):                         # N * N 리스트 생성
        store_list = [0 for j in range(N)]
        result_list.append(store_list)

    while(length == 0):
        for x in range(length):
            result_list[m][x] = n
            n += 1
        count += 1
        m = length - 1

        for x in range(N-length, N):
            result_list[x][m] = n
            n += 1
        count += 1



        if count == 2:
            length = length - 1
            count = 0








    return result_list




