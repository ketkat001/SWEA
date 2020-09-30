from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    delivery_map = [list(map(int, input().split())) for _ in range(N)]
    restaurant = []
    house = []
    for i in range(N):
        for j in range(N):
            if delivery_map[i][j] > 1:
                restaurant.append([i, j, delivery_map[i][j]])
            if delivery_map[i][j] == 1:
                house.append([i, j, 1])

    min_value = 99999999
    for n in range(1, len(restaurant)+1):
        for comb in combinations(restaurant, n):
            restaurants = []
            result = 0
            for com in comb:
                restaurants.append(com)
                result += com[2]
            for hou in house:
                temp = 0
                min_temp = 999999
                for res in restaurants:
                    temp = abs(hou[0] - res[0]) + abs(hou[1] - res[1])
                    if temp < min_temp:
                        min_temp = temp
                result += min_temp
            if result < min_value:
                min_value = result
    print("#{} {}".format(t, min_value))
