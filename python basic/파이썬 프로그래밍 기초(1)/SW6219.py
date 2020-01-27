#-*-coding: utf-8-*-

number = int(input())
number_list = []
if number > 0:
    for i in range(1, number+1):
        if number % i == 0:
            number_list.append(i)
            print(f'{i}(은)는 {number}의 약수입니다.')
if len(number_list) == 2:
    print(f'{number}(은)는 {number_list[0]}과 {number_list[1]}로만 나눌 수 있는 소수입니다.')