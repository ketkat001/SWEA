# -*-coding: utf-8 -*-

a_man, b_man = map(int, input().split())

if a_man == 1:
    if b_man == 2:
        print("B")
    else:
        print("A")
if a_man == 2:
    if b_man == 3:
        print("B")
    else:
        print("A")
if a_man == 3:
    if b_man == 1:
        print("B")
    else:
        print("A")
