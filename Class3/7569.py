import sys
from collections import deque

n, m, h = map(int, sys.stdin.readline().split())
dq = deque()

tomato_list = []
visited = [[[False] * n for _ in range(m)] for _ in range(h)]
for _ in range(h):
    tomato_list.append([list(map(int, sys.stdin.readline().split())) for _ in range(m)])

for i in range(h):
    for j in range(m):
        for k in range(n):
            if tomato_list[i][j][k] == 1:
                dq.append([i, j, k, 0])
                visited[i][j][k] = True
            elif tomato_list[i][j][k] == -1:
                visited[i][j][k] = True

move_list = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [-1, 0, 0], [1, 0, 0]]
while dq:
    value = dq.popleft()
    i = value[0]
    j = value[1]
    k = value[2]
    s = value[3]
    for move in move_list:
        current_x = move[2] + k
        current_y = move[1] + j
        current_h = move[0] + i
        if current_x < 0 or current_x > n - 1 or current_y < 0 or current_y > m - 1 or current_h < 0 or current_h > h - 1 or visited[current_h][current_y][current_x]:
            continue
        else:
            if tomato_list[current_h][current_y][current_x] == 0:
                visited[current_h][current_y][current_x] = True
                dq.append([current_h, current_y, current_x, s + 1])
            elif tomato_list[current_h][current_y][current_x] == -1:
                continue

br = False
for i in range(h):
    for j in range(m):
        if False in visited[i][j]:
            print(-1)
            br = True
            break
    if br:
        break
else:
    print(s)
    