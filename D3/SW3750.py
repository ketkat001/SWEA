def digit(n):
    n_sum = 0
    for i in range(len(n)):
        n_sum += int(n[i])
    if n_sum >= 10:
        return digit(str(n_sum))
    else:
        return n_sum


T = int(input())
result = []
for t in range(1, T+1):
    N = input()
    result.append(digit(N))

for t in range(1, T+1):
    print('#{} {}'.format(t, result[t-1]))