n = int(input())

loc_list = [list(map(int, input().split())) for _ in range(n)]
loc_list.sort()
for i, j in loc_list:
    print(i, j)