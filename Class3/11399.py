import sys

n = int(sys.stdin.readline().strip())

waitng_list = sorted(list(map(int, sys.stdin.readline().strip().split())))

waited = 0
for i in range(len(waitng_list) - 1, -1, -1):
    waitng_list[i] = sum(waitng_list[:i + 1])
print(sum(waitng_list))