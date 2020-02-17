def addEdge(u, v):
    graph_list[u].append(v)
    in_degree[v] += 1


def GraphSort():
    for x in range(1, V+1):
        if in_degree[x] == 0:
            stack.append(x)
    for y in range(V):
        cur = stack.pop()
        result.append(cur)
        for num in graph_list[cur]:
            in_degree[num] -= 1
            if in_degree[num] == 0:
                stack.append(num)
    return result


for t in range(1, 11):
    V, E = map(int, input().split())
    E_list = list(map(int, input().split()))
    graph_list = [[] for _ in range(V+1)]
    in_degree = [0 for _ in range(V+1)]
    stack = []
    result = []
    for a in range(len(E_list)//2):
        addEdge(E_list[(2*a)], E_list[(2*a)+1])
    ans = ' '.join(map(str, GraphSort()))
    print('#{} {}'.format(t, ans))