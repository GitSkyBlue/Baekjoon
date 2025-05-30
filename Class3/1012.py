import sys

n = int(sys.stdin.readline())
move_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for _ in range(n):
    n, m, k = map(int, sys.stdin.readline().split())
    total_map = [[0] * n for _ in range(m)]
    cab_loc = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
    visited = [[False] * n for _ in range(m)]
    for cab in cab_loc:
        total_map[cab[1]][cab[0]] = 1
    count = 0
    
    for i in range(m):
        for j in range(n):
            if total_map[i][j] == 0 or visited[i][j]:
                continue
            else:
                count += 1
                visited[i][j] = True
                target_list = [[i, j]]
                while target_list:
                    temp = []
                    for target in target_list:
                        for move in move_list:
                            current_x = move[1] + target[1]
                            current_y = move[0] + target[0]
                            if current_x < 0 or current_x > n - 1 or current_y < 0 or current_y > m - 1 or total_map[current_y][current_x] == 0 or visited[current_y][current_x]:
                                continue
                            else:
                                visited[current_y][current_x] = True
                                temp.append([current_y, current_x])

                    target_list = temp
    
    print(count)