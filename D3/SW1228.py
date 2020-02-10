def password(l, s, n):
    idx = 0
    result = []
    for i in range(s):
        ord = int(n[2+idx])
        num = idx + 3 + ord
        a = 1
        while ord+1 != a:
            l.insert(int(n[idx+1]), n[num-a])
            a += 1
        idx = num
    for x in range(10):
        result.append(l[x])
    return result

for t in range(1, 11):
    N = int(input())
    N_list = list(input().split())
    S = int(input())
    S_list = list(input().split())
    ans = ' '.join(password(N_list, S, S_list))
    print('#{} {}'.format(t, ans))