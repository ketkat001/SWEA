def find_square(a, b):
    p, q = 0, 0
    while t_list[a + p][b]:
        p += 1
        if a + p > n - 1:
            break
    while t_list[a][b + q]:
        q += 1
        if b + q > n - 1:
            break
    for x in range(p):
        for y in range(q):
            t_list[a + x][b + y] = 0
    return p, q


def square_sort(count, m):
    result = [count]
    for _ in range(len(m)-1):
        for a in range(len(m) - 1):
            if m[a][0] * m[a][1] > m[a + 1][0] * m[a + 1][1]:
                m[a], m[a + 1] = m[a + 1], m[a]
            elif m[a][0] * m[a][1] == m[a + 1][0] * m[a + 1][1]:
                if m[a][0] > m[a + 1][0]:
                    m[a], m[a + 1] = m[a + 1], m[a]
    for a in range(len(m)):
        for b in range(2):
            result.append(m[a][b])
    return result


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    t_list = [list(map(int, input().split())) for _ in range(n)]
    result_list = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if t_list[i][j]:
                result_list.append(find_square(i, j))
                cnt += 1
    result_s = square_sort(cnt, result_list)

    ans = ' '.join(map(str, result_s))
    print('#{} {}'.format(t, ans))

