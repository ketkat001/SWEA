# -*- coding: utf-8 -*-

def my_palindrome(L):
    length = 2
    count = 0
    while(length <= 100):
        for x in range(100):
            for y in range(100-length+1):
                y_count = 0
                x_count = 0
                for h in range(length//2):
                    if L[x][y+h] == L[x][length-h+y-1]:
                        y_count += 1
                    if L[y+h][x] == L[length-h+y-1][x]:
                        x_count += 1
                if y_count == length//2 or x_count == length//2:
                    count = length
                    break
        length += 1


    return count


for t in range(1, 11):
    p_list = []
    n = int(input())
    for x in range(100):
        l_list = []
        a = input()
        for i in a:
            l_list.append(i)
        p_list.append(l_list)

    print(f'#{n} {my_palindrome(p_list)}')


