result = [0]
T = int(input())
for _ in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    max_score = sum(N_list)
    cnt = 1
    temp = 0
    score_list = [0] * (max_score+1)
    for i in range(N):
        temp += N_list[i]
        for j in range(temp-1, -1, -1):
            if score_list[j]:
                score_list[j + N_list[i]] = 1
        score_list[N_list[i]] = 1
    for k in range(max_score+1):
        if score_list[k]:
            cnt += 1
    result.append(cnt)
for t in range(1, T+1):
    print('#{} {}'.format(t, result[t]))