# -*- coding: utf-8 -*-

T = int(input())
for t in range(T):
    N = int(input())
    sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result_list = []
    result = 0
    while(True):
        for x in range(1, 10000):
            for i in str(N*x):
                if int(i) not in result_list:
                    result_list.append(int(i))
                    result_list.sort()
            
            if result_list == sample_list:
                break
        result = N * x
        break
            

    
    print(f'#{t+1} {result}')
            