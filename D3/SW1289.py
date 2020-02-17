T = int(input())
for t in range(1, T+1):
    n = input()
    num = []
    for i in range(len(n)):
        num.append(n[i])
    num_2 = []
    cnt = 0
    for i in range(len(num)):
        num_2.append('0')

    while num != num_2:
        for i in range(len(num_2)):
            if num[i] == '1' and num[i] != num_2[i]:
                for x in range(i, len(num_2)):
                    num_2[x] = '1'
                cnt += 1
            elif num[i] == '0' and num[i] != num_2[i]:
                for x in range(i, len(num_2)):
                    num_2[x] = '0'
                cnt += 1

    print('#{} {}'.format(t, cnt))