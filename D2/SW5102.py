# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    a_list = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph_list = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    visited[S] = 1
    queue = [S]
    result, flag = 0, 0
    for i in range(len(a_list)):
        graph_list[a_list[i][0]].append(a_list[i][1])
        graph_list[a_list[i][1]].append(a_list[i][0])
    while queue:
        if flag:
            break
        x = queue.pop(0)
        for y in graph_list[x]:
            if y == G:
                result = visited[x]
                flag = 1
                break
            elif visited[y] == 0:
                queue.append(y)
                visited[y] = visited[x] + 1
    print('#{} {}'.format(t, result))
