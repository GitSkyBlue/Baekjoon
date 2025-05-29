import sys

n, m = map(int, sys.stdin.readline().split())

map_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited_map_list = [[1000001] * m for _ in range(n)]

start_x = -1
start_y = -1
for y in range(n):
    for x in range(m):
        if map_list[y][x] == 2:
            start_x = x
            start_y = y

target_list = [[start_y, start_x]]
visited_map_list[start_y][start_x] = 0
visited = [[False] * m for _ in range(n)]
visited[start_y][start_x] = True
move_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]

while target_list:
    temp = []
    for target in target_list:
        for move in move_list:
            current_x = target[1] + move[1]
            current_y = target[0] + move[0]
            
            if current_x > m - 1 or current_x < 0 or current_y > n - 1 or current_y < 0 or visited[current_y][current_x] or map_list[current_y][current_x] == 0: 
                continue
            else:
                visited[current_y][current_x] = True
                visited_map_list[current_y][current_x] = min(visited_map_list[current_y][current_x], visited_map_list[target[0]][target[1]] + 1)
                temp.append([current_y, current_x])
    target_list = temp

for y in range(n):
    for x in range(m):
        if visited_map_list[y][x] == 1000001:
            if map_list[y][x] == 0:
                visited_map_list[y][x] = 0
            else:
                visited_map_list[y][x] = -1
            
for m in visited_map_list:
    print(*m)
