import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
total_map = [100] * 200
total_map[1] = 0
move_dict = {}
visited = set()

for _ in range(n + m):
    i, j = map(int, sys.stdin.readline().split())
    move_dict[i] = j

count = 0
target_list = [1]
while target_list:
    count += 1
    temp = set()
    for target in target_list:
        for i in range(1, 7):
            if target + i in move_dict and target + i not in visited:
                total_map[target + i] = 0
                total_map[move_dict[target + i]] = min(count, total_map[move_dict[target + i]])
                visited.add(move_dict[target + i])
                visited.add(target + i)
                temp.add(move_dict[target + i])
            else:
                total_map[target + i] = min(count, total_map[target + i])
                visited.add(target + i)    
                
        for j in range(6):
            if total_map[target + 6 - j] != 0:
                temp.add(target + 6 - j)
                break       
    
    target_list = temp
    if total_map[100] != 100:
        break
    
print(total_map[100])