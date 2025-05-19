import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
relation = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

relation_dict = {}
for rel in relation:
    if relation_dict.get(rel[0]):
        relation_dict[rel[0]].append(rel[1])
    else:
        relation_dict[rel[0]] = [rel[1]]

    if relation_dict.get(rel[1]):
        relation_dict[rel[1]].append(rel[0])
    else:
        relation_dict[rel[1]] = [rel[0]]

visited = set()
target_list = set(relation_dict.get(1, set()))
while target_list:
    temp = set()
    for t in target_list:
        for r in relation_dict[t]:
            if r not in visited:
                visited.add(r)
                temp.add(r)

    target_list = temp

if relation_dict.get(1):
    sys.stdout.write(str(len(visited) - 1) + '\n')
else:
    sys.stdout.write(str(0) + '\n')