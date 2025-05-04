n, m = map(int, input().split())

number_dict = {}
for i in range(n, m + 1):
    number_dict[i] = 0

for i in range(2, m // 2 + 1):
    n = 2
    while i * n <= m:
        if i * n in number_dict:
            del number_dict[i * n]
        n += 1

for s in number_dict:
    if s > 1:
        print(s)