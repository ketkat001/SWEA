T = int(input())
result = [0]
for _ in range(T):
    p = input()
    cnt = 0
    stick = []
    i = 0
    while i < len(p):
        if p[i] == '(' and p[i + 1] == ')' and stick != []:
            cnt += len(stick)
            i += 1
        elif p[i] == '(' and p[i + 1] != ')':
            stick.append(p[i])
            cnt += 1
        elif p[i] == ')' and stick != []:
            stick.pop()
        i += 1
    result.append(cnt)
for t in range(1, T+1):
    print('#{} {}'.format(t, result[t]))