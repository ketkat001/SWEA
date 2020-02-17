def N_queen(n):



T = int(input())
for t in range(1, T+1):
    N = int(input())
    chess_list = [[0]*N for _ in range(N)]
    print(N_Queen(N))