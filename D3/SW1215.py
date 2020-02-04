# -*- coding: utf-8 -*-

def my_palindrome(list, n):
    count = 0

    for x in range(8):
        for y in range(8-n+1):
            y_count = 0
            x_count = 0
            for h in range(n//2):
                if list[x][y+h] == list[x][n-h+y-1]:
                    y_count += 1
                if list[y+h][x] == list[n-h+y-1][x]:
                    x_count += 1
            if y_count == n//2:
                count += 1
            if x_count == n//2:
                count += 1
    return count

for i in range(10):
    N = int(input())
    T_list = []
    for t in range(8):
        m = input()
        A_list = []
        for word in m:
            A_list.append(word)
        T_list.append(A_list)
    result = my_palindrome(T_list, N)
    print(f'#{i+1} {result}')
