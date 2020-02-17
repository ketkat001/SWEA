def square(n, a, b):
    min_square = 1000000000
    for r in range(1, n+1):
        for c in range(1, (n//r)+1):
            s = a * abs(r - c) + b * (n - r * c)
            if s < min_square:
                min_square = s
    return min_square


T = int(input())
for t in range(1, T+1):
    N, A, B = map(int, input().split())
    print('#{} {}'.format(t, square(N, A, B)))