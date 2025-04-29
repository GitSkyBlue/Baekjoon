import sys

n = int(sys.stdin.readline())

num_dict = {}
for i in range(10000):
    num_dict[i + 1] = 0

for _ in range(n):
    inp = int(input())

    num_dict[inp] += 1

for key, value in sorted(num_dict.items()):
    for k in range(value):
        print(key)