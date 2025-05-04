n, m = map(int, input().split())

pep_list = [i for i in range(1, n + 1)]

for i in range(1, n + 1):
    temp_list = pep_list
    n = 1
    while n * 3 - 1 < len(pep_list):
        del temp_list[n * 3 - 1]
        n += 1
    pep_list += temp_list
    print(pep_list)
# print([1, 2] + [3, 4])