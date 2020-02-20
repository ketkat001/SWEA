def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nex in combinations(arr[i+1:], r-1):
                yield [arr[i]] + nex


T = int(input())
result_list = []
for _ in range(T):
    n_list = list(map(int, input().split()))
    result = []
    for comb in combinations(n_list, 3):
        if sum(comb) not in result:
            result.append(sum(comb))
    result.sort()
    result_list.append(result[-5])
for t in range(1, T+1):
    print('#{} {}'.format(t, result_list[t-1]))