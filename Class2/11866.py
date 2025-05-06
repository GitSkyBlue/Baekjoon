n, m = map(int, input().split())

pep_list = [i + 1 for i in range(n)] 
current = 0
count = 0
for i in range(20):
    if pep_list[current] == 0:
        count += 1
    else:
        count += 1
        if count % 3 == 0:
            pep_list[current] = 0
        current += 1
    print(pep_list)