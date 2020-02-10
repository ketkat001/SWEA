num_list = []
result_list = []

for i in range(1, 1000001):
    num_list.append(1)

for x in range(2, 1000000):
    y = x
    if num_list[x] == 0:
        pass
    else:
        while y < 1000000 - x:
            num_list[x+y] = 0
            y += x
        result_list.append(x)

print(' '.join(map(str, result_list)))


