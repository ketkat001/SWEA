result_list = []
T = int(input())
for i in range(T):
    x=int(input())**(1/3)
    if abs(round(x) - x) < 0.0001:
        result_list.append(round(x))
    else:
        result_list.append(-1)

for t in range(1, T+1):
    print('#{} {}'.format(t, result_list[t-1]))