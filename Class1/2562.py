import sys

max_num = 0
max_arg = 0
for i, n in enumerate(sys.stdin):
    if int(n) > max_num:
        max_num = int(n)
        max_arg = i

print(max_num)
print(max_arg + 1)