T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    first_list = list(map(int, input().split()))
    for i in range(M - 1):
        next_list = list(map(int, input().split()))
        for j in range(len(first_list)):
            if first_list[j] > next_list[0]:
                first_list[j:j] = next_list
                break
        else:
            first_list = first_list + next_list
    result = ' '.join(map(str, first_list[-1:-11:-1]))
    print('#{} {}'.format(t, result))
