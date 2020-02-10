def mPassWord(n):
    cha = 1
    while n[7] != 0:
        if cha == 6:
            cha = 1
        else:
            n[0] -= cha
            if n[0] < 0:
                n[0] = 0
            swap = n.pop(0)
            n.append(swap)
            cha += 1
    return n

for t in range(10):
    T = int(input())
    N_list = list(map(int, input().split()))
    result = ' '.join(map(str, mPassWord(N_list)))
    print('#{} {}'.format(T, result))