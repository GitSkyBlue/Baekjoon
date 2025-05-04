import sys

n = int(sys.stdin.readline())

num_dict = {}

for i in range(n):
    num = int(sys.stdin.readline())
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1 

for k, v in sorted(num_dict.items()):
    for _ in range(v):
        print(k)
