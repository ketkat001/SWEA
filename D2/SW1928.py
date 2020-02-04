# -*- coding: utf-8 -*-

def six_bitChar(arg):           # 64bit 문자 리스트 작성
    m = []
    x = 0
    for i in range(26):         # 배열에 인덱스 0 부터 25 까지 대문자 A부터Z 의 아스키코드를 삽입
        x = chr(ord('A') + i)
        m.append(x)
        x = 0
    for i in range(26):         # 배열에 인덱스 26부터 51 까지 소문자 a부터z 의 아스키코드를 삽입
        x = chr(ord('a') + i)
        m.append(x)
        x = 0

    for i in range(10):         # 배열에 인덱스 52부터 61 까지 0부터 9까지의 아스키코드 삽입
        x = chr(ord('0') + i)
        m.append(x)
        x = 0
    m.append(chr(ord('+')))
    m.append(chr(ord('/')))

    for num in range(len(m)):
        if m[num] == arg:       # arg에 대응하는 값을 반환한다.
            return num

def my_sixBin(x):               # 4개의 문자리스트를 받아 6자리의 2진수 코드로 변환후 반환

    result_bin = []
    for i in range(4):
        bin = []
        while x[i]!=0:
            bin.append(x[i] % 2)
            x[i] = x[i]//2
        bin.reverse()
        result = ''.join(map(str, bin))
        result = f'{result:0>6}'
        result_bin.append(result)

    return result_bin

def bin_num(x):               # 2진수를 10진수로 변환
    sum = 0
    bin_list = [128, 64, 32, 16, 8, 4, 2, 1]
    for i in range(0, 8):
        sum += int(x[i]) * bin_list[i]

    return sum


T = int(input())
for t in range(T):
    test_case = input()

    result_test = []
    result = ''
    a = 0
    b = ''

    for x in range(0, int(len(test_case) / 4)):
        buffer_list = []
        for j in range(x*4, x*4+4):
            a = six_bitChar(test_case[j])
            buffer_list.append(a)
        b = my_sixBin(buffer_list)
        result_test.append(b)


    for buffer in range(0, int(len(test_case) / 4)):
        Eightbit_buffer = ''
        Eightbit_buffer = ''.join(map(str, result_test[buffer]))
        for i in range(3):

            result += chr(bin_num(Eightbit_buffer[i * 8: i * 8 + 8]))

    print(f'#{t+1} {result}')
