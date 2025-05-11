import sys

n, m = map(int, sys.stdin.readline().strip().split())

passwd_dict = {}

for i in range(n):
    q, a = input().split()
    passwd_dict[q] = a

for i in range(m):
    print((passwd_dict[input()]))