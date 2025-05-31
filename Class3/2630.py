import sys

n = int(sys.stdin.readline())

paper_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

center = n // 2

for p in paper_list:
    print(p)