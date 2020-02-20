result_list = []
T = int(input())
for _ in range(T):
    N = int(input())
    n_sum = 0
    for _ in range(N):
        p, x = map(float, input().split())
        n_sum += p * x
    result_list.append(n_sum)

for i in range(T):
    print('#{} {:.6f}'.format(i+1, result_list[i]))