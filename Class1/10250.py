n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

for d in data:
    row = d[2] // d[0] + (1 if d[2] % d[0] != 0 else 0)
    col = d[2] % d[0]
    if col == 0:
        col = d[0]
    if row < 10:
        print(str(col) + '0' + str(row))
    else:
        print(str(col) + str(row))