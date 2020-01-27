# -*- coding: utf-8 -*-

a, b = map(int, input().split())

if a and b not in range(1,10):
    print(False)

print(a + b)
print(a - b)
print(a * b)
print(int(a / b))



