# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    n_list = []
    result = 0

    for n in range(N):
        n_list.append(list(map(int, input().split())))  # N * N 의 퍼즐 입력

    for x in range(N):
        length = 0  # 문자 들어갈 공간 크기 변수 선언
        for y in range(N):  # 가로 공간 측정

            if n_list[x][y] == 0:
                    if length == K:
                        result += 1
                        length = 0
                    else:
                        length = 0
            else:
                length += 1

            if y == N-1:
                if length == K:
                    result += 1

    for x in range(N):
        length = 0
        for h in range(N):  # 세로 공간 측정
            if n_list[h][x] == 0:
                if length == K:
                    result += 1
                    length = 0
                else:
                    length = 0
            else:
                length += 1

            if h == N-1:
                if length == K:
                    result += 1


    print(f'#{i + 1} {result}')