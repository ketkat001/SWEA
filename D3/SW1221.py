T = int(input())
for t in range(1, T+1):
    n, m = input().split()
    l_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    l_cnt = [0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0]
    data = input().split()
    for num in data:
        for i in range(10):
            if num == l_num[i]:
                l_cnt[i] += 1
    result = []
    for i in range(10):
        while l_cnt[i] != 0:
            result.append(l_num[i])
            l_cnt[i] -= 1
    result = ' '.join(result)
    print(n)
    print('{}'.format(result))