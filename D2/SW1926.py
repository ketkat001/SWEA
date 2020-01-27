# -*- coding: utf-8 -*-

N = int(input())

num_list = []
r = 0                          # 1, 10 ,100, 1000의 자리를 저장하는 값
save_num = 0                   # 나누는 대상
q = 0                          # 10을 나눈 몫을 저장


for i in range(1, N+1):
    flag = 0                   # 3,6,9가 없는 경우 0, 하나라도 있으면 1
    save_num = i
    x = 0                      # 3,6,9의 갯수 저장
    while(save_num != 0):
        r = save_num % 10
        if r % 3 == 0 and r != 0:            # r != 0을 넣어 10, 20, 40 등 10으로 나눴을 경우 나머지가 없는 경우 방지
            flag = 1
            x += 1
        else:
            pass
        q = int(save_num / 10)
        save_num = q
        
    if flag == 0:                       # flag가 0 일 경우 숫자를 리스트에 삽입
        num_list.append(i)
    elif flag == 1:                     # flag가 1 일 경우 x 갯수 만큼 '-'를 곱하여 리스트에 삽입
        num_list.append('-' * x)
        
print(' '.join(map(str, num_list)))