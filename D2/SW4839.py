# -*- coding: utf-8 -*-

def my_binarysort(page, a_page, b_page):
    list_page = [a_page, b_page]
    count = [0, 0]
    for i in range(2):
        start = 1
        end = page
        middle = int((start + end)/2)

        while(True):
            if middle > list_page[i]:
                end = middle
                middle = int((start + end)/2)
                count[i] += 1
            elif middle < list_page[i]:
                start = middle
                middle = int((start + end) / 2)
                count[i] += 1
            else:
                break
    if count[0] < count[1]:
        return 'A'
    elif count[0] > count[1]:
        return 'B'
    else:
        return 0

T = int(input())
for t in range(1, T+1):
    P, A, B = map(int, input().split())

    print('#{} {}'.format(t, my_binarysort(P, A, B)))

