def subset_sum(n, k):
    a = len(n)
    count = 0
    for i in range(1<<a):
        sum = 0
        for j in range(a):
            if i & (1<<j):
                sum += n[j]
        if sum == k:
            count += 1
    return count


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    N_list = list(map(int, input().split()))

    print('#{} {}'.format(t, subset_sum(N_list, K)))