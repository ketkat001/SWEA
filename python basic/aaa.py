a = b = c = d = e = f = 0
list3 = [[0, 0, 0]]
for i in range(Q):
    for j in range(len(my_list[i])):
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
    list3.append([a-b, c-d, e-f])