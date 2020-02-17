def fish_cake(n, m, k, n_list):
    n_list.sort()
    tm = 0
    x = 0
    fi_ca = 0
    while x != n:
        if tm % m == 0 and tm > 0:
            fi_ca += k
        if tm == n_list[x]:
            fi_ca -= 1
            if fi_ca < 0:
                return "Impossible"
            x += 1
        elif tm > n_list[x]:
            if fi_ca == 0:
                return "Impossible"
            else:
                fi_ca -= 1
                x += 1
        tm += 1
    return "Possible"



T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    print('#{} {}'.format(t, fish_cake(N, M, K, N_list)))