T = int(input())
for t in range(1, T+1):
    N_list = list(map(int, input()))
    all_a = 0
    ans = 0
    for i in range(len(N_list)):
        if N_list[i] == 0:
            pass
        elif all_a >= i:
            all_a += N_list[i]
        else:
            a = i - all_a
            ans += a
            all_a += a
            all_a += N_list[i]
    print('#{} {}'.format(t, ans))