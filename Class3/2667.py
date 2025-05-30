import sys

n = int(sys.stdin.readline())

home_list = []
for _ in range(n):
    home_list.append(list(sys.stdin.readline().strip()))

visited = [[False] * n for _ in range(n)]
move_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
answer = []

for i in range(n):
    for j in range(n):
        if visited[i][j] or home_list[i][j] == '0':
            continue
        count = 1
        target_list = [[i, j]]
        while target_list:
            temp = []
            for target in target_list:
                visited[target[0]][target[1]] = True
                for move in move_list:
                    current_x = target[1] + move[1]
                    current_y = target[0] + move[0]
                    if current_x < 0 or current_x > n - 1 or current_y < 0 or current_y > n - 1 or visited[current_y][current_x]:
                        continue
                    else:
                        if home_list[current_y][current_x] == '1':
                            temp.append([current_y, current_x])
                            visited[current_y][current_x] = True
                            count += 1
                        else:
                            continue
            target_list = temp
        answer.append(count)

print(len(answer))
for a in sorted(answer):
    print(a)