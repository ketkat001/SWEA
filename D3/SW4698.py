result_list = [1]*1000001
for x in range(2, 1000001):
    y = x
    if result_list[x] == 0:
        pass
    else:
        while y < 1000001-x:
            result_list[x+y] = 0
            y += x

T = int(input())
ans = []
for t in range(1, T+1):
    D, A, B = map(int, input().split())
    ans_list = []
    for i in range(A, B+1):
        if result_list[i] == 1 and str(D) in str(i) and i != 1:
            ans_list.append(i)
    ans.append(len(ans_list))

for t in range(1, T+1):
    print('#{} {}'.format(t, ans[t-1]))