T = int(input())
result_list = []
for _ in range(T):
    N = input()
    if int(N[-1]) % 2 == 0:
        result = 'Even'
    else:
        result = 'Odd'
    result_list.append(result)

for i in range(T):
    print('#{} {}'.format(i+1, result_list[i]))