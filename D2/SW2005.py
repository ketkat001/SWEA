# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N = int(input())
    print(f'#{i + 1}')                # #1, #2, #3 출력
    for num in range(N):              # 리스트 1, 2, 3 --- , N 개 생성
        r = 1
        result_list = [1]

        for j in range(num):          # 리스트 1, 2, 3 --- , N 의 인덱스 생성
            r = (r * (num - j)) / (j + 1)
            result_list.append(int(r))

        print(' '.join(map(str, result_list)))