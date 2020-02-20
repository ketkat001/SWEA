mini = [1] * 1001
mini_list = []
for i in range(2, 1000):
    a = i
    if mini[i] == 0:
        pass
    else:
        while a < 1000 - i:
            mini[a+i] = 0
            a += i
        mini_list.append(i)

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    cnt = 0
    for x in range(len(mini_list)-2):
        if mini_list[x] > N:
            break
        for y in range(x, len(mini_list)-1):
            if mini_list[x] + mini_list[y] > N:
                break
            for z in range(y, len(mini_list)):
                if mini_list[x] + mini_list[y] + mini_list[z] > N:
                    break
                elif mini_list[x] + mini_list[y] + mini_list[z] == N:
                    cnt += 1
    result.append(cnt)

for i in range(T):
    print('#{} {}'.format(i+1, result[i]))