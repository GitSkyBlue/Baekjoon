import sys
from collections import deque

n = sys.stdin.readline()

number_list = sys.stdin.read().splitlines()

for i in range(0, len(number_list), 2):
    count = 0
    target = int(number_list[i].split()[1])
    compare_list = deque(map(int, number_list[i + 1].split()))
    target_num = compare_list[target]
    while len(compare_list) != 0:
        max_value = max(compare_list)
        ele = compare_list.popleft()
        target -= 1
        if ele >= max_value:
            count += 1
            if target == -1 and ele == target_num:
                print(count)
                break
        else:
            if target == -1:
                target = len(compare_list)
            compare_list.append(ele)