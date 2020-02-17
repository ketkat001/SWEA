T = int(input())
for t in range(1, T+1):
    N = int(input())
    P = [1, 1, 1]
    if N > 2:
        for n in range(3, N):
            P.append(P[n-2]+P[n-3])

    print('#{} {}'.format(t, P[N-1]))