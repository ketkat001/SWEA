T = int(input())
for t in range(1, T+1):
    N = int(input())
    S1 = (N*(N+1)) // 2
    S2 = N*N
    S3 = S1 * 2
    print('#{} {} {} {}'.format(t, S1, S2, S3))
