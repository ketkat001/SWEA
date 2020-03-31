def solve():
    flag = 0
    for r in range(1, 21):
        for y in range(1, 21):
            for z in range(1, 21):
                for x in range(1, len(list1)-1):
                    if r*list1[x][0] + y*list1[x][1] + z*list1[x][2] == list2[x]:
                        flag = 1
                    else:
                        flag = 0
                        break
                if flag == 1:
                    R.append(r)
                    C.append(y)
                    S.append(z)


T = int(input())
for t in range(1, T+1):
    P, Q = map(int, input().split())
    style_list = [list(input()) for _ in range(P)]
    my_list = [list(input()) for _ in range(Q)]
    a = b = c = d = e = f = 0
    list1 = [[0, 0, 0]]
    list2 = []
    R, C, S = [], [], []
    for i in range(P):
        dot = 0
        m = 0
        while style_list[i][m] == '.':
            dot += 1
            m += 1
        for j in range(len(style_list[i])):
            if style_list[i][j] == '(':
                a += 1
            elif style_list[i][j] == ')':
                b += 1
            elif style_list[i][j] == '{':
                c += 1
            elif style_list[i][j] == '}':
                d += 1
            elif style_list[i][j] == '[':
                e += 1
            elif style_list[i][j] == ']':
                f += 1
        list1.append([a-b, c-d, e-f])
        list2.append(dot)
    case = 0
    for n in range(1, len(list1)):
        case += sum(list1[n])
    solve()
    a = b = c = d = e = f = 0
    list3 = [[0, 0, 0]]
    for i in range(Q):
        for j in range(len(my_list[i])):
            if my_list[i][j] == '(':
                a += 1
            elif my_list[i][j] == ')':
                b += 1
            elif my_list[i][j] == '{':
                c += 1
            elif my_list[i][j] == '}':
                d += 1
            elif my_list[i][j] == '[':
                e += 1
            elif my_list[i][j] == ']':
                f += 1
        list3.append([a-b, c-d, e-f])
    result = [0]
    for p in range(1, len(list3)-1):
        ans = []
        for q in range(len(R)):
            ans.append(R[q]*list3[p][0] + C[q]*list3[p][1] + S[q]*list3[p][2])
        if case == 0 and sum(list3[p]) != 0:
            result.append(-1)
        elif len(R) == len(C) == len(S) == 0:
            result.append(0)
        elif sum(ans)//len(R) != R[0]*list3[p][0] + C[0]*list3[p][1] + S[0]*list3[p][2]:
            result.append(-1)
        else:
            result.append(R[0]*list3[p][0] + C[0]*list3[p][1] + S[0]*list3[p][2])
    result = ' '.join(map(str, result))
    print('#{} {}'.format(t, result))