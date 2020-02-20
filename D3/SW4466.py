T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    score_list = list(map(int, input().split()))
    score_list.sort(reverse=True)
    score_sum = 0
    for i in range(K):
        score_sum += score_list[i]
    print('#{} {}'.format(t, score_sum)))