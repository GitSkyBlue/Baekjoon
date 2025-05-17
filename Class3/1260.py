n, m, k = map(int, input().split())

node_dict = {}
node_list = [list(map(int, input().split())) for _ in range(m)]

for node in node_list:
    if node[0] in node_dict:
        node_dict[node[0]] += [node[1]]
    else:
        node_dict[node[0]] = [node[1]]
    if node[1] in node_dict:
        node_dict[node[1]] += [node[0]]
    else:
        node_dict[node[1]] = [node[0]]

answer = {}
seq = 1
def DFS(node_dict, node):
    global seq
    if node in answer:
        return
    
    answer[node] = seq
    seq += 1
    
    for n in sorted(node_dict[node]):
        DFS(node_dict, n)

if k in node_dict:
    DFS(node_dict, k)
else:
    answer = [str(k)]
print(' '.join(list(map(str, answer))))

answer = {}
next = [k]
seq = 1
answer[k] = seq

while next:
    if k not in node_dict:
        break
    temp = []
    for nex in next:
        for n in sorted(node_dict[nex]):
            if n in answer:
                pass
            else:
                temp.append(n)
                seq += 1
                answer[n] = seq
    next = temp

print(' '.join(list(map(str, answer))))
