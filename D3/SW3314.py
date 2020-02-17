T = int(input())
for t in range(1, T+1):
    score_list = list(map(int, input().split()))
    score_sum = 0
    for i in range(5):
        if score_list[i] >= 40:
            score_sum += score_list[i]
        else:
            score_sum += 40
    avg = score_sum // 5

    print('#{} {}'.format(t, avg))