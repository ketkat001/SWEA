def palindrome(word):
    for i in range(len(word)//2):
        if word[i] == word[len(word)-1-i]:
            pass
        elif word[i] == '*' or word[len(word)-1-i] == '*':
            return 'Exist'
        else:
            return 'Not exist'
    return 'Exist'


T = int(input())
for t in range(1, T+1):
    words = input()
    print('#{} {}'.format(t, palindrome(words)))