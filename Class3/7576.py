import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

tomato_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
move_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dq = deque()
visited = [[False] * n for _ in range(m)]
next = []
for y in range(m):
    for x in range(n):
        if tomato_list[y][x] == 1:
            next.append([y, x])
            visited[y][x] = True
        elif tomato_list[y][x] == -1:
            visited[y][x] = True
dq.append(next)

count = -1
while dq:
    next = []
    target_list = dq.pop()
    count += 1
    for target in target_list:
        for move in move_list:
            current_x = target[1] + move[1]
            current_y = target[0] + move[0]
            if current_x < 0 or current_x > n - 1 or current_y < 0 or current_y > m - 1 or visited[current_y][current_x] or tomato_list[current_y][current_x] == -1:
                continue
            else:
                next.append([current_y, current_x])
                visited[current_y][current_x] = True
    if next != []:
        dq.append(next)

for v in visited:
    if False in v:
        print(-1)
        break
else:
    print(count)