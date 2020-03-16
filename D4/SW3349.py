T = int(input())
for t in range(1, T+1):
    W, H, N = map(int, input().split())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-1):
        x = N_list[i+1][0] - N_list[i][0]
        y = N_list[i+1][1] - N_list[i][1]
        a, b = abs(x), abs(y)
        if x*y > 0:
            if a > b:
                ans += a
            else:
                ans += b
        else:
            ans += a + b
    print('#{} {}'.format(t, ans))
