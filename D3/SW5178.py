# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합
class Tree:
    def __init__(self, n):
        self.result_sum = 0
        self.lst = [0] * (n + 1)
        self.n = n

    def put(self, num_1, num_2):
        self.lst[num_1] = num_2

    def search_leaf(self, node):
        if node * 2 > N:
            self.sum += self.lst[node]
        else:
            self.search_leaf(node * 2)
            if node * 2 != N:
                self.search_leaf(node * 2 + 1)

    def result(self, p):
        self.sum = 0
        self.search_leaf(p)
        return self.sum


T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = Tree(N)
    for _ in range(M):
        num1, num2 = map(int, input().split())
        tree.put(num1, num2)
    print('#{} {}'.format(t, tree.result(L)))
