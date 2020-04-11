# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
def is_wall(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def solve(x, y, a):
    global min_value
    if x == N-1 and y == N-1:
        if min_value > a:
            min_value = a
    else:
        if a > min_value:
            return
        else:
            for i in range(2):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if is_wall(next_x, next_y):
                    solve(next_x, next_y, a + board[next_x][next_y])


dx = [1, 0]
dy = [0, 1]
for t in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_value = 1700
    solve(0, 0, board[0][0])
    print('#{} {}'.format(t, min_value))