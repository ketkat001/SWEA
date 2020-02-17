T = int(input())
for t in range(1, T+1):
    t_list = list(map(int, input().split()))
    if t_list[0] != t_list[1] and t_list[0] != t_list[2]:
        result = t_list[0]
    elif t_list[0] != t_list[1] and t_list[0] == t_list[2]:
        result = t_list[1]
    elif t_list[0] == t_list[1] and t_list[0] != t_list[2]:
        result = t_list[2]
    else:
        result = t_list[0]

    print('#{} {}'.format(t, result))

