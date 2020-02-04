# -*- coding: utf-8 -*-

for i in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))
    max_idx, min_idx = 0, 0

    for dum in range(dump):
        max_h, min_h = box_list[max_idx], box_list[min_idx]

        for x in range(0, len(box_list)):
            if max_h == max(box_list) and min_h == min(box_list):  # max_h와 min_h가 리스트의 최대값과 최소값이라면 반복문 종료
                break

            if box_list[x] > max_h:                        # 최대값을 찾고 그 최대값의 인덱스를 max_idx에 저장
                max_h = box_list[x]
                max_idx = x

            if box_list[x] < min_h:                       # 최소값을 찾고 그 최소값의 인덱스를 min_idx에 저장
                min_h = box_list[x]
                min_idx = x

        box_list[max_idx] = box_list[max_idx] - 1           # 리스트의 max_idx와 min_idx에 저장된 값에서 수정
        box_list[min_idx] = box_list[min_idx] + 1


        if max(box_list) - min(box_list) <= 1:           # 만약에 수정 후의 리스트 최대값과 최소값의 차가 1 이하라면 종료
            break

    print(f'#{i} {max(box_list) - min(box_list)}')