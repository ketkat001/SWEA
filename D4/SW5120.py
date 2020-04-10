# 5120. [파이썬 S/W 문제해결 기본] 7일차 - 암호

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int,input().split())
    test_list = list(map(int, input().split()))
    num = 0
    num_1 = test_list[0]
    for i in range(K):
        num += M
        if num > len(test_list):
            num = num-len(test_list)
        if num == len(test_list):
            test_list.append(test_list[0] + test_list[num-1])
        else:
            test_list[num:0] = [test_list[num-1] + test_list[num]]
    result = test_list[-1:-11:-1]
    result = ' '.join(map(str, result))
    print('#{} {}'.format(t, result))