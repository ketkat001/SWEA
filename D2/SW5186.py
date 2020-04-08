# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

for t in range(1, int(input()) + 1):
    N = float(input())
    result = ''

    for i in range(1, 13):
        num = 1.0 / (1 << i)
        if N == 0:
            break
        if N - num >= 0:
            result += '1'
            N = N - num
        else:
            result += '0'
    if N != 0:
        result = 'overflow'

    print("#{} {}".format(t, result))