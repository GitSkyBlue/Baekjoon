import sys

input = sys.stdin.readline
n = int(input())
bitmask = 0

for _ in range(n):
    order = input().strip().split()
    if order[0] == 'add':
        bitmask |= (1 << (int(order[1]) - 1))
    elif order[0] == 'remove':
        bitmask &= ~(1 << int(order[1]) - 1)
    elif order[0] == 'check':
        sys.stdout.write('1\n' if bitmask & (1 << (int(order[1]) - 1)) else '0\n')
    elif order[0] == 'toggle':
        bitmask ^= (1 << (int(order[1]) - 1))
    elif order[0] == 'all':
        bitmask = (1 << 20) - 1
    elif order[0] == 'empty':
        bitmask = 0

# import sys

# input = sys.stdin.readline
# n = int(input())
# sets = set()

# for _ in range(n):
#     order = input().strip().split()
#     if order[0] == 'add':
#         sets.add(order[1])
#     elif order[0] == 'remove':
#         sets.discard(order[1])
#     elif order[0] == 'check':
#         print(1 if order[1] in sets else 0)
#     elif order[0] == 'toggle':
#         if order[1] in sets:
#             sets.discard(order[1])
#         else:
#             sets.add(order[1])
#     elif order[0] == 'all':
#         sets = set([str(i) for i in range(1, 21)])
#     elif order[0] == 'empty':
#         sets.clear()

