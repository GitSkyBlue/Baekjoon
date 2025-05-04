import sys

number_list = list(map(int, sys.stdin.read().splitlines()))[1:]

for i in range(len(number_list) // 2):
    n, m = number_list[i * 2], number_list[i * 2 + 1]
    base = [[i + 1 for i in range(m)] for _ in range(n + 1)]
    for k in range(len(base) - 1):
        for j in range(m):
            base[k + 1][j] = sum(base[k][:j + 1])
    print(base[n][m - 1])