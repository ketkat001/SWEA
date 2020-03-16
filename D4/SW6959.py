result = [0]
T = int(input())
for _ in range(T):
    num = list(input().rstrip())
    cnt = 0
    ans = ''
    while len(num) != 1:
        a = int(num.pop())
        b = int(num.pop())
        c = a+b
        if c < 10:
            num.append(str(c))
        else:
            c = str(c)
            num.append(c[0])
            num.append(c[1])
        cnt += 1
    if cnt % 2:
        ans = 'A'
    else:
        ans = 'B'
    result.append(ans)
for t in range(1, T+1):
    print('#{} {}'.format(t, result[t]))
