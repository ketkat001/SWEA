# -*- coding: utf-8 -*-

for i in range(10):
    T = int(input())
    search = input()
    T_text = input()

    cnt = 0
    for x in range(len(T_text)):
        if search[0] == T_text[x]:
            if search == T_text[x:x+len(search)]:
                cnt += 1

    print(f'#{T} {cnt}')
