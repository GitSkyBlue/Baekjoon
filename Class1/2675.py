n = int(input())
data = [input().split() for _ in range(n)]

for d in data:
    for s in d[1]:
        print(s * int(d[0]), end='')
    print()