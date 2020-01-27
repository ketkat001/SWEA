# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    N = int(input())
    store = 0
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []

    for mon in range(len(money)):
        if N % money[mon] != 0:
            store = int(N / money[mon])
            N = N - (store * money[mon])
            result.append(store)

        elif N % money[mon] == 0:
            store = int(N / money[mon])
            N = N - (store * money[mon])
            result.append(store)

        else:
            result.append(0)

    print(f'#{i+1}')
    print(' '.join(map(str, result)))