result_list = []
T = int(input())
for _ in range(T):
    N, Q = map(int, input().split())
    N_list = [0]*(N+1)
    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L, R+1):
            N_list[i] = q
    result = N_list[1:]
    result_list.append(' '.join(map(str, result)))

for t in range(1, T+1):
    print('#{} {}'.format(t, result_list[t-1]))