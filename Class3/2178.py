import sys

n, m = map(int, sys.stdin.readline().split())

maze_list = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
move_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
target_list = [[0, 0]]
visited[0][0] = True
count = 1
while target_list:
    temp = []
    count += 1
    for target in target_list:
        for move in move_list:
            current_x = target[1] + move[1]
            current_y = target[0] + move[0]
            if current_x < 0 or current_x > m - 1 or current_y < 0 or current_y > n - 1 or visited[current_y][current_x]:
                continue
            else:
                if maze_list[current_y][current_x] != '0':
                    temp.append([current_y, current_x])
                    visited[current_y][current_x] = True

    if [n - 1, m - 1] in temp:
        break
    target_list = temp

print(count)