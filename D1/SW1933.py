# -*-coding: utf-8-*-

N = int(input())
result = []
if N>1000 or N<1:
    print(False)
for i in range(1,N+1):
    if N % i == 0:
        result.append(i)
result = sorted(result)
print(' '.join(map(str, result)))

