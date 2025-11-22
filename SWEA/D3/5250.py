cases = int(input())

for case in range(cases):
    row = int(input())

    map_list = [list(map(int, input().split())) for _ in range(row)]

    print(map_list)

    queue = [[1, 0], [0, 1]]
