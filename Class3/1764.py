n, m = map(int, input().split())

name_dict = {}

for i in range(n):
    name_dict[input()] = 1

dict_keys = name_dict.keys()
for i in range(m):
    inp = input()
    if inp in dict_keys:
        name_dict[inp] += 1

name_dict = {k: v for k, v in name_dict.items() if v > 1}
print(len(name_dict))
for name in sorted(name_dict):
    print(name)