# -*- coding: utf-8 -*-

T = int(input())

for i in range(T):
    sudoku = []
    result = 1
    for num in range(0, 9):
        sudoku.append(list(map(int, input().split())))  # 스도쿠 생성

    for x in range(0, 9):
        sum = 0
        for y in range(0, 9):  # 가로 스도쿠 확인
            sum += sudoku[x][y]
        if sum != 45:
            result = 0

    for x in range(0, 9):
        sum = 0
        for y in range(0, 9):  # 세로 스도쿠 확인
            sum += sudoku[y][x]
        if sum != 45:
            result = 0

    for x in range(0, 3):  # 3 * 3 스도쿠 확인
        for y in range(0, 3):
            sum = 0
            for h in range(0, 3):
                for j in range(0, 3):
                    sum += sudoku[x * 3 + h][y * 3 + j]
            if sum != 45:
                result = 0

    print(f'#{i + 1} {result}')




