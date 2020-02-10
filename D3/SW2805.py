def farm(ln, n):
    num = 1
    n_sum = 0
    for x in range(ln):
        if x <= (ln//2):




T = int(input())
for t in range(1, T+1):
    N = int(input())
    n_list = [input() for _ in range(N)]

    print(farm(N, n_list))