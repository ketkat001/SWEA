T = int(input())
for t in range(1, T+1):
    word = input()
    H = int(input())
    h_list = list(map(int, input().split()))
    result = ''
    for i in range(len(word)):
        if i == 0:
            for q in range(len(h_list)):
                if h_list[q] == 0:
                    result += '-'
        result += word[i]
        for j in range(len(h_list)):
            if i+1 == h_list[j]:
                result += '-'


    print('#{} {}'.format(t, result))