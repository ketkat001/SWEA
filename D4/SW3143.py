result = [0]
T = int(input())
for _ in range(T):
    A, B = input().split()
    num = len(A)
    num_2 = len(B)
    i, cnt = 0, 0
    while i < num:
        if A[i:i+num_2] == B:
            cnt += 1
            i += num_2
        else:
            i += 1
            cnt += 1
    result.append(cnt)
for t in range(1, T+1):
    print('#{} {}'.format(t, result[t]))