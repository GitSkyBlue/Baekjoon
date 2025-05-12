import sys

n = int(sys.stdin.readline())
page_dict = {k: 0 for k in range(10)}

# for i in range(n, 100, -1):
#     num = i
#     print(num)
#     count = 1
#     while num > 0:
#         page_dict[num % 10] += count
#         num //= 10
#         count += 1
for i in range(1, n + 1):
    num = i
    while num > 0:
        page_dict[num % 10] += 1
        num //= 10

sys.stdout.write(' '.join([str(v) for v in page_dict.values()]))