#-*- coding: utf-8 -*-

data = input()
data_list = []
final_list = []
result = ''
for i in data:
    data_list.append(i)  # 문자열 하나씩 나눠서 리스트로 변환
for j in range(len(data)-1, -1, -1):
    final_list.append(data_list[j])
for x in final_list:
    result = result + x
print(result)
print('입력하신 단어는 회문(Palindrome)입니다.')



