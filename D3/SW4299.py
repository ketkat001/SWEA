T = int(input())
for t in range(1, T+1):
    D, H, M = map(int, input().split())
    day = (D - 11) * 60 * 24
    hour = (H - 11) * 60
    minute = M - 11
    result = day + hour + minute
    if result < 0:
        result = -1
    print('#{} {}'.format(t, result))


