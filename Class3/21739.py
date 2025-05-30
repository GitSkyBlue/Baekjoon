import sys

n, m = map(int, sys.stdin.readline().split())

total_map = [sys.stdin.readline() for _ in range(n)]
move_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

visited = [[False] * m for _ in range(n)]
x = 0
y = 0
find = False
count = 0
for i in range(n):
    for j in range(m):
        if total_map[i][j] == 'I':
            x = j
            y = i
            find = True
            break
    if find:
        break    

target_list = [[y, x]]
visited[y][x] = True

while target_list:
    temp = []
    for target in target_list:
        for move in move_list:    
            current_x = target[1] + move[1]
            current_y = target[0] + move[0]
            if current_x < 0 or current_x > m - 1 or current_y < 0 or current_y > n - 1 or visited[current_y][current_x]:
                continue
            else:
                if total_map[current_y][current_x] == 'P':
                    count += 1
                elif total_map[current_y][current_x] == 'X':
                    continue
                temp.append([current_y, current_x])
                visited[current_y][current_x] = True
    
    target_list = temp

print(count if count != 0 else 'TT')