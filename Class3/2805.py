import sys

n, m = map(int, sys.stdin.readline().strip().split())
tree_list = list(map(int, sys.stdin.readline().strip().split()))

high = max(tree_list)
low = 0
answer = 0

while low <= high:
    count = 0
    length = (high + low) // 2
    count += sum(tree - length for tree in tree_list if tree > length)
    
    if count >= m:
        answer = length
        low = length + 1
    else:
        high = length - 1

sys.stdout.write(str(answer) + '\n')