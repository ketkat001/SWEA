T = int(input())
result_list = []
for _ in range(T):
    D, A, B, F = map(int, input().split())
    fli_t = D / (A+B)
    result = fli_t * F
    result_list.append(result)

for t in range(T):
    print('{} {:.6f}'.format(t+1, result_list[t]))