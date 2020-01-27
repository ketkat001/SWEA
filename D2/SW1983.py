# -*- coding: utf-8 -*-

T = int(input())
for i in range (T):
    N, K = map(int, input().split())
    score_list = []
    student = 0
    sudent_rank = 0
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for num in range(N):
        score = list(map(int, input().split()))
        sum_score = 0
        sum_score = score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2
        score_list.append(sum_score)

    student = score_list[K-1]
    score_list.sort(reverse=True)
    student_rank = score_list.index(student)

    avg = int((student_rank / N) * 10)
    print(f'#{i+1} {grade[avg]}')