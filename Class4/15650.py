import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

number_list = [i for i in range(1, n + 1)]

for i in combinations(number_list, m):
    print(*i)