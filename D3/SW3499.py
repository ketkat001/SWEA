T = int(input())
for t in range(1, T+1):
    N = int(input())
    card_list = list(input().split())
    result = []
    if len(card_list) % 2 == 0:
        for i in range(len(card_list)//2):
            result.append(card_list[i])
            result.append(card_list[len(card_list)//2+i])
    else:
        for i in range(len(card_list)//2):
            result.append(card_list[i])
            result.append(card_list[len(card_list)//2 + 1 + i])
        result.append(card_list[len(card_list)//2])
    result = ' '.join(result)
    print('#{} {}'.format(t, result))