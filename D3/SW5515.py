import time
from datetime import date

result_list = []
T = int(input())
for _ in range(T):
    m, d = map(int, input().split())
    result = int(date(2016, m, d).strftime("%w"))
    if result == 0:
        result = 6
        result_list.append(result)
    else:
        result_list.append(result-1)

for i in range(T):
    print('#{} {}'.format(i+1, result_list[i]))