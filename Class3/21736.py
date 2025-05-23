import sys

n, m = map(int, sys.stdin.readline().split())

loc_list = [sys.stdin.readline().strip() for _ in range(n)]

print()
for loc in loc_list:
    print(loc)

for loc in [[0] * m for _ in range(n)]:
    for l in loc:  
        print(l, end='')

    print()