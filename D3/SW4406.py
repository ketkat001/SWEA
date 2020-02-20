m = ['a', 'e', 'i', 'o', 'u']
T = int(input())
for t in range(1, T+1):
    words = input()
    result = ''
    for word in words:
        if word in m:
            pass
        else:
            result += word
    print('#{} {}'.format(t, result))
