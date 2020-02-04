# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N = int(input())
    N_list = []
    N_list1 = []
    N_list2 = []
    N_list3 = []
    result = []

    for num in range(N):              # N * N 행렬 생성
        N_list.append(list(map(int, input().split())))

    for x in range(N):                # N_list1 90도 회전한 리스트
        store_list = []               # 임시 저장용 리스트 생성
        store_list = [N_list[y][x] for y in range(N-1, -1, -1)]
        N_list1.append(store_list)

    for x in range(N-1, -1, -1):      # N_list2 180도 회전한 리스트
        store_list = []
        store_list = [N_list[x][y] for y in range(N-1, -1, -1)]
        N_list2.append(store_list)

    for x in range(N-1, -1, -1):      # N_list3 270도 회전한 리스트
        store_list = []
        store_list = [N_list[y][x] for y in range(N)]
        N_list3.append(store_list)

    for j in range(N):
        store_list = []
        store_list.append(''.join(map(str, N_list1[j])))
        store_list.append(''.join(map(str, N_list2[j])))
        store_list.append(''.join(map(str, N_list3[j])))
        result.append(store_list)

    print(f'#{i+1}')
    for a in range(N):
        print(' '.join(map(str, result[a])))




