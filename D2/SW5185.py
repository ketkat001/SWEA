# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

for t in range(1, int(input()) + 1):
    N, hex_num = input().split()
    result = ''
    for num in hex_num:
        if '0' <= num <= '9':
            temp = ord(num) - ord('0')
        else:
            temp = ord(num) - ord('A') + 10
        for i in range(3, -1, -1):
            if temp & (1 << i):
                result += '1'
            else:
                result += '0'
    print('#{} {}'.format(t, result))