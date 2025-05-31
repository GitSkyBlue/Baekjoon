import sys

n = int(sys.stdin.readline())
map_list = []
move_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False] * n for _ in range(n)]
answer = []
count = 0
for _ in range(n):
    map_list.append(list(sys.stdin.readline().strip()))

for y in range(n):
    for x in range(n):
        if visited[y][x]:
            continue
        else:
            count += 1
            target_alpha = map_list[y][x]
            target_list = [[y, x]]
            visited[y][x] = True
            while target_list:
                temp = []
                for target in target_list:
                    for move in move_list:
                        current_x = target[1] + move[1]
                        current_y = target[0] + move[0]
                        if current_x < 0 or current_x > n - 1 or current_y < 0 or current_y > n - 1 or visited[current_y][current_x] or map_list[current_y][current_x] != target_alpha:
                            continue
                        else:
                            temp.append([current_y, current_x])
                            visited[current_y][current_x] = True

                target_list = temp
answer.append(count)
for i in range(n):
    for j in range(n):
        if map_list[i][j] == 'G':
            map_list[i][j] = 'R'

count = 0
visited = [[False] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if visited[y][x]:
            continue
        else:
            count += 1
            target_alpha = map_list[y][x]
            target_list = [[y, x]]
            visited[y][x] = True
            while target_list:
                temp = []
                for target in target_list:
                    for move in move_list:
                        current_x = target[1] + move[1]
                        current_y = target[0] + move[0]
                        if current_x < 0 or current_x > n - 1 or current_y < 0 or current_y > n - 1 or visited[current_y][current_x] or map_list[current_y][current_x] != target_alpha:
                            continue
                        else:
                            temp.append([current_y, current_x])
                            visited[current_y][current_x] = True

                target_list = temp
answer.append(count)
print(*answer)