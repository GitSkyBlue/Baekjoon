# import sys

# n = int(sys.stdin.readline())
# page_dict = {k: 0 for k in range(10)}
# for i in range(1, n + 1):
#     for s in str(i):
#         page_dict[int(s)] += 1

# sys.stdout.write(' '.join([str(v) for v in page_dict.values()]))

a = 0
for i in range(1, 999):
    a += len(str(i))

print(a)
# 250347 - 11110
# 239237

# a = 54321
# str_a = '54321'
# s = 0
# for i in range(len(str_a) - 1):
#     print((9 * (10 ** i)) * int(str_a[-(i + 1)]))
#     s += (9 * (10 ** i)) * int(str_a[-(i + 1)])
# s += (a - 10 ** (len(str_a) - 1) + 1) * 5
# print(s)

# s += ((a - 10 ** (len(str_a) - 1)) - 1) * int(str_a[0])
# print(s)

# 54321 - 9999 * 5