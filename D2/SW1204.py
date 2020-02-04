# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N = int(input())
    Stu_list = map(int, input().split())

    score_dic = {}
    max_val = 0

    for score in Stu_list:
        if score not in score_dic:
            score_dic[score] = 1
        else:
            score_dic[score] += 1
    
    for key, val in score_dic.items():
        if val > max_val:
            max_val = val
            max_score = []
            max_score.append(key)
        elif val == max_val:
            max_score.append(key)
    max_score.sort()
    
    print(f'#{N} {max_score[-1]}')
        
