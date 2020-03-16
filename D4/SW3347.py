T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    count_list = [0] * N
    for pay in B_list:
        for i in range(N):
            if pay >= A_list[i]:
                count_list[i] += 1
                break
    result = count_list.index(max(count_list))+1
    print('#{} {}'.format(t, result))

