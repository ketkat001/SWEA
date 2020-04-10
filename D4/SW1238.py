# 1238. [S/W 문제해결 기본] 10일차 - Contact

for t in range(1, 11):
    A, B = map(int, input().split())
    contact_list = list(map(int, input().split()))
    visited = [0] * 101
    queue = [B]
    visited[B] = 1
    graph_list = [[] for _ in range(101)]
    for i in range(A//2):
        graph_list[contact_list[i*2]].append(contact_list[(2*i)+1])
    while queue:
        x = queue.pop(0)
        for y in graph_list[x]:
            if visited[y] == 0:
                visited[y] = visited[x] + 1
                queue.append(y)
    max_value, idx = 0, 0
    for p in range(101):
        if visited[p] > max_value:
            max_value = visited[p]
            idx = p
        elif visited[p] == max_value:
            if p > idx:
                idx = p
    print('#{} {}'.format(t, idx))