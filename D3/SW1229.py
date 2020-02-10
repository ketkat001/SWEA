def password(l, s, n):
    idx = 0
    result = []
    for i in range(s):
        ord = int(n[2+idx])
        n_idx = int(n[idx + 1])
        a = 1
        if n[0+idx] == 'I':
            num = idx + 3 + ord
            if n_idx > 10:
                idx = num
                continue
            while ord+1 != a:
                l.insert(int(n[idx+1]), n[num-a])
                a += 1
            idx = num
        else:
            num = idx + 3
            if n_idx > 10:
                idx = num
                continue
            while ord != 0:
                l.pop(int(n[idx+1]))
                ord -= 1
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