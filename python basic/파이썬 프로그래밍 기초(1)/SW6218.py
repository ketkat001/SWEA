#-*-coding: utf-8-*-

number = int(input())

for i in range(1,number+1):
    if number%i==0:
        print(f'{i}(은)는 {number}의 약수입니다.')


