result_list = []
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    k_list = list(map(int, input().split()))
    stu_list = [0] * (N+1)
    result = []
    for num in k_list:
        stu_list[num] = 1
    for i in range(1, N+1):
        if stu_list[i] == 0:
            result.append(i)

    result_list.append(' '.join(map(str, result)))
for i in range(T):
    print('#{} {}'.format(i+1, result_list[i]))