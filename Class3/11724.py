import sys

n, m = map(int, sys.stdin.readline().split())

link_dict = {i: [] for i in range(n + 1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    link_dict[a].append(b)
    link_dict[b].append(a)

used = set()
result = 0
for link in range(1, n + 1):
    if link in used:
        continue
    else:
        result += 1
        target_list = link_dict[link]
        while target_list:
            temp = set()
            for target in target_list:
                for l in link_dict[target]:
                    if l not in used:
                        used.add(l)
                        temp.add(l)

            target_list = temp

sys.stdout.write(str(result) + '\n')