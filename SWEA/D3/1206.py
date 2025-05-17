floor_list = [list(map(int, input().split())) for _ in range(20)]

for i in range(0, len(floor_list), 2):
    answer = 0 
    for j in range(floor_list[i][0] - 4):
        current = floor_list[i + 1][j + 2]
        front = max(floor_list[i + 1][j + 1], floor_list[i + 1][j])
        back = max(floor_list[i + 1][j + 3], floor_list[i + 1][j + 4])
        if current - max(front, back) > 0:
            answer += current - max(front, back)
    
    print(f'#{(i // 2 + 1)} {answer}')
