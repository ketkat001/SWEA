T = int(input())
for t in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    n_max, n_sum = -1000, 0
    for i in range(N):
        n_sum += N_list[i]
        if n_max < n_sum:
            n_max = n_sum
        if n_sum < 0:
            n_sum = 0
    print('#{} {}'.format(t+1, n_max))