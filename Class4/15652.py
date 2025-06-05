import sys

n, m = map(int, sys.stdin.readline().split())
number_list = [i for i in range(1, n + 1)]
number_dict = {i: list(range(i, n + 1)) for i in range(1, n + 1)}

def DFS(num, depth, answer):
    if depth >= m:
        print(*answer)
        return
    else:
        for j in number_dict[num]:
            DFS(j, depth + 1, answer + [j])

for i in range(1, n + 1):
    DFS(i, 1, [i])