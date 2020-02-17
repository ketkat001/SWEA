T = int(input())
result = []
for t in range(1, T+1):
    A, B, C, D = map(int, input().split())
    if A/B > C/D:
        result.append('ALICE')
    elif A/B == C/D:
        result.append('DRAW')
    else:
        result.append('BOB')

for i in range(1, T+1):
    print('#{} {}'.format(i, result[i-1]))

