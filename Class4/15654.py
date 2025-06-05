import sys

n, m = map(int, sys.stdin.readline().split())
number_list = sorted(list(map(int, sys.stdin.readline().split())))
number_dict = {i: number_list[:] for i in number_list}

def DFS(num, depth, answer):
    if depth >= m:
        print(*answer)
        return
    else:
        for j in number_dict[num]:
            if j not in answer:
                DFS(j, depth + 1, answer + [j])
    pass

for i in number_list:
    DFS(i, 1, [i])