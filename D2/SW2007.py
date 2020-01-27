# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    sample = input()
    pattern_size = 1
    if len(sample) > 30:                           # 문자열의 길이가 30 이상일 경우 False 출력
        print(False)
    else:
        for j in range(int(len(sample)/2)):
            if sample[j] == sample[j+pattern_size]:        # 패턴이 반복되지 않을 경우 패턴길이 +1
                pass
            else:
                pattern_size += 1
        if pattern_size > 10:                       # 패턴길이가 10이 넘어갈 경우 False 출력
            print(False)
        else:
            print(f'#{i+1} {pattern_size}')
