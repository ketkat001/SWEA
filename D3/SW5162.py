T = int(input())
sum_list = []
for t in range(1,T+1):
    A, B, C = map(int, input().split())
    n_sum = 0
    if A > B:
        n_sum += C // B
        C = C % B
        n_sum += C // A
    else:
        n_sum += C // A
        C = C % A
        n_sum += C // B
    sum_list.append(n_sum)
for i in range(1, T+1):
    print('#{} {}'.format(i, sum_list[i-1]))
