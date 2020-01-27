#coding: utf-8

x = int(input())
list = []
while x > 0:
    list.append(int(x % 2))
    x = x // 2
list.reverse()
print(''.join([str(i) for i in list]))