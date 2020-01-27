# -*-coding: utf-8-*-

T = int(input())
for i in range(T):
    sample = list(input())
    result = 0
    for num in range(int(len(sample)/2)):
        if sample[num] == sample[len(sample)-num-1]:
            result = 1
        else:
            result = 0
    print(f'#{i+1} {result}')