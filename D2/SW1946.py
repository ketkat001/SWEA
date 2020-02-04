# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N = int(input())
    word_list = []
    word_length = 0

    for x in range(N):
        word, num = input().split()
        word_list.append(word * int(num))

    result = ''.join(word_list)
    word_length = len(result)

    if word_length % 10 != 0:
        count = word_length // 10 + 1
    else:
        count = word_length // 10

    print(f'#{i+1}')

    for y in range(0, count):
        for z in range(y*10, y*10 + 10):
            if z > word_length-1:
                break
            print(result[z], end = '')
        print()
