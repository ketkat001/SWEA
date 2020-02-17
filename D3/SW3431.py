T = int(input())
for t in range(1, T+1):
    L, U, X = map(int, input().split())
    if X < L:
        result = L-X
    elif X > U:
        result = -1
    else:
        result = 0
    print('#{} {}'.format(t, result))